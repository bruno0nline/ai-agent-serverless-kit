# Guia de Deploy - AI Agent Solution

## 🚀 Deploy Rápido (15 minutos)

Este guia mostra como replicar a solução em qualquer conta AWS.

---

## 📋 Pré-requisitos

- Conta AWS ativa
- AWS CLI configurado
- Permissões: Bedrock, S3, IAM
- Quotas Bedrock habilitadas (ver seção abaixo)

---

## 🔧 Passo 1: Habilitar Quotas Bedrock

**IMPORTANTE:** Novas contas AWS têm quotas Bedrock em 0.0 por padrão.

```bash
# Verificar quotas atuais
aws service-quotas list-service-quotas \
  --service-code bedrock \
  --region us-east-1 \
  --query "Quotas[?Value > \`0\`]"

# Se retornar vazio, abrir ticket AWS Support
```

**Como abrir ticket:**
1. Console: https://console.aws.amazon.com/support/
2. Tipo: "Service Limit Increase"
3. Serviço: "Amazon Bedrock"
4. Usar template: `Documentação/Bedrock/CONCLUSAO-ANALISE.md`

**Tempo:** 24-48h para aprovação

---

## 📦 Passo 2: Criar Bucket S3

```bash
# Definir variáveis
BUCKET_NAME="sua-empresa-rag-knowledge-base"
REGION="us-east-1"

# Criar bucket
aws s3 mb s3://$BUCKET_NAME --region $REGION

# Criar pasta RH
aws s3api put-object \
  --bucket $BUCKET_NAME \
  --key RH/
```

---

## 📄 Passo 3: Upload de Documentos

```bash
# Upload dos documentos de RH
aws s3 cp documentos/beneficios.md s3://$BUCKET_NAME/RH/
aws s3 cp documentos/codigo-conduta.md s3://$BUCKET_NAME/RH/
aws s3 cp documentos/politica-ferias.md s3://$BUCKET_NAME/RH/

# Verificar
aws s3 ls s3://$BUCKET_NAME/RH/ --recursive
```

**Formatos suportados:** .md, .txt, .pdf, .docx, .html

---

## 🧠 Passo 4: Criar Knowledge Base

### Via Console (Recomendado)

1. Acessar: https://console.aws.amazon.com/bedrock/
2. Knowledge Bases → Create Knowledge Base
3. Configurar:
   - Nome: `[SuaEmpresa]-RH-KnowledgeBase`
   - Fonte: Amazon S3
   - URI: `s3://sua-empresa-rag-knowledge-base/RH/`
   - Embedding: Titan Text Embeddings v2.0
   - Vector DB: Amazon S3 Vectors
   - Fragmentação: Padrão (300 tokens)
4. Criar e aguardar
5. Clicar em "Sync" para indexar documentos

### Via CLI (Avançado)

```bash
# Criar role IAM primeiro
aws iam create-role \
  --role-name BedrockKnowledgeBaseRole \
  --assume-role-policy-document file://trust-policy.json

# Criar Knowledge Base
aws bedrock-agent create-knowledge-base \
  --name "SuaEmpresa-RH-KnowledgeBase" \
  --role-arn "arn:aws:iam::ACCOUNT_ID:role/BedrockKnowledgeBaseRole" \
  --knowledge-base-configuration '{
    "type": "VECTOR",
    "vectorKnowledgeBaseConfiguration": {
      "embeddingModelArn": "arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v2:0"
    }
  }' \
  --storage-configuration '{
    "type": "S3",
    "s3Configuration": {
      "bucketArn": "arn:aws:s3:::sua-empresa-rag-knowledge-base"
    }
  }'
```

---

## 🤖 Passo 5: Criar Agent

### Via Console (Recomendado)

1. Bedrock → Agents → Create Agent
2. Configurar:
   - Nome: `agent-rh-[sua-empresa]`
   - Modelo: Amazon Nova Micro 1.0
   - Instruções: (ver abaixo)
3. Adicionar Knowledge Base criada no passo 4
4. Configurações avançadas:
   - User input: Enabled
   - Code interpreter: Disabled
   - Timeout: 600s
5. Criar e testar

