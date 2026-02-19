# 🤖 AI Agent Serverless Kit

> Solução serverless de Agente de IA para RH usando Amazon Bedrock, RAG e tecnologias AWS nativas.

[![AWS](https://img.shields.io/badge/AWS-Bedrock-orange)](https://aws.amazon.com/bedrock/)
[![Serverless](https://img.shields.io/badge/Architecture-Serverless-green)](https://aws.amazon.com/serverless/)
[![Cost](https://img.shields.io/badge/Cost-$2--12%2Fmonth-brightgreen)](ROADMAP.md)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## 🎯 Sobre o Projeto

Kit completo para criar Agentes de IA serverless com foco em:
- **💰 Baixo custo** (~$2-12/mês dependendo do uso)
- **⚡ 100% Serverless** (paga apenas pelo que usa)
- **🚀 Tecnologias atuais** (Amazon Bedrock, Nova Micro, RAG)
- **📦 Fácil replicação** para múltiplos clientes
- **📚 Documentação completa** para implementação rápida

**Status atual:** POC validada, pronta para produção

---

## ✨ Features

- ✅ Agent de IA com RAG (Retrieval-Augmented Generation)
- ✅ Knowledge Base integrada (documentos em S3)
- ✅ Embeddings com Amazon Titan v2.0
- ✅ Vector Database (S3 Vectors - mais barato)
- ✅ Respostas contextualizadas baseadas em documentos
- ✅ **Lambda Action Group** - Consulta de feriados brasileiros
- ✅ **Guardrail** - Filtro de conteúdo ofensivo
- ✅ **Lambda Layer** - Biblioteca holidays (Docker build)
- ✅ Monitoramento com CloudWatch
- ✅ Deploy em 15 minutos
- ✅ Documentação completa

---

## 🚀 Quick Start

### Pré-requisitos
- Conta AWS ativa
- AWS CLI configurado
- Quotas Bedrock habilitadas ([ver guia](Documentação/Bedrock/))

### Deploy em 3 passos

```bash
# 1. Clone o repositório
git clone git@github.com:bruno0nline/ai-agent-serverless-kit.git
cd ai-agent-serverless-kit

# 2. Configure suas variáveis
export BUCKET_NAME="sua-empresa-rag-kb"
export REGION="us-east-1"

# 3. Execute o deploy
# Ver guia completo: DEPLOYMENT.md
```

**Tempo total:** 15-30 minutos (após quotas aprovadas)

📖 **Guia completo:** [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 📁 Estrutura do Projeto

```
.
├── Documentação/
│   ├── Inteligência Artificial sem servidor na AWS.md  # Documentação principal
│   ├── Bedrock/                                        # Troubleshooting Bedrock
│   │   ├── RESUMO-EXECUTIVO.md                        # 🎯 Comece aqui!
│   │   ├── README.md                                  # Índice da pasta
│   │   ├── resolucao-throttling-quotas.md             # Guia completo
│   │   ├── ticket-aws-support-bedrock-quotas.md       # Template de ticket
│   │   └── quotas-ajustaveis-prioritarias.md          # Análise de quotas
│   ├── comandos-kiro.txt
│   ├── prompt-kiro.txt
│   └── Script Bruno.txt
│
├── PythonAwsBedrockActionGroupDemo/                   # Lambda Action Group
│   ├── lambda_function_bedrock.py                     # Handler para Bedrock
│   ├── lambda_function_regular.py                     # Handler standalone
│   ├── requirements.txt                               # Dependências Python
│   ├── Dockerfile                                     # Build do Layer
│   ├── create_zip.py                                  # Script auxiliar
│   ├── COMANDOS-WINDOWS.md                            # Guia Windows
│   ├── README.md                                      # Documentação
│   └── test/                                          # Eventos de teste
│       ├── lambda_function_bedrock/
│       └── lambda_function_regular/
│
├── Lambda/                                            # Outras Lambdas
│   ├── action-groups/
│   │   ├── verificar-status-servico/
│   │   ├── consultar-ticket/
│   │   └── criar-ticket/
│   ├── api/
│   │   └── invoke-agent/
│   ├── webhooks/
│   │   └── slack-integration/
│   ├── INTEGRATION-GUIDE.md
│   └── README.md
│
├── IA na AWS/
│   ├── Kiro/                                          # Workspace Kiro IDE
│   └── RAG-Knowledge-Base/                            # Documentos para RAG
│       ├── aws-well-architected.md
│       ├── aws-security-best-practices.md
│       ├── aws-compute-services.md
│       └── README.md
│
├── Scripts/                                            # Scripts Python AWS
│   ├── S3/
│   ├── EC2/
│   ├── IAM/
│   ├── RDS/
│   ├── CloudWatch/
│   └── Lambda/
│
├── Configurações/
│   ├── variavel-de-ambientes.txt
│   └── profile-sso.txt
│
├── Instaladores/
│   ├── kiro-ide-0.9.2-stable-win32-x64.exe
│   └── AWSToolkitPackage.v17.vsix
│
├── Screenshots/                                        # Evidências de erros
│
├── bedrock-quotas.json                                # Quotas do Bedrock
└── README.md                                          # Este arquivo
```

---

## 🎯 Status Atual do Projeto

### ✅ Concluído

- [x] Configuração do ambiente (WSL, AWS CLI, Python)
- [x] Estudos sobre Amazon Bedrock (Pricing, Guardrails, Automated Reasoning)
- [x] Estudos sobre RAG (Embeddings, Vector Databases, Knowledge Bases)
- [x] Criação de Knowledge Base (AWS-RAG-Knowledge-Base)
- [x] Estudos sobre Agentes de IA (Single vs Multi-Agent)
- [x] Criação de Single Agent (agent-rh-chatbot)
- [x] Criação de Knowledge Base de RH (PoliticasRH-KnowledgeBase)
- [x] Análise de quotas do Bedrock
- [x] Documentação completa de troubleshooting
- [x] Abrir ticket AWS Support para aumentar quotas ✅ **Concluído 16/02/2026**
- [x] Acesso ao Bedrock liberado ✅ **Concluído 19/02/2026**
- [x] Lambda Function para consulta de feriados (Action Group)
- [x] Lambda Layer com biblioteca holidays (Docker)
- [x] Integração Lambda + Bedrock Agent
- [x] Guardrail implementado (Filtro-de-Conteudo-Ofensivo)
- [x] Agent RH testado e funcionando

### 🟢 Próximos Passos

- [ ] Multi-Agent Collaboration (Módulo 62)
- [ ] Bedrock Flows (Módulo 63)
- [ ] Finalizar fundamentos do Bedrock

---

## 🚨 ~~Problema Atual: Throttling do Bedrock~~ ✅ RESOLVIDO

**Status:** ✅ **RESOLVIDO em 19/02/2026**

~~**Erro:** HTTP 429 - "Too many tokens per day"~~  
~~**Causa:** Quotas do Bedrock em 0.0 (sem acesso habilitado)~~  
~~**Solução:** Abrir ticket AWS Support~~

### ✅ Solução Implementada

Ticket AWS Support #624012998785 foi resolvido com sucesso. A equipe AWS liberou o acesso aos modelos do Bedrock.

**Resultado:**
- ✅ Acesso aos modelos Bedrock liberado
- ✅ Agent RH funcionando
- ✅ Lambda Action Group integrada
- ✅ Guardrail implementado

### 📖 Documentação Completa

**Comece aqui:** [`Documentação/Bedrock/RESUMO-EXECUTIVO.md`](Documentação/Bedrock/RESUMO-EXECUTIVO.md)

Este documento contém:
- Análise completa do problema
- Solução implementada
- Histórico do ticket AWS
- Links para toda documentação

---

## 🏗️ Arquitetura da Solução (POC)

```
┌─────────────┐
│   Usuário   │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────┐
│  AWS Bedrock Agent                  │
│  (agent-rh-chatbot)                 │
│                                     │
│  Model: Amazon Nova Micro 1.0       │
│  Guardrail: Filtro-de-Conteudo-     │
│             Ofensivo                │
└──────┬──────────────────┬───────────┘
       │                  │
       │                  ▼
       │         ┌─────────────────────┐
       │         │  Lambda Function    │
       │         │  (Consulta_Feriados)│
       │         │                     │
       │         │  Layer: holidays    │
       │         │  Runtime: Python 3.13│
       │         └─────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│  Knowledge Base                     │
│  (PoliticasRH-KnowledgeBase)        │
│                                     │
│  - Embedding: Titan v2.0            │
│  - Vector DB: S3 Vectors            │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│  S3 Bucket                          │
│  s3://maestriatec-rag-knowledge-    │
│  base/RH/                           │
│                                     │
│  - beneficios.md                    │
│  - codigo-conduta.md                │
│  - politica-ferias.md               │
└─────────────────────────────────────┘
```

---

## 🛠️ Tecnologias Utilizadas

### AWS Services
- **Amazon Bedrock** - Foundation Models (LLMs)
- **Amazon Bedrock Agents** - Agentes de IA
- **Amazon Bedrock Knowledge Bases** - RAG
- **Amazon S3** - Armazenamento de documentos
- **Amazon S3 Vectors** - Vector Database
- **AWS IAM** - Permissões e roles
- **AWS CloudWatch** - Monitoramento (futuro)

### Modelos de IA
- **Amazon Titan Text Embeddings v2.0** - Embeddings
- **Amazon Nova Micro 1.0** - Agent chatbot
- **Anthropic Claude 3 Haiku** - Alternativa (futuro)

### Ferramentas
- **AWS CLI** - Gerenciamento via linha de comando
- **Python 3 + Boto3** - Scripts de automação
- **WSL (Ubuntu 24.04)** - Ambiente Linux no Windows
- **Kiro IDE** - IDE para desenvolvimento

---

## 📚 Documentação

### Para Desenvolvedores
- **[ROADMAP.md](ROADMAP.md)** - Planejamento completo do projeto (POC → BS4IT → Comercial)
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Arquitetura técnica detalhada
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Guia de deploy passo a passo (15 min)
- **[TECH-STACK-2026.md](TECH-STACK-2026.md)** - Stack recomendada e comparações

### Para Troubleshooting
- **[Documentação/Bedrock/](Documentação/Bedrock/)** - Resolução de problemas de quotas
  - `RESUMO-EXECUTIVO.md` - Visão geral do problema
  - `CONCLUSAO-ANALISE.md` - Descoberta sobre quotas
  - `STATUS-TICKET.md` - Acompanhamento do ticket AWS
  - `comandos-prontos.md` - Comandos CLI prontos

### Para Aprendizado
- **[Documentação/Inteligência Artificial AWS Bedrock.md](Documentação/)** - Anotações do curso

---

## 🎯 Casos de Uso

### Atual: POC Maestriacloud
- Agente de RH para atendimento de funcionários
- 3 documentos base (benefícios, código de conduta, férias)
- Testes e validação de tecnologia

### Futuro: BS4IT (Empresa CLT)
- Implementação em ambiente corporativo real
- Integração com sistemas internos
- Métricas de ROI e satisfação

### Visão: Produto Comercial
- Solução replicável para múltiplos clientes
- Template customizável
- Modelo SaaS ou implementação dedicada

---

## 💰 Custos Estimados

| Fase | Uso Mensal | Custo |
|------|------------|-------|
| **POC** | 100 interações | ~$0.21/mês |
| **Produção Pequena** | 1.000 interações | ~$2.80/mês |
| **Produção Média** | 10.000 interações | ~$11.54/mês |

**ROI Esperado:** 4000-8000% (economia de 20h/mês de atendimento RH)

Ver detalhes em: [ROADMAP.md](ROADMAP.md#-modelo-de-custos)

---

## 🚀 Como Começar

### 1. Configurar Ambiente

```bash
# Instalar AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Configurar profile AWS
aws configure sso --profile Master

# Verificar acesso
aws s3 ls --profile Master
```

### 2. Instalar Python e Boto3

```bash
# Criar virtualenv
python3 -m venv ~/venv/ia
source ~/venv/ia/bin/activate

# Instalar dependências
pip install boto3 awscli
```

### 3. Resolver Problema de Quotas

Seguir instruções em: [`Documentação/Bedrock/RESUMO-EXECUTIVO.md`](Documentação/Bedrock/RESUMO-EXECUTIVO.md)

---

## 📞 Informações do Projeto

**Empresa:** Maestriacloud  
**Localização:** Minas Gerais, Brasil  
**Tipo:** POC (Proof of Concept)  
**Objetivo:** Agente de RH para atendimento de funcionários

**AWS Account:** 624012998785  
**Região Principal:** us-east-1 (US East - N. Virginia)  
**Profile AWS CLI:** Master

---

## 🔗 Links Úteis

### AWS Console
- [Bedrock Console](https://console.aws.amazon.com/bedrock/)
- [Service Quotas Console](https://console.aws.amazon.com/servicequotas/)
- [AWS Support](https://console.aws.amazon.com/support/)
- [S3 Console](https://s3.console.aws.amazon.com/s3/)

### Documentação AWS
- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Bedrock Agents Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
- [Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Service Quotas](https://docs.aws.amazon.com/servicequotas/)

### Recursos de Aprendizado
- [AWS Builder Content](https://builder.aws.com/)
- [Kiro IDE](https://app.kiro.dev/)

---

## 📝 Notas

- Este é um projeto de **estudo e POC**
- Foco em aprendizado de IA Generativa na AWS
- Implementação simplificada para testes
- Documentação detalhada de todo o processo

---

**Última atualização:** 19/02/2026  
**Versão:** 1.1 - Agent RH com Lambda Action Group e Guardrail funcionando
