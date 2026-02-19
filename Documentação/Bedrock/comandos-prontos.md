# Comandos Prontos - Amazon Bedrock Quotas

Este arquivo contém comandos prontos para copiar e colar no terminal.

---

## 📋 Verificar Quotas Específicas

### Claude 3 Haiku (Cross-Region)
```bash
aws service-quotas get-service-quota --service-code bedrock --quota-code L-DCADBC78 --region us-east-1 --profile Master
```

### Amazon Nova Micro (Cross-Region)
```bash
aws service-quotas get-service-quota --service-code bedrock --quota-code L-DC7FF66C --region us-east-1 --profile Master
```

### Amazon Nova 2 Lite (Cross-Region)
```bash
aws service-quotas get-service-quota --service-code bedrock --quota-code L-C6F5908D --region us-east-1 --profile Master
```

### Cohere Embed V4 (Cross-Region)
```bash
aws service-quotas get-service-quota --service-code bedrock --quota-code L-4C3F0FE6 --region us-east-1 --profile Master
```

---

## 🔧 Solicitar Aumentos (Quotas Ajustáveis)

⚠️ **ATENÇÃO:** Estas são quotas Cross-Region (tokens por minuto), não On-Demand (tokens por dia).

### Claude 3 Haiku - 10.000 tokens/minuto
```bash
aws service-quotas request-service-quota-increase \
  --service-code bedrock \
  --quota-code L-DCADBC78 \
  --desired-value 10000 \
  --region us-east-1 \
  --profile Master
```

### Amazon Nova Micro - 10.000 tokens/minuto
```bash
aws service-quotas request-service-quota-increase \
  --service-code bedrock \
  --quota-code L-DC7FF66C \
  --desired-value 10000 \
  --region us-east-1 \
  --profile Master
```

### Amazon Nova 2 Lite - 10.000 tokens/minuto
```bash
aws service-quotas request-service-quota-increase \
  --service-code bedrock \
  --quota-code L-C6F5908D \
  --desired-value 10000 \
  --region us-east-1 \
  --profile Master
```

### Cohere Embed V4 - 10.000 tokens/minuto
```bash
aws service-quotas request-service-quota-increase \
  --service-code bedrock \
  --quota-code L-4C3F0FE6 \
  --desired-value 10000 \
  --region us-east-1 \
  --profile Master
```

---

## 📊 Verificar Solicitações Pendentes

### Listar todas solicitações pendentes
```bash
aws service-quotas list-requested-service-quota-change-history \
  --service-code bedrock \
  --region us-east-1 \
  --profile Master \
  --status PENDING
```

### Listar todas solicitações (incluindo aprovadas/negadas)
```bash
aws service-quotas list-requested-service-quota-change-history \
  --service-code bedrock \
  --region us-east-1 \
  --profile Master
```

---

## 🔍 Listar Modelos Disponíveis

### Todos os modelos
```bash
aws bedrock list-foundation-models \
  --region us-east-1 \
  --profile Master \
  --output table
```

### Apenas modelos Amazon
```bash
aws bedrock list-foundation-models \
  --by-provider amazon \
  --region us-east-1 \
  --profile Master \
  --output table
```

### Apenas modelos Anthropic
```bash
aws bedrock list-foundation-models \
  --by-provider anthropic \
  --region us-east-1 \
  --profile Master \
  --output table
```

### Apenas modelos de Embedding
```bash
aws bedrock list-foundation-models \
  --region us-east-1 \
  --profile Master \
  --query "modelSummaries[?contains(modelId, 'embed')]" \
  --output table
```

---

## 📦 Verificar S3 Bucket

### Listar arquivos na pasta RH
```bash
aws s3 ls s3://maestriatec-rag-knowledge-base/RH/ --recursive --profile Master
```

### Ver detalhes dos arquivos
```bash
aws s3 ls s3://maestriatec-rag-knowledge-base/RH/ --recursive --human-readable --summarize --profile Master
```

### Baixar um arquivo específico
```bash
aws s3 cp s3://maestriatec-rag-knowledge-base/RH/beneficios.md . --profile Master
```

---

## 🔐 Verificar Permissões IAM

### Listar roles do Bedrock
```bash
aws iam list-roles --query "Roles[?contains(RoleName, 'Bedrock')]" --profile Master
```

### Ver detalhes da role da Knowledge Base
```bash
aws iam get-role --role-name AmazonBedrockExecutionRoleForKnowledgeBase_dyS2B --profile Master
```

---

## 📈 CloudWatch Metrics (Após ter acesso)

### Ver invocações do Bedrock (últimas 24h)
```bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/Bedrock \
  --metric-name Invocations \
  --start-time $(date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 3600 \
  --statistics Sum \
  --region us-east-1 \
  --profile Master
```