**Instruções do Agent:**
```
Você é um assistente virtual de Recursos Humanos da [SUA EMPRESA].

Sua missão é:
- Responder dúvidas sobre políticas de RH, benefícios e processos
- Ser sempre cordial, profissional e empático
- Fornecer informações precisas sobre a empresa
- Quando não souber algo, orientar o funcionário a procurar o RH presencial
- Usar linguagem clara e acessível

Sempre baseie suas respostas nos documentos da base de conhecimento.
```

---

## ✅ Passo 6: Testar

### Teste 1: Via Console
1. Agent → Test
2. Perguntas sugeridas:
   - "Quantos dias de férias tenho direito?"
   - "Quais são os benefícios da empresa?"
   - "Como solicito uma licença médica?"

### Teste 2: Via CLI
```bash
aws bedrock-agent-runtime invoke-agent \
  --agent-id "AGENT_ID" \
  --agent-alias-id "TSTALIASID" \
  --session-id "test-session-1" \
  --input-text "Quantos dias de férias tenho direito?" \
  output.json

cat output.json
```

---

## 📊 Passo 7: Monitoramento (Opcional)

### CloudWatch Metrics

```bash
# Ver invocações do agent
aws cloudwatch get-metric-statistics \
  --namespace AWS/Bedrock \
  --metric-name Invocations \
  --dimensions Name=AgentId,Value=AGENT_ID \
  --start-time $(date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 3600 \
  --statistics Sum
```

### Alarmes

```bash
# Criar alarme de custo
aws cloudwatch put-metric-alarm \
  --alarm-name bedrock-high-cost \
  --alarm-description "Alert when Bedrock cost > $50" \
  --metric-name EstimatedCharges \
  --namespace AWS/Billing \
  --statistic Maximum \
  --period 86400 \
  --evaluation-periods 1 \
  --threshold 50 \
  --comparison-operator GreaterThanThreshold
```

---

## 🔒 Passo 8: Segurança

### IAM Policies

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeAgent",
        "bedrock:InvokeModel"
      ],
      "Resource": [
        "arn:aws:bedrock:*:*:agent/*",
        "arn:aws:bedrock:*::foundation-model/*"
      ]
    }
  ]
}
```

### S3 Bucket Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock.amazonaws.com"
      },
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::sua-empresa-rag-knowledge-base/*",
        "arn:aws:s3:::sua-empresa-rag-knowledge-base"
      ]
    }
  ]
}
```

---

## 💰 Estimativa de Custos

### POC (100 interações/mês)
- Agent: $0.05
- Nova Micro: $0.10
- Titan Embeddings: $0.01
- S3: $0.05
- **Total: ~$0.21/mês**

### Produção (1000 interações/mês)
- Agent: $0.50
- Nova Micro: $1.00
- Titan Embeddings: $0.10
- S3: $0.20
- CloudWatch: $1.00
- **Total: ~$2.80/mês**

---

## 🐛 Troubleshooting

### Erro: "Too many tokens per day"
**Causa:** Quotas Bedrock não habilitadas  
**Solução:** Abrir ticket AWS Support (Passo 1)

### Erro: "Knowledge Base sync failed"
**Causa:** Permissões IAM incorretas  
**Solução:** Verificar role da Knowledge Base tem acesso ao S3

### Agent não responde corretamente
**Causa:** Documentos não sincronizados  
**Solução:** Clicar em "Sync" na Knowledge Base

### Custo muito alto
**Causa:** Muitas invocações ou modelo errado  
**Solução:** Verificar CloudWatch metrics e considerar Nova Lite

---

## 📚 Próximos Passos

Após deploy básico:
1. [ ] Adicionar mais documentos
2. [ ] Refinar instruções do agent
3. [ ] Configurar monitoramento
4. [ ] Implementar frontend (opcional)
5. [ ] Integrar com Slack/Teams (opcional)

---

## 🆘 Suporte

- Documentação: `Documentação/Bedrock/`
- Issues: GitHub Issues
- Email: [seu-email]

---

**Tempo total de deploy:** 15-30 minutos (após quotas aprovadas)  
**Dificuldade:** Intermediária  
**Custo:** < $3/mês para produção pequena
