# 🎯 Recursos AWS do Projeto

**Conta AWS:** 624012998738  
**Região:** us-east-1 (US East - N. Virginia)  
**Última atualização:** 26/02/2026

---

## 📊 Resumo Geral

| Serviço | Quantidade | Status |
|---------|------------|--------|
| **Bedrock Agents** | 3 | ✅ Ativos |
| **Bedrock Knowledge Bases** | 3 | ✅ Ativos |
| **Bedrock Guardrails** | 2 | ✅ Ativos |
| **Bedrock Flows** | 1 | ✅ Ativo |
| **Lambda Functions** | 2 | ✅ Ativas |
| **IAM Roles** | 11 | ✅ Ativas |
| **DynamoDB Tables** | 1 | ✅ Ativa |

---

## 🤖 Amazon Bedrock

### Agents (3)

#### 1. supervisor (IMQEKI4AKK)
- **Modelo:** Amazon Nova Pro 1.0
- **Descrição:** Supervisor agent que orquestra e delega tarefas entre agentes especializados (RH e Vendas)
- **Status:** PREPARED
- **Última atualização:** 20/02/2026
- **Função:** Identifica necessidade do cliente e direciona para agente apropriado

#### 2. especialista-rh (EUTPHYTJC5)
- **Modelo:** Amazon Nova Micro 1.0
- **Descrição:** Assistente de RH para políticas, benefícios, férias e procedimentos internos
- **Status:** PREPARED
- **Última atualização:** 20/02/2026
- **Guardrail:** Filtro-de-Contudo-Ofensivo (q8xq058iym07)
- **Knowledge Base:** PoliticasRH-KnowledgeBase (A8Q2SRNGS4)
- **Versão:** 1

#### 3. especialista-produtos (JJ1OX8CEOU)
- **Modelo:** Claude 3.5 Haiku v1
- **Descrição:** Especialista em vendas de cursos de tecnologia (IA, Cloud AWS, Data Science)
- **Status:** PREPARED
- **Última atualização:** 20/02/2026
- **Knowledge Base:** PoliticasCurso-Knowledge-Base (HZKFK7YCSY)
- **Versão:** 1

---

### Knowledge Bases (3)

#### 1. PoliticasRH-KnowledgeBase (A8Q2SRNGS4)
- **Descrição:** Políticas, benefícios, procedimentos internos e dúvidas trabalhistas
- **Status:** ACTIVE
- **Última atualização:** 13/02/2026
- **Documentos:**
  - beneficios.md
  - codigo-conduta.md
  - politica-ferias.md
- **Embedding:** Amazon Titan Text Embeddings v2.0
- **Vector Store:** Amazon S3 Vectors
- **Bucket:** maestriatec-rag-knowledge-base

#### 2. PoliticasCurso-Knowledge-Base (HZKFK7YCSY)
- **Descrição:** Dados e políticas de cursos da Maestriacloud
- **Status:** ACTIVE
- **Última atualização:** 20/02/2026
- **Documentos:**
  - catalogo-cursos-maestriacloud.md (13 cursos)
  - catalogo-cursos-academia-saber.md
- **Embedding:** Amazon Titan Text Embeddings v2.0
- **Vector Store:** Amazon S3 Vectors
- **Bucket:** maestriatec-rag-knowledge-base

#### 3. AWS-RAG-Knowledge-Base (DOSAKSMY9J)
- **Descrição:** Documentação técnica AWS (Well-Architected, Security, Compute)
- **Status:** ACTIVE
- **Última atualização:** 12/02/2026
- **Documentos:**
  - aws-well-architected.md
  - aws-security-best-practices.md
  - aws-compute-services.md
- **Embedding:** Amazon Titan Text Embeddings v2.0
- **Vector Store:** Amazon S3 Vectors
- **Bucket:** maestriatec-rag-knowledge-base

---

### Guardrails (2)

#### 1. Filtro-de-Contudo-Ofensivo (q8xq058iym07)
- **Descrição:** Filtra linguagem ofensiva e de ódio para garantir interações respeituosas
- **Status:** READY
- **Versão:** DRAFT
- **Criado:** 10/02/2026
- **Última atualização:** 19/02/2026
- **Usado por:** especialista-rh

