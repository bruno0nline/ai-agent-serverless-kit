# 💰 Documentação de Custos - AI Agent Serverless Kit

**Projeto:** Maestriacloud - Multi-Agent Collaboration  
**Última atualização:** 20/02/2026  
**Versão:** 1.0

---

## 📊 Visão Geral

Este documento detalha os custos reais e estimados do projeto AI Agent Serverless Kit, incluindo a arquitetura Multi-Agent implementada.

---

## 🏗️ Componentes e Custos

### 1. Amazon Bedrock - Foundation Models

#### Supervisor Agent (Patrícia)
- **Modelo:** Amazon Nova Pro 1.0
- **Tipo:** On-demand
- **Pricing:**
  - Input: $0.80 / 1M tokens
  - Output: $3.20 / 1M tokens
- **Uso estimado (POC):**
  - 100 interações/mês
  - ~500 tokens input/interação
  - ~200 tokens output/interação
- **Custo mensal:** ~$0.10

#### Collaborator Agent RH (Carla)
- **Modelo:** Amazon Nova Micro 1.0
- **Tipo:** On-demand
- **Pricing:**
  - Input: $0.035 / 1M tokens
  - Output: $0.14 / 1M tokens
- **Uso estimado (POC):**
  - 50 interações/mês (delegadas)
  - ~300 tokens input/interação
  - ~150 tokens output/interação
- **Custo mensal:** ~$0.01

#### Collaborator Agent Vendas (Rafael)
- **Modelo:** Claude 3.5 Haiku v1
- **Tipo:** On-demand
- **Pricing:**
  - Input: $0.80 / 1M tokens
  - Output: $4.00 / 1M tokens
- **Uso estimado (POC):**
  - 50 interações/mês (delegadas)
  - ~400 tokens input/interação
  - ~200 tokens output/interação
- **Custo mensal:** ~$0.08

**Total Agents (POC):** ~$0.19/mês

---

### 2. Amazon Bedrock - Embeddings

#### Titan Text Embeddings v2.0
- **Pricing:** $0.02 / 1M tokens
- **Uso:**
  - 2 Knowledge Bases
  - ~10.000 tokens totais (documentos)
  - Sincronização: 1x/mês
- **Custo mensal:** ~$0.0002 (desprezível)

---

### 3. Amazon S3

#### Armazenamento de Documentos
- **Bucket:** `maestriatec-rag-knowledge-base`
- **Conteúdo:**
  - /RH/ - 3 arquivos (~5 KB)
  - /Cursos/ - 1 arquivo (~7 KB)
- **Pricing:** $0.023 / GB-mês
- **Custo mensal:** < $0.01

#### S3 Vectors (Vector Database)
- **Pricing:** $0.023 / GB-mês
- **Tamanho estimado:** ~1 MB (embeddings)
- **Custo mensal:** < $0.01

**Total S3:** ~$0.02/mês

---

### 4. AWS Lambda (Action Groups)

#### Lambda Function - Consulta Feriados
- **Runtime:** Python 3.13
- **Memória:** 128 MB
- **Invocações:** ~10/mês (POC)
- **Duração média:** 100ms
- **Pricing:**
  - Requests: $0.20 / 1M requests
  - Compute: $0.0000166667 / GB-second
- **Custo mensal:** < $0.01

#### Lambda Layer
- **Tamanho:** ~19 MB (holidays library)
- **Armazenamento:** Incluído no free tier
- **Custo mensal:** $0.00

**Total Lambda:** < $0.01/mês

---

### 5. AWS IAM (Roles e Policies)

- **Custo:** $0.00 (sem cobrança)

---

### 6. CloudWatch Logs (Monitoramento)

- **Logs gerados:** ~10 MB/mês (POC)
- **Pricing:** $0.50 / GB ingerido
- **Custo mensal:** < $0.01

---

## 💵 Resumo de Custos

### POC (100 interações/mês)

| Componente | Custo Mensal |
|------------|--------------|
| Agents (3x) | $0.19 |
| Embeddings | $0.00 |
| S3 Storage + Vectors | $0.02 |
| Lambda | $0.01 |
| CloudWatch | $0.01 |
| **TOTAL** | **~$0.23/mês** |

### Produção Pequena (1.000 interações/mês)

| Componente | Custo Mensal |
|------------|--------------|
| Agents (3x) | $1.90 |
| Embeddings | $0.00 |
| S3 Storage + Vectors | $0.02 |
| Lambda | $0.05 |
| CloudWatch | $0.03 |
| **TOTAL** | **~$2.00/mês** |

### Produção Média (10.000 interações/mês)

| Componente | Custo Mensal |
|------------|--------------|
| Agents (3x) | $19.00 |
| Embeddings | $0.01 |
| S3 Storage + Vectors | $0.05 |
| Lambda | $0.50 |
| CloudWatch | $0.30 |
| **TOTAL** | **~$19.86/mês** |

---

## 📈 Comparação com Alternativas

