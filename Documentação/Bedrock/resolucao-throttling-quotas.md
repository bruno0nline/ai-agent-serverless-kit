# Resolução de Erros de Throttling do Amazon Bedrock

## Análise da Causa Raiz

Os erros ThrottlingException com mensagens "Too many tokens per day" ocorrem porque:

1. A conta tem cotas de valor **zero (0.0)** para limites de invocação de modelo
2. Novas contas AWS normalmente têm cotas iniciais menores que os valores padrão
3. Alguns modelos têm cotas fixas não ajustáveis que requerem tratamento especial

---

## Etapas de Resolução (Ordem de Execução)

### ETAPA 1: Verificar Status Atual da Cota ✅

**Objetivo:** Identificar quais quotas são ajustáveis e quais requerem aprovação manual

**Comandos:**

```bash
# Ver detalhes de uma quota específica
aws service-quotas get-service-quota \
  --service-code bedrock \
  --quota-code L-A60EE1AF \
  --region us-east-1 \
  --profile Master

# Listar todas as quotas do Bedrock
aws service-quotas list-service-quotas \
  --service-code bedrock \
  --region us-east-1 \
  --profile Master
```

**O que verificar:**
- `Adjustable: true` → Pode aumentar via CLI/Console
- `Adjustable: false` → Requer ticket AWS Support
- `Value: 0.0` → Sem acesso habilitado

---

### ETAPA 2: Solicitar Aumentos de Cota (Quotas Ajustáveis) 🔧

**Objetivo:** Aumentar quotas que permitem ajuste self-service

**Comando:**

```bash
aws service-quotas request-service-quota-increase \
  --service-code bedrock \
  --quota-code L-A60EE1AF \
  --desired-value 200000 \
  --region us-east-1 \
  --profile Master
```

**Quando usar:**
- Apenas para quotas com `Adjustable: true`
- Aprovação geralmente automática ou em minutos/horas

**Valores recomendados para POC:**
- Embeddings (Titan): 100.000 tokens/dia
- Modelos de chat (Nova Micro): 50.000 tokens/dia
- Modelos alternativos (Claude Haiku): 50.000 tokens/dia

---

### ETAPA 3: Lidar com Cotas NÃO Ajustáveis 📧

**Objetivo:** Solicitar acesso a modelos on-demand que requerem aprovação manual

**Processo:**
1. Abrir ticket no AWS Support Console
2. Tipo: "Service Limit Increase"
3. Serviço: "Amazon Bedrock"
4. Incluir informações detalhadas (ver template em `ticket-aws-support-bedrock-quotas.md`)

**Informações obrigatórias:**
- Nome da cota e ID do modelo
- Região de destino (us-east-1)
- Explicação do caso de uso
- Uso projetado (tokens/solicitações por minuto)
- Tokens médios de entrada e saída por solicitação

**Tempo de resposta:** 24-48h ou mais

**⚠️ IMPORTANTE - Tratamento de Prioridade:**
- AWS prioriza clientes que **já estão gerando tráfego**
- Solicitações podem ser negadas se você não tiver uso atual
- **Estratégia:** Pedir valores pequenos primeiro (10k-50k), usar tudo, depois pedir mais

---

### ETAPA 4: Implementar Perfis de Inferência Entre Regiões 🌍

**Objetivo:** Distribuir carga entre múltiplas regiões AWS para evitar throttling

**Como funciona:**
- Cada região AWS mantém pools de capacidade independentes
- Se us-east-1 está limitada, roteia para us-west-2, eu-west-1, etc
- Modelos como Claude 4.5 Sonnet oferecem perfis de inferência global

**Quando usar:**
- Quando uma região específica está com throttling
- Para aplicações de alta disponibilidade
- Durante picos de tráfego

**Configuração:**
```python
# Exemplo de configuração cross-region
import boto3

regions = ['us-east-1', 'us-west-2', 'eu-west-1']
clients = {region: boto3.client('bedrock-runtime', region_name=region) for region in regions}

# Implementar lógica de fallback entre regiões
```

---

### ETAPA 5: Configurar Lógica de Repetição com Exponential Backoff ⏱️

**Objetivo:** Implementar retry automático quando receber erro 429 (throttling)

**Código Python:**

```python
from botocore.config import Config
import boto3

# Configurar retry com backoff exponencial
config = Config(
    retries={
        'max_attempts': 10,  # Padrão é 3
        'mode': 'adaptive'   # Ajusta automaticamente baseado em erros
    }
)

bedrock_runtime = boto3.client('bedrock-runtime', config=config, region_name='us-east-1')
```