### Ver tokens de entrada consumidos
```bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/Bedrock \
  --metric-name InputTokenCount \
  --start-time $(date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 3600 \
  --statistics Sum \
  --region us-east-1 \
  --profile Master
```

---

## 🧪 Testar Acesso ao Bedrock (Após ter quotas)

### Invocar modelo Claude Haiku (exemplo)
```bash
aws bedrock-runtime invoke-model \
  --model-id anthropic.claude-3-haiku-20240307-v1:0 \
  --body '{"anthropic_version":"bedrock-2023-05-31","max_tokens":100,"messages":[{"role":"user","content":"Olá, você está funcionando?"}]}' \
  --region us-east-1 \
  --profile Master \
  output.json

cat output.json
```

### Invocar modelo Nova Micro (exemplo)
```bash
aws bedrock-runtime invoke-model \
  --model-id amazon.nova-micro-v1:0 \
  --body '{"messages":[{"role":"user","content":[{"text":"Olá, você está funcionando?"}]}],"inferenceConfig":{"max_new_tokens":100}}' \
  --region us-east-1 \
  --profile Master \
  output.json

cat output.json
```

---

## 🔄 Sincronizar Knowledge Base (Após ter quotas)

### Via CLI (se disponível)
```bash
# Verificar se existe comando para sync
aws bedrock-agent help | grep sync
```

### Via Console (Recomendado)
1. Acessar: https://console.aws.amazon.com/bedrock/
2. Knowledge Bases → PoliticasRH-KnowledgeBase
3. Clicar em "Sync"

---

## 🧹 Limpeza (Se necessário)

### Cancelar solicitação de quota pendente
```bash
# Primeiro, listar para pegar o RequestId
aws service-quotas list-requested-service-quota-change-history \
  --service-code bedrock \
  --region us-east-1 \
  --profile Master \
  --status PENDING

# Depois, cancelar (se necessário)
# Nota: Não há comando direto para cancelar, precisa fazer via console
```

---

## 📝 Salvar Outputs em Arquivos

### Salvar lista de quotas
```bash
aws service-quotas list-service-quotas \
  --service-code bedrock \
  --region us-east-1 \
  --profile Master \
  --output json > bedrock-quotas-$(date +%Y%m%d).json
```

### Salvar lista de modelos
```bash
aws bedrock list-foundation-models \
  --region us-east-1 \
  --profile Master \
  --output json > bedrock-models-$(date +%Y%m%d).json
```

### Salvar solicitações de quota
```bash
aws service-quotas list-requested-service-quota-change-history \
  --service-code bedrock \
  --region us-east-1 \
  --profile Master \
  --output json > bedrock-quota-requests-$(date +%Y%m%d).json
```

---

## 🎯 Comandos Recomendados para AGORA

### 1. Verificar se já tem alguma quota > 0
```bash
aws service-quotas list-service-quotas \
  --service-code bedrock \
  --region us-east-1 \
  --profile Master \
  --query "Quotas[?Value > \`0\`].[QuotaName,Value]" \
  --output table
```

### 2. Tentar solicitar aumento das quotas ajustáveis (Cross-Region)
```bash
# Claude Haiku
aws service-quotas request-service-quota-increase --service-code bedrock --quota-code L-DCADBC78 --desired-value 10000 --region us-east-1 --profile Master

# Nova Micro
aws service-quotas request-service-quota-increase --service-code bedrock --quota-code L-DC7FF66C --desired-value 10000 --region us-east-1 --profile Master

# Nova Lite
aws service-quotas request-service-quota-increase --service-code bedrock --quota-code L-C6F5908D --desired-value 10000 --region us-east-1 --profile Master
```

### 3. Verificar se as solicitações foram aceitas
```bash
aws service-quotas list-requested-service-quota-change-history \
  --service-code bedrock \
  --region us-east-1 \
  --profile Master \
  --status PENDING \
  --output table
```

---

## ⚠️ Notas Importantes

1. **Quotas Cross-Region vs On-Demand:**
   - Cross-Region: tokens por **minuto** (ajustáveis)
   - On-Demand: tokens por **dia** (NÃO ajustáveis)

2. **Solicitações podem ser negadas:**
   - AWS prioriza quem já está usando
   - Pedir valores realistas
   - Justificar caso de uso

3. **Tempo de aprovação:**
   - Quotas ajustáveis: minutos/horas
   - Quotas não ajustáveis: dias (via ticket)

4. **Após aprovação:**
   - Quotas são ativadas automaticamente
   - Não precisa reiniciar nada
   - Pode começar a usar imediatamente

---

**Última atualização:** 16/02/2026  
**Projeto:** POC Agente RH - Maestriacloud