### Solução Tradicional (EC2 + RDS)

| Componente | Custo Mensal |
|------------|--------------|
| EC2 t3.small (24/7) | $15.18 |
| RDS db.t3.micro | $15.33 |
| ELB | $16.20 |
| **TOTAL** | **$46.71/mês** |

**Economia com Serverless:** 95% (POC) a 57% (10K interações)

### Solução SaaS (ex: Intercom, Zendesk)

| Plano | Custo Mensal |
|-------|--------------|
| Básico | $39-79 |
| Profissional | $99-149 |
| Enterprise | $199+ |

**Economia com Serverless:** 99% (POC) a 90% (10K interações)

---

## 🎯 ROI Estimado

### Cenário: Empresa com 50 funcionários

**Sem Agent:**
- Atendimento RH: 2h/dia
- Custo hora RH: $25/h
- Custo mensal: $1.000

**Com Agent:**
- Redução de 80% no atendimento
- Custo Agent: $2-20/mês
- Economia mensal: $780-998

**ROI:** 3.900% a 49.900%

---

## 📊 Monitoramento de Custos

### Ferramentas Disponíveis

1. **AWS Cost Explorer**
   - Acesso via Console AWS
   - Filtrar por serviço: "Amazon Bedrock"
   - Granularidade: Diária/Mensal

2. **Script `monitor_costs.py`**
   ```bash
   cd tests/
   python3 monitor_costs.py
   ```
   - Relatório automático dos últimos 7 dias
   - Projeção de custo mensal
   - Exporta para JSON

3. **AWS Budgets**
   - Criar alerta para custos > $5/mês
   - Notificação por email

### Comandos AWS CLI

```bash
# Custos do mês atual
aws ce get-cost-and-usage \
  --time-period Start=2026-02-01,End=2026-02-28 \
  --granularity MONTHLY \
  --metrics "UnblendedCost" \
  --filter file://bedrock-filter.json \
  --profile Master

# Criar arquivo bedrock-filter.json:
{
  "Dimensions": {
    "Key": "SERVICE",
    "Values": ["Amazon Bedrock"]
  }
}
```

---

## 💡 Dicas para Otimização de Custos

### 1. Escolha do Modelo

| Modelo | Custo | Quando Usar |
|--------|-------|-------------|
| Nova Micro | Mais barato | Tarefas simples, respostas curtas |
| Nova Pro | Médio | Orquestração, raciocínio complexo |
| Claude Haiku | Médio | Respostas rápidas, conversação |
| Claude Sonnet | Caro | Tarefas complexas, análise profunda |

**Recomendação atual:**
- ✅ Supervisor: Nova Pro (orquestração)
- ✅ Collaborators: Nova Micro / Claude Haiku (execução)

### 2. Otimização de Prompts

- Instruções concisas e diretas
- Evitar repetições desnecessárias
- Usar system prompts eficientes
- Limitar tamanho de contexto

### 3. Caching de Respostas

- Implementar cache para perguntas frequentes
- Usar DynamoDB ou ElastiCache
- Reduz invocações do Bedrock em até 70%

### 4. Batching de Requisições

- Agrupar múltiplas perguntas quando possível
- Reduz overhead de invocações

### 5. Monitoramento Contínuo

- Revisar custos semanalmente
- Identificar picos anormais
- Ajustar limites de uso

---

## 🚨 Alertas de Custo

### Configurar AWS Budget

```bash
# Via Console AWS
1. Acessar AWS Budgets
2. Create Budget
3. Cost Budget
4. Budget amount: $10/mês
5. Alert threshold: 80% ($8)
6. Email notification
```

### Limites Recomendados

| Ambiente | Limite Mensal | Alerta em |
|----------|---------------|-----------|
| POC | $5 | $4 (80%) |
| Dev | $20 | $16 (80%) |
| Produção | $100 | $80 (80%) |

---

## 📝 Histórico de Custos

### Fevereiro 2026

| Período | Custo Real | Interações | Custo/Interação |
|---------|------------|------------|-----------------|
| 01-10/02 | $0.00 | 0 | - |
| 11-19/02 | $0.00 | 0 | - |
| 20-28/02 | TBD | TBD | TBD |

**Nota:** Custos podem levar até 24h para aparecer no Cost Explorer.

---

## 🔗 Links Úteis

- [AWS Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)
- [AWS Cost Explorer](https://console.aws.amazon.com/cost-management/home)
- [AWS Budgets](https://console.aws.amazon.com/billing/home#/budgets)
- [AWS Pricing Calculator](https://calculator.aws/)

---

## 📞 Suporte

Para dúvidas sobre custos:
- Revisar este documento
- Executar `monitor_costs.py`
- Consultar AWS Cost Explorer
- Abrir ticket AWS Support (se necessário)

---

**Última atualização:** 20/02/2026  
**Próxima revisão:** 27/02/2026  
**Responsável:** Bruno Mendes Augusto