**Regras importantes:**
- Backoff de repetição deve durar **1 minuto completo** ao atingir cotas por minuto
- Sincronize tentativas com o ciclo de atualização de cota (60 segundos)
- Distribua solicitações em vários segundos dentro de 1 minuto

**Quando usar:**
- **SEMPRE!** É boa prática em qualquer aplicação
- Evita perder requisições por throttling temporário
- Melhora resiliência da aplicação

---

### ETAPA 6: Monitorar o Uso com CloudWatch 📊

**Objetivo:** Acompanhar uso em tempo real para evitar atingir limites

**Métricas importantes:**
- `InputTokenCount`: Tokens de entrada consumidos
- `OutputTokenCount`: Tokens de saída gerados
- `Invocations`: Número de chamadas ao modelo
- `ThrottledRequests`: Requisições bloqueadas por throttling

**Como configurar:**

```bash
# Ver métricas via CLI
aws cloudwatch get-metric-statistics \
  --namespace AWS/Bedrock \
  --metric-name Invocations \
  --dimensions Name=ModelId,Value=amazon.titan-embed-text-v2:0 \
  --start-time 2026-02-16T00:00:00Z \
  --end-time 2026-02-16T23:59:59Z \
  --period 3600 \
  --statistics Sum \
  --region us-east-1 \
  --profile Master
```

**⚠️ Observação:** O painel do Service Quotas mostra apenas cotas configuradas, **NÃO o uso em tempo real**. Use CloudWatch para monitoramento real.

---

## Soluções Alternativas

### Opção: Throughput Provisionado 💰

**O que é:**
- Capacidade dedicada (não compartilhada com outros clientes)
- Você paga por hora/mês independente do uso
- Zero throttling, performance garantida

**Quando usar:**
- Produção com alto volume previsível
- Aplicações críticas que não podem ter throttling
- Quando on-demand não atende requisitos de SLA

**Custo:**
- Mais caro que on-demand
- Cobrança por Model Units (MU) por hora
- Exemplo: Claude 3 Haiku ~$8-10/hora por MU

**Como adquirir:**
1. Console Bedrock → Provisioned Throughput
2. Selecionar modelo e quantidade de Model Units
3. Escolher commitment (sem compromisso, 1 mês, 6 meses)

---

## Tempo de Atualização de Quotas

**Importante entender:**

- Quotas são atualizadas **por minuto** (não por segundo)
- Limite de tokens/dia é distribuído ao longo de 24h
- Exemplo: 100.000 tokens/dia = ~69 tokens/minuto

**Otimização:**
- Distribua solicitações uniformemente ao longo do minuto
- Não envie todas requisições no primeiro segundo
- Use rate limiting na aplicação

---

## Considerações de Disponibilidade do Serviço

**Se enfrentar throttling sem exceder quotas:**

1. Verificar integridade do serviço regional:
   - AWS Service Health Dashboard
   - https://status.aws.amazon.com/

2. Considerar usar perfis cross-region quando:
   - Uma região enfrenta restrições de capacidade
   - Há manutenção programada
   - Picos de demanda regional

3. Implementar circuit breaker:
   - Detectar falhas consecutivas
   - Alternar automaticamente para região backup
   - Retornar à região principal quando estável

---

## Checklist de Ações para o Projeto

### Imediato (Hoje)
- [ ] Verificar quotas ajustáveis via CLI
- [ ] Solicitar aumento das quotas ajustáveis
- [ ] Preparar ticket para quotas não ajustáveis

### Curto Prazo (Esta Semana)
- [ ] Abrir ticket AWS Support se necessário
- [ ] Implementar retry com backoff no código
- [ ] Configurar monitoramento CloudWatch

### Médio Prazo (Próximas Semanas)
- [ ] Implementar cross-region fallback
- [ ] Avaliar necessidade de Provisioned Throughput
- [ ] Otimizar uso de tokens (prompt engineering)

---

## Referências

- [AWS Bedrock Quotas Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html)
- [AWS Service Quotas User Guide](https://docs.aws.amazon.com/servicequotas/latest/userguide/)
- [Boto3 Retry Configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/retries.html)
- [CloudWatch Metrics for Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-cw.html)

---

**Última atualização:** 16/02/2026  
**Projeto:** POC Agente RH - Maestriacloud  
**Região:** us-east-1  
**Account ID:** 624012998785
