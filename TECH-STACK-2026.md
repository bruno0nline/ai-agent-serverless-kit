# Stack Tecnológica Recomendada (2026)

## 🎯 Objetivo

Documentar as melhores tecnologias serverless e de baixo custo para implementar Agentes de IA em produção.

---

## 🏆 Stack Recomendada (Atualizada 2026)

### Foundation Models (LLMs)

| Modelo | Custo | Quando Usar | Prioridade |
|--------|-------|-------------|------------|
| **Amazon Nova Micro** | $0.001/1k tokens | Chatbots, Q&A, uso geral | ⭐⭐⭐ |
| Amazon Nova Lite | $0.0006/1k tokens | Tarefas simples, alto volume | ⭐⭐ |
| Anthropic Claude 3 Haiku | $0.25/1M tokens | Qualidade premium, raciocínio complexo | ⭐⭐ |
| Amazon Nova Pro | $0.008/1k tokens | Tarefas complexas, análise profunda | ⭐ |

**Recomendação:** Amazon Nova Micro para 90% dos casos de uso.

---

### Embedding Models

| Modelo | Custo | Dimensões | Quando Usar | Prioridade |
|--------|-------|-----------|-------------|------------|
| **Titan Text Embeddings v2.0** | $0.0001/1k tokens | 1024 | RAG, busca semântica | ⭐⭐⭐ |
| Cohere Embed V4 | $0.0001/1k tokens | Variável | Alternativa ao Titan | ⭐⭐ |
| Amazon Nova Embeddings | $0.0002/1k tokens | 2048 | Alta precisão | ⭐ |

**Recomendação:** Titan v2.0 pela integração nativa e custo.

---

### Vector Databases

| Solução | Custo | Quando Usar | Prioridade |
|---------|-------|-------------|------------|
| **Amazon S3 Vectors** | $0.02/GB/mês | POC, produção pequena/média | ⭐⭐⭐ |
| OpenSearch Serverless | $0.24/OCU/hora | Queries complexas, alta escala | ⭐⭐ |
| Pinecone | $70/mês (starter) | Multi-cloud, features avançadas | ⭐ |
| pgvector (Aurora) | $0.12/hora | Já usa PostgreSQL | ⭐ |

**Recomendação:** S3 Vectors para começar, migrar para OpenSearch se necessário.

**Quando migrar para OpenSearch:**
- Mais de 100k documentos
- Necessidade de busca híbrida (vetorial + keyword)
- Filtros complexos
- Latência < 100ms crítica

---

### Infraestrutura como Código

| Ferramenta | Quando Usar | Prioridade |
|------------|-------------|------------|
| **AWS CDK** | Projetos AWS-only, type-safe | ⭐⭐⭐ |
| Terraform | Multi-cloud, equipe experiente | ⭐⭐ |
| CloudFormation | Simplicidade, nativo AWS | ⭐ |
| Pulumi | Linguagens modernas (TS, Python) | ⭐ |

**Recomendação:** AWS CDK em TypeScript ou Python.

**Exemplo CDK:**
```typescript
import * as cdk from 'aws-cdk-lib';
import * as bedrock from 'aws-cdk-lib/aws-bedrock';
import * as s3 from 'aws-cdk-lib/aws-s3';

export class AgentStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string) {
    super(scope, id);

    // S3 Bucket para documentos
    const bucket = new s3.Bucket(this, 'KnowledgeBaseBucket', {
      versioned: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
    });

    // Knowledge Base
    const kb = new bedrock.CfnKnowledgeBase(this, 'RH-KB', {
      name: 'RH-KnowledgeBase',
      roleArn: role.roleArn,
      knowledgeBaseConfiguration: {
        type: 'VECTOR',
        vectorKnowledgeBaseConfiguration: {
          embeddingModelArn: 'arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v2:0'
        }
      },
      storageConfiguration: {
        type: 'S3',
        s3Configuration: {
          bucketArn: bucket.bucketArn
        }
      }
    });
  }
}
```

---

### Frontend (Opcional)

| Solução | Custo | Quando Usar | Prioridade |
|---------|-------|-------------|------------|
| **AWS Amplify + React** | $0.01/build + hosting | Interface web moderna | ⭐⭐⭐ |
| Slack/Teams Integration | Grátis | Usuários já usam | ⭐⭐⭐ |
| API Gateway + Lambda | $3.50/milhão | API pública | ⭐⭐ |
| Streamlit | Grátis (self-hosted) | Protótipos rápidos | ⭐ |

**Recomendação:** Começar com Slack/Teams, depois web se necessário.

---

### Autenticação

| Solução | Custo | Quando Usar | Prioridade |
|---------|-------|-------------|------------|
| **Amazon Cognito** | $0.0055/MAU | Nativo AWS, simples | ⭐⭐⭐ |
| Auth0 | $23/mês | Features avançadas | ⭐⭐ |
| Okta | Enterprise | SSO corporativo | ⭐ |

**Recomendação:** Cognito para começar.

---

### Monitoramento

| Solução | Custo | Quando Usar | Prioridade |
|---------|-------|-------------|------------|
| **CloudWatch** | $0.30/métrica | Nativo AWS, básico | ⭐⭐⭐ |
| CloudWatch + X-Ray | +$5/milhão traces | Debug detalhado | ⭐⭐ |
| Datadog | $15/host/mês | Observabilidade completa | ⭐ |
| Grafana Cloud | $49/mês | Dashboards avançados | ⭐ |

**Recomendação:** CloudWatch para começar, X-Ray para debug.

---

### CI/CD