#### 2. AWS-Security-Guardrail (za0f8g5chihq)
- **Descrição:** Valida configurações AWS usando raciocínio automatizado para conformidade
- **Status:** READY
- **Versão:** DRAFT
- **Criado:** 12/02/2026
- **Tipo:** Automated Reasoning (Raciocínio Automatizado)
- **Função:** Garantir conformidade com políticas de baseline de segurança

---

### Flows (1)

#### Flow-OrderStatusAssistant (MP05DEKERM)
- **Descrição:** Fluxo automatizado que consulta status de pedidos e gera respostas personalizadas
- **Status:** Prepared
- **Versão:** DRAFT
- **Criado:** 26/02/2026
- **Última atualização:** 26/02/2026
- **Componentes:**
  1. **Flow Input** - Recebe order_id do usuário
  2. **Lambda Function** - Consulta DynamoDB (Consulta_OrderStatus)
  3. **Prompt Node** - Formata resposta amigável (OrderStatusResponder)
  4. **Flow Output** - Retorna mensagem ao usuário
- **Integração:** Lambda + DynamoDB + Prompt Management

---

### Prompt Management

#### OrderStatusResponder
- **Descrição:** Gera respostas amigáveis para consultas de status de pedidos
- **Variável:** `{{status}}`
- **Modelo:** Amazon Nova Micro 1.0
- **Versão:** Draft
- **Exemplos de resposta:**
  - Processing: "Seu pedido está sendo processado..."
  - Shipped: "Ótimas notícias! Seu pedido foi enviado..."
  - Delivered: "Seu pedido foi entregue com sucesso..."
  - Cancelled: "Infelizmente, seu pedido foi cancelado..."

---

## ⚡ AWS Lambda

### Functions (2)

#### 1. Consulta_Feriados
- **ARN:** arn:aws:lambda:us-east-1:624012998738:function:Consulta_Feriados
- **Runtime:** Python 3.13
- **Handler:** lambda_function.lambda_handler
- **Timeout:** 15s
- **Memory:** 128 MB
- **Role:** Lambda_Bedrock_Consulta_Feriado
- **Layer:** Holidays (biblioteca Python)
- **Descrição:** Action Group para consulta de feriados brasileiros
- **Integração:** Bedrock Agent (especialista-rh)
- **Última atualização:** 19/02/2026

#### 2. Consulta_OrderStatus
- **ARN:** arn:aws:lambda:us-east-1:624012998738:function:Consulta_OrderStatus
- **Runtime:** Python 3.14
- **Handler:** lambda_function.lambda_handler
- **Timeout:** 3s
- **Memory:** 128 MB
- **Role:** Lambda_DynamoDB_QueryOrderStatus
- **Descrição:** Consulta status de pedidos no DynamoDB
- **Integração:** Bedrock Flow (Flow-OrderStatusAssistant)
- **Última atualização:** 26/02/2026
- **Tabela:** VeganSweetOrders

---

## 🔐 AWS IAM

### Roles do Projeto (11)

#### Bedrock Agents (5 roles)
1. **AmazonBedrockExecutionRoleForAgents_R7SBV6YVRW8** - especialista-rh
2. **AmazonBedrockExecutionRoleForAgents_STU9V6CWJ8L** - especialista-rh (v2)
3. **AmazonBedrockExecutionRoleForAgents_SJ9WQAUS64** - especialista-produtos
4. **AmazonBedrockExecutionRoleForAgents_2A2SYUDOMLC** - supervisor
5. **AmazonBedrockExecutionRoleForAgents_QHVLZ73DYCS** - supervisor (v2)

#### Bedrock Knowledge Bases (3 roles)
1. **AmazonBedrockExecutionRoleForKnowledgeBase** - AWS-RAG-Knowledge-Base
2. **AmazonBedrockExecutionRoleForKnowledgeBase_dy528** - PoliticasRH-KnowledgeBase
3. **AmazonBedrockExecutionRoleForKnowledgeBase_fbuq0** - PoliticasCurso-Knowledge-Base

