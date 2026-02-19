# Amazon Bedrock - Documentação e Troubleshooting

Esta pasta contém documentação específica sobre Amazon Bedrock, incluindo resolução de problemas de quotas e throttling.

## Arquivos

### 📋 [resolucao-throttling-quotas.md](resolucao-throttling-quotas.md)
**Guia completo de resolução de erros de throttling**

Conteúdo:
- Análise da causa raiz dos erros 429
- 6 etapas de resolução (verificação, aumento de quotas, tickets, cross-region, retry, monitoramento)
- Soluções alternativas (Provisioned Throughput)
- Checklist de ações
- Comandos AWS CLI prontos para uso

**Use este documento quando:**
- Receber erro "Too many tokens per day"
- Precisar aumentar quotas do Bedrock
- Implementar retry logic na aplicação
- Configurar monitoramento de uso

---

### 🎯 [CONCLUSAO-ANALISE.md](CONCLUSAO-ANALISE.md) ⭐ **IMPORTANTE!**
**Descoberta crucial sobre quotas do Bedrock**

Conteúdo:
- Descoberta: Quota padrão é 4M tokens/min (mas desabilitada)
- Problema real: Acesso não habilitado (não falta de quota)
- Solução correta: Solicitar HABILITAÇÃO (não aumento)
- Template simplificado para ticket
- Diferença entre habilitação vs aumento

**LEIA ESTE DOCUMENTO ANTES DE ABRIR O TICKET!**

---

### 📧 [ticket-aws-support-bedrock-quotas.md](ticket-aws-support-bedrock-quotas.md)
**Template completo para abrir ticket no AWS Support**

Conteúdo:
- Informações básicas do ticket
- Descrição detalhada do problema
- Análise de quotas atual
- Solicitação de aumento com justificativas
- Perguntas para o Support
- Evidências e comandos executados

**Use este documento quando:**
- Precisar abrir ticket para quotas não ajustáveis
- Solicitar acesso inicial ao Bedrock
- Pedir aumento de limites que requerem aprovação manual

---

## Problema Atual

**Status:** 🟡 Aguardando resposta AWS Support  
**Ticket:** Aberto em 16/02/2026  
**Erro:** HTTP 429 - "Too many tokens per day"  
**Causa:** Quotas em 0.0 (acesso não habilitado)  
**Descoberta:** Quota padrão é 4M tokens/min, mas está desabilitada  
**Solução:** Solicitada HABILITAÇÃO via AWS Support  
**Região:** us-east-1  
**Account:** 624012998785

### Expectativa de Resposta
- **Resposta inicial:** 24-48 horas
- **Aprovação:** 2-5 dias úteis
- **Após aprovação:** Quotas ativadas automaticamente

### Componentes Afetados
- ❌ Knowledge Base Sync (PoliticasRH-KnowledgeBase)
- ❌ Playground do Bedrock
- ❌ Agent Testing (agent-rh-chatbot)
- ❌ Model Invocation (todos os modelos)

### Modelos Necessários
1. **Amazon Titan Text Embeddings v2.0** (Priority 1)
   - Para: Knowledge Base embeddings
   - Quota atual: 0.0 tokens/dia
   - Solicitado: 100.000 tokens/dia

2. **Amazon Nova Micro 1.0** (Priority 1)
   - Para: Agent RH chatbot
   - Quota atual: 0.0 tokens/dia
   - Solicitado: 50.000 tokens/dia

3. **Anthropic Claude 3 Haiku** (Priority 2)
   - Para: Testes alternativos
   - Quota atual: 0.0 tokens/dia
   - Solicitado: 50.000 tokens/dia

---

## Próximos Passos

### 1. Verificar Quotas Ajustáveis (AGORA)
```bash
# Executar comandos na pasta raiz do projeto
cd "P:\Meu Drive\Documentos\Cursos\AI"

# Verificar quotas do Titan Embeddings
aws service-quotas list-service-quotas \
  --service-code bedrock \
  --region us-east-1 \
  --profile Master \
  --query "Quotas[?contains(QuotaName, 'Titan') && contains(QuotaName, 'embed')]"
```

### 2. Solicitar Aumentos (SE AJUSTÁVEL)
```bash
# Exemplo: aumentar quota ajustável
aws service-quotas request-service-quota-increase \
  --service-code bedrock \
  --quota-code [CODIGO_DA_QUOTA] \
  --desired-value 100000 \
  --region us-east-1 \
  --profile Master
```

### 3. Abrir Ticket (SE NÃO AJUSTÁVEL)
- Acessar: https://console.aws.amazon.com/support/home
- Usar template: `ticket-aws-support-bedrock-quotas.md`
- Anexar screenshots dos erros

---

## Comandos Úteis

### Listar todas as quotas do Bedrock
```bash
aws service-quotas list-service-quotas \
  --service-code bedrock \
  --region us-east-1 \
  --profile Master \
  --output table
```

### Verificar quota específica
```bash
aws service-quotas get-service-quota \
  --service-code bedrock \
  --quota-code L-A60EE1AF \
  --region us-east-1 \
  --profile Master
```

### Listar modelos disponíveis
```bash
aws bedrock list-foundation-models \
  --region us-east-1 \
  --profile Master \
  --query "modelSummaries[*].[modelId,modelName,providerName]" \
  --output table
```

### Verificar solicitações de aumento pendentes
```bash
aws service-quotas list-requested-service-quota-change-history \
  --service-code bedrock \
  --region us-east-1 \
  --profile Master
```

---

## Referências Rápidas

- **Documentação AWS Bedrock:** https://docs.aws.amazon.com/bedrock/
- **Service Quotas Console:** https://console.aws.amazon.com/servicequotas/
- **AWS Support Console:** https://console.aws.amazon.com/support/
- **Bedrock Pricing:** https://aws.amazon.com/bedrock/pricing/
- **Service Health Dashboard:** https://status.aws.amazon.com/

---

**Projeto:** POC Agente RH - Maestriacloud  
**Última atualização:** 16/02/2026