| Solução | Custo | Quando Usar | Prioridade |
|---------|-------|-------------|------------|
| **GitHub Actions** | Grátis (2000 min/mês) | Código no GitHub | ⭐⭐⭐ |
| AWS CodePipeline | $1/pipeline/mês | All-in AWS | ⭐⭐ |
| GitLab CI | Grátis (400 min/mês) | Código no GitLab | ⭐⭐ |
| Jenkins | Grátis (self-hosted) | Controle total | ⭐ |

**Recomendação:** GitHub Actions.

**Exemplo workflow:**
```yaml
name: Deploy to AWS
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - run: cdk deploy --require-approval never
```

---

## 🆚 Comparações Importantes

### Nova Micro vs Claude 3 Haiku

| Aspecto | Nova Micro | Claude 3 Haiku |
|---------|------------|----------------|
| Custo | $0.001/1k | $0.25/1M ($0.00025/1k) |
| Qualidade | Boa | Excelente |
| Latência | ~1-2s | ~1-2s |
| Context Window | 128k tokens | 200k tokens |
| **Veredito** | Melhor custo-benefício | Melhor qualidade |

**Quando usar cada um:**
- **Nova Micro:** 90% dos casos (chatbot, Q&A, resumos)
- **Claude Haiku:** Raciocínio complexo, análise profunda, código

---

### S3 Vectors vs OpenSearch Serverless

| Aspecto | S3 Vectors | OpenSearch |
|---------|------------|------------|
| Custo (10GB) | $0.20/mês | $172/mês |
| Setup | Simples | Complexo |
| Latência | ~200-500ms | ~50-100ms |
| Queries | Vetorial apenas | Híbrida (vetorial + keyword) |
| Escala | Ilimitada | Auto-scale |
| **Veredito** | POC e pequeno/médio | Grande escala |

**Quando migrar:**
- Mais de 100k documentos
- Latência < 100ms crítica
- Necessidade de filtros complexos
- Orçamento > $200/mês

---

### CDK vs Terraform

| Aspecto | AWS CDK | Terraform |
|---------|---------|-----------|
| Linguagem | TypeScript, Python, Java | HCL |
| Type Safety | ✅ Sim | ❌ Não |
| Multi-cloud | ❌ AWS only | ✅ Sim |
| Comunidade | Crescendo | Madura |
| Curva aprendizado | Média | Média |
| **Veredito** | AWS-only projects | Multi-cloud |

---

## 💡 Melhores Práticas 2026

### 1. Sempre Serverless
```
✅ Lambda, Bedrock, S3, DynamoDB
❌ EC2, RDS (a menos que necessário)
```

### 2. Pay-per-use
```
✅ On-demand, auto-scaling
❌ Provisioned, always-on
```

### 3. Managed Services
```
✅ Bedrock, Cognito, CloudWatch
❌ Self-hosted LLMs, custom auth
```

### 4. Infrastructure as Code
```
✅ CDK, Terraform, CloudFormation
❌ Console manual, ClickOps
```

### 5. Monitoramento desde o início
```
✅ CloudWatch, alarmes, dashboards
❌ "Vamos adicionar depois"
```

### 6. Segurança by design
```
✅ IAM least privilege, encryption, VPC
❌ Permissões amplas, dados não criptografados
```

---

## 🚀 Stack Evolutiva

### Fase 1: POC (Atual)
```
Agent: Bedrock Agent
LLM: Nova Micro
Embeddings: Titan v2.0
Vector DB: S3 Vectors
Storage: S3
Monitoring: CloudWatch básico
```

### Fase 2: Produção Pequena
```
+ Frontend: Slack/Teams integration
+ Auth: Cognito
+ CI/CD: GitHub Actions
+ IaC: AWS CDK
+ Monitoring: CloudWatch + alarmes
```

### Fase 3: Produção Média
```
+ Frontend: React + Amplify
+ API: API Gateway + Lambda
+ Vector DB: OpenSearch Serverless (se necessário)
+ Monitoring: CloudWatch + X-Ray
+ Multi-region: Failover automático
```

### Fase 4: Enterprise
```
+ Multi-tenant: Isolamento por cliente
+ SSO: Okta/Azure AD
+ Compliance: CloudTrail, Config
+ Observability: Datadog/New Relic
+ Multi-Agent: Supervisor + especialistas
```

---

## 📊 Comparação de Custos (1000 interações/mês)

| Stack | Custo Mensal | Quando Usar |
|-------|--------------|-------------|
| **Mínimo** (S3 Vectors + Nova Micro) | $2.80 | POC, startup |
| **Recomendado** (+ CloudWatch + Cognito) | $8.50 | Produção pequena |
| **Avançado** (+ OpenSearch + X-Ray) | $180 | Produção média |
| **Enterprise** (+ Multi-region + Datadog) | $500+ | Grande escala |

---

## 🎓 Recursos de Aprendizado

### Documentação Oficial
- [AWS Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
- [Amazon Nova Models](https://aws.amazon.com/bedrock/nova/)
- [AWS CDK Guide](https://docs.aws.amazon.com/cdk/)
- [RAG Best Practices](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)

### Cursos Recomendados
- AWS Skill Builder: Bedrock Fundamentals
- Coursera: Generative AI with LLMs
- Udemy: AWS CDK Complete Guide

### Comunidades
- AWS Community Builders
- Reddit: r/aws, r/MachineLearning
- Discord: AWS Developers

---

## 🔄 Atualizações

Este documento será atualizado conforme:
- Novos modelos são lançados
- Preços mudam
- Melhores práticas evoluem
- Feedback da comunidade

**Última atualização:** 16/02/2026  
**Próxima revisão:** 16/05/2026 (trimestral)

---

**Contribuições:** Pull requests bem-vindos!  
**Dúvidas:** Abrir issue no GitHub