#### Bedrock Flows (1 role)
1. **AmazonBedrockExecutionRoleForFlows_MRWR4X8TWKP** - Flow-OrderStatusAssistant

#### Lambda (2 roles)
1. **Lambda_Bedrock_Consulta_Feriado** - Consulta_Feriados
   - Permissões: CloudWatch Logs
   
2. **Lambda_DynamoDB_QueryOrderStatus** - Consulta_OrderStatus
   - Permissões: CloudWatch Logs + DynamoDB GetItem
   - Policy customizada: DynamoDB-GetAccess-Items

---

## 🗄️ Amazon DynamoDB

### Tables (1)

#### VeganSweetOrders
- **Região:** us-east-1
- **Partition Key:** order_id (String)
- **Itens:** 25 pedidos
- **Atributos:**
  - order_id (String)
  - customer_id (Number)
  - description (String)
  - order_date (String)
  - rating (Number)
  - status (String)
- **Status possíveis:** Processing, Shipped, Delivered, Cancelled
- **Uso:** Bedrock Flow OrderStatusAssistant

---

## 📦 Amazon S3

### Buckets

#### maestriatec-rag-knowledge-base
- **Região:** us-east-1
- **Uso:** Armazenamento de documentos para Knowledge Bases
- **Estrutura:**
  ```
  /kb-rh/
    - beneficios.md
    - codigo-conduta.md
    - politica-ferias.md
  /kb-cursos/
    - catalogo-cursos-maestriacloud.md
    - catalogo-cursos-academia-saber.md
  /kb-aws-security/
    - aws-well-architected.md
    - aws-security-best-practices.md
    - aws-compute-services.md
  ```
- **Vector Store:** Amazon S3 Vectors (embeddings)

---

## 🎓 Features Implementadas

### ✅ RAG (Retrieval-Augmented Generation)
- 3 Knowledge Bases ativas
- Embeddings com Amazon Titan v2.0
- Vector Database (S3 Vectors)
- Respostas contextualizadas baseadas em documentos

### ✅ Multi-Agent Collaboration
- 1 Supervisor Agent (Patrícia)
- 2 Collaborator Agents (Carla RH, Rafael Vendas)
- Orquestração inteligente de tarefas

### ✅ Guardrails
- Filtro de conteúdo ofensivo
- Raciocínio automatizado para segurança AWS
- Validação de conformidade

### ✅ Action Groups
- Lambda integrada ao Bedrock Agent
- Consulta de feriados brasileiros
- Lambda Layer com biblioteca holidays

### ✅ Bedrock Flows
- Fluxo automatizado de consulta de pedidos
- Integração Lambda + DynamoDB + Prompt
- Respostas personalizadas

### ✅ Prompt Management
- Versionamento de prompts
- Variáveis dinâmicas
- Templates reutilizáveis

### ✅ Automated Reasoning
- Guardrail com validação lógica
- Conformidade com políticas de segurança

---

## 💰 Custos Estimados

| Recurso | Uso Mensal | Custo Estimado |
|---------|------------|----------------|
| **Bedrock Agents** | 1.000 invocações | ~$2.00 |
| **Knowledge Bases** | 1.000 consultas | ~$0.50 |
| **Lambda** | 1.000 execuções | ~$0.20 |
| **DynamoDB** | On-demand | ~$0.10 |
| **S3** | 1 GB | ~$0.02 |
| **Total** | | **~$2.82/mês** |

---

## 📚 Documentação Relacionada

- [README.md](../README.md) - Visão geral do projeto
- [ARCHITECTURE.md](../ARCHITECTURE.md) - Arquitetura técnica
- [DEPLOYMENT.md](../DEPLOYMENT.md) - Guia de deploy
- [ROADMAP.md](../ROADMAP.md) - Planejamento e próximos passos
- [Documentação/agents-maestriacloud.md](../Documentação/agents-maestriacloud.md) - Multi-Agent detalhado

---

**Gerado automaticamente em:** 26/02/2026  
**Comando usado:** `aws bedrock list-agents`, `aws lambda list-functions`, `aws iam list-roles`
