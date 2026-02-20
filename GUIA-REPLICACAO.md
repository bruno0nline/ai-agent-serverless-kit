# 📘 Guia Completo de Replicação - Multi-Agent AI Solution

**Objetivo:** Documentar TUDO necessário para recriar esta solução do zero em qualquer empresa.

**Última atualização:** 20/02/2026  
**Versão:** 1.0 - Multi-Agent Collaboration

---

## 📋 Índice

1. [Visão Geral da Solução](#visão-geral)
2. [Arquitetura Multi-Agent](#arquitetura)
3. [Pré-requisitos](#pré-requisitos)
4. [Passo a Passo Completo](#passo-a-passo)
5. [Configurações Detalhadas](#configurações)
6. [Troubleshooting](#troubleshooting)
7. [Custos](#custos)
8. [Checklist Final](#checklist)

---

## 🎯 Visão Geral da Solução {#visão-geral}

### O que é?

Sistema de atendimento automatizado usando IA Generativa com:
- **3 Agents:** 1 Supervisor + 2 Collaborators (RH e Vendas)
- **3 Knowledge Bases:** Documentos de RH, Cursos e AWS
- **RAG:** Respostas baseadas em documentos reais
- **100% Serverless:** Sem servidores para gerenciar
- **Baixo custo:** $0.23 a $20/mês dependendo do uso

### Casos de Uso

- ✅ Atendimento RH (políticas, benefícios, férias)
- ✅ Vendas de cursos (catálogo, preços, matrículas)
- ✅ Suporte técnico (documentação, troubleshooting)
- ✅ FAQ automatizado
- ✅ Onboarding de funcionários

---

## 🏗️ Arquitetura Multi-Agent {#arquitetura}

### Fluxo de Funcionamento

```
Usuário
  ↓
Supervisor Agent (Patrícia)
  ├─→ Identifica tipo de pergunta
  ├─→ Delega para agent especializado
  │
  ├─→ Collaborator RH (Carla)
  │     └─→ Knowledge Base RH
  │
  └─→ Collaborator Vendas (Rafael)
        └─→ Knowledge Base Cursos
```

### Componentes

| Componente | Quantidade | Função |
|------------|------------|--------|
| **Supervisor Agent** | 1 | Orquestra e delega tarefas |
| **Collaborator Agents** | 2+ | Executam tarefas especializadas |
| **Knowledge Bases** | 2-3 | Armazenam documentos |
| **S3 Bucket** | 1 | Armazena arquivos e vetores |
| **Lambda (opcional)** | 0-N | Action Groups customizados |
| **Guardrails (opcional)** | 0-N | Filtros de conteúdo |

---

## ✅ Pré-requisitos {#pré-requisitos}

### 1. Conta AWS

- Conta AWS ativa
- Acesso root ou IAM com permissões:
  - `bedrock:*`
  - `s3:*`
  - `iam:CreateRole`, `iam:AttachRolePolicy`
  - `lambda:*` (se usar Action Groups)

### 2. Quotas Bedrock

⚠️ **CRÍTICO:** Novas contas têm quotas em 0.0

**Verificar:**
```bash
aws service-quotas list-service-quotas \
  --service-code bedrock \
  --region us-east-1 \
  --query "Quotas[?contains(QuotaName, 'tokens per day')].[QuotaName,Value]" \
  --output table
```

**Se Value = 0.0:**
1. Abrir ticket AWS Support
2. Tipo: "Service Limit Increase"
3. Serviço: "Amazon Bedrock"
4. Justificativa: "POC de agente de IA para [sua empresa]"
5. Aguardar 24-48h

**Documentação:** `Documentação/Bedrock/RESUMO-EXECUTIVO.md`

### 3. Ferramentas

- AWS CLI instalado e configurado
- Python 3.8+ (para scripts de teste)
- Editor de texto (para documentos)

---

## 🚀 Passo a Passo Completo {#passo-a-passo}

### FASE 1: Preparação de Documentos

#### 1.1. Criar Documentos de RH

Criar 3 arquivos em formato Markdown:

**`beneficios.md`**
```markdown
# Benefícios da Empresa

## Vale Alimentação
- Valor: R$ 500/mês
- Cartão: Alelo

## Plano de Saúde
- Operadora: Unimed
- Cobertura: Nacional
- Dependentes: Até 4

## Vale Transporte
- Desconto: 6% do salário
- Fornecido conforme necessidade
```

**`codigo-conduta.md`**
```markdown
# Código de Conduta

## Valores
- Respeito
- Integridade
- Colaboração

## Comportamentos Esperados
- Pontualidade
- Profissionalismo
- Comunicação clara
```

**`politica-ferias.md`**
```markdown
# Política de Férias

## Direitos
- 30 dias corridos após 12 meses
- Pode dividir em até 3 períodos
- Mínimo de 14 dias corridos em um período

## Solicitação
- Avisar com 30 dias de antecedência
- Aprovar com gestor direto
```

#### 1.2. Criar Catálogo de Cursos (se aplicável)

**`catalogo-cursos.md`**
```markdown
# Catálogo de Cursos

## Data Science Bootcamp
- Duração: 12 semanas
- Preço: $4.999
- Modalidade: Online/Presencial

## Python para Iniciantes
- Duração: 8 semanas
- Preço: $599
- Modalidade: Online

## AWS Cloud Practitioner
- Duração: 6 semanas
- Preço: $899
- Preparação para certificação
```

---

### FASE 2: Infraestrutura AWS

#### 2.1. Criar Bucket S3

```bash
# Definir variáveis (AJUSTE PARA SUA EMPRESA)
export BUCKET_NAME="suaempresa-rag-kb"
export REGION="us-east-1"
export AWS_PROFILE="seu-profile"

# Criar bucket
aws s3 mb s3://$BUCKET_NAME \
  --region $REGION \
  --profile $AWS_PROFILE

# Criar estrutura de pastas
aws s3api put-object \
  --bucket $BUCKET_NAME \
  --key RH/ \
  --profile $AWS_PROFILE

aws s3api put-object \
  --bucket $BUCKET_NAME \
  --key Cursos/ \
  --profile $AWS_PROFILE
```

#### 2.2. Upload de Documentos

```bash
# Upload RH
aws s3 cp beneficios.md s3://$BUCKET_NAME/RH/ --profile $AWS_PROFILE
aws s3 cp codigo-conduta.md s3://$BUCKET_NAME/RH/ --profile $AWS_PROFILE
aws s3 cp politica-ferias.md s3://$BUCKET_NAME/RH/ --profile $AWS_PROFILE

# Upload Cursos
aws s3 cp catalogo-cursos.md s3://$BUCKET_NAME/Cursos/ --profile $AWS_PROFILE

# Verificar
aws s3 ls s3://$BUCKET_NAME/ --recursive --profile $AWS_PROFILE
```

---

### FASE 3: Knowledge Bases

#### 3.1. Criar Knowledge Base de RH

**Via Console AWS:**

1. Acessar: https://console.aws.amazon.com/bedrock/
2. Menu lateral: **Knowledge bases** → **Create knowledge base**

**Etapa 1 - Detalhes:**
- Nome: `[SuaEmpresa]-RH-KnowledgeBase`
- Descrição: "Políticas de RH, benefícios e procedimentos internos"
- Service role: **Create and use a new service role** (deixar automático)
- Tipo: **Base de conhecimento usa armazenamento vetorial**

**Etapa 2 - Fonte de Dados:**
- Nome da fonte: `RH-DataSource`
- Tipo: **Amazon S3**
- URI do S3: `s3://suaempresa-rag-kb/RH/`
- Estratégia de fragmentação: **Padrão** (300 tokens)
- Estratégia de análise: **Analisador padrão do Amazon Bedrock**

**Etapa 3 - Armazenamento:**
- Modelo de incorporações: **Titan Text Embeddings v2.0**
- Dimensões vetoriais: **1024**
- Armazenamento de vetores: **Amazon S3 Vectors**

**Etapa 4 - Revisar e criar**
- Clicar em **Create knowledge base**
- Aguardar status: **Available**
- Clicar em **Sync** para indexar documentos
- Aguardar sync completar (1-5 minutos)

#### 3.2. Criar Knowledge Base de Cursos

Repetir processo acima com:
- Nome: `[SuaEmpresa]-Cursos-KnowledgeBase`
- URI: `s3://suaempresa-rag-kb/Cursos/`

---

### FASE 4: Agents

#### 4.1. Criar Collaborator Agent RH (Carla)

**Via Console AWS:**

1. Bedrock → **Agents** → **Create Agent**

**Detalhes do Agent:**
- Nome: `especialista-rh`
- Descrição: "Assistente de RH que responde dúvidas sobre políticas, benefícios e procedimentos"
- Modelo: **Amazon Nova Micro 1.0** (mais barato)
- Multi-agent collaboration: **Disabled** (é um collaborator)
- User input: **Enabled**
- Code interpreter: **Disabled**
- Idle session timeout: **600 segundos**

**Instruções do Agent:**
```
Você é um assistente virtual de Recursos Humanos da [SUA EMPRESA], seu nome é Carla.

Sua missão é:
- Responder dúvidas sobre políticas de RH, benefícios e processos
- Ser sempre cordial, profissional e empática
- Fornecer informações precisas sobre a empresa
- Quando não souber algo, orientar o funcionário a procurar o RH presencial
- Usar linguagem clara e acessível

Sempre baseie suas respostas nos documentos da base de conhecimento.
```

**Adicionar Knowledge Base:**
- Clicar em **Add** na seção Knowledge bases
- Selecionar: `[SuaEmpresa]-RH-KnowledgeBase`
- Instrução: "Use essa base de conhecimento para responder perguntas sobre políticas de RH"

**Criar Alias:**
- Clicar em **Create Alias**
- Nome: `dev`
- Descrição: "Versão de desenvolvimento"

**Preparar Agent:**
- Clicar em **Prepare** (aguardar 1-2 minutos)
- Status deve ficar: **PREPARED**

#### 4.2. Criar Collaborator Agent Vendas (Rafael)

Repetir processo acima com:
- Nome: `especialista-produtos`
- Modelo: **Claude 3.5 Haiku v1** (melhor para conversação)
- Instruções: Adaptar para vendas de cursos
- Knowledge Base: `[SuaEmpresa]-Cursos-KnowledgeBase`

**Instruções do Agent:**
```
Você é um consultor de vendas especializado da [SUA EMPRESA], seu nome é Rafael.

Sua missão é ajudar clientes a encontrar o curso ideal para suas necessidades.

DIRETRIZES:
- Seja prestativo e detalhado ao explicar cursos, preços e formas de pagamento
- Sempre mencione modalidades disponíveis (presencial, online, híbrida)
- Destaque certificações e benefícios inclusos
- Seja proativo em sugerir cursos relacionados
- Se não tiver informação específica, oriente a contatar admissões

Seu objetivo é ajudar estudantes a encontrar o curso ideal.
```

#### 4.3. Criar Supervisor Agent (Patrícia)

**Detalhes do Agent:**
- Nome: `supervisor`
- Descrição: "Supervisor que orquestra e delega tarefas entre RH e Vendas"
- Modelo: **Amazon Nova Pro 1.0** (melhor para orquestração)
- Multi-agent collaboration: **Enabled** ⚠️ IMPORTANTE
- User input: **Enabled**

**Instruções do Agent:**
```
Você é o Supervisor Agent da [SUA EMPRESA], seu nome é Patrícia, responsável por orquestrar e delegar tarefas entre agentes especializados.

AGENTES COLABORADORES DISPONÍVEIS:
1. **Carla** - Especialista em Recursos Humanos
   - Políticas de RH, benefícios, férias, licenças
   - Código de conduta e procedimentos internos

2. **Rafael** - Especialista em Vendas de Cursos
   - Catálogo de cursos de tecnologia
   - Preços, pacotes promocionais e formas de pagamento

SUA FUNÇÃO:
- Analisar a solicitação do usuário e identificar qual agente é mais adequado
- Delegar a tarefa para o agente especializado apropriado
- Se envolver múltiplas áreas, coordenar entre os agentes
- Consolidar respostas quando necessário
- Fornecer experiência fluida ao usuário

REGRAS DE DELEGAÇÃO:
- Perguntas sobre RH, políticas, benefícios → Carla (especialista-rh)
- Perguntas sobre cursos, vendas, preços → Rafael (especialista-produtos)
- Perguntas gerais sobre a empresa → você pode responder diretamente
- Dúvidas ambíguas → pergunte ao usuário para clarificar

ESTILO:
- Seja cordial e profissional
- Apresente-se como Patrícia quando apropriado
- Explique brevemente para qual especialista está direcionando
- Mantenha o contexto da conversa
- Garanta que o usuário receba resposta completa

Seu objetivo é garantir que cada solicitação seja atendida pelo agente mais qualificado.
```

**Configurar Collaborators:**

1. Na seção **Multi-agent collaboration**, clicar em **Add collaborator**

**Collaborator 1 - Carla:**
- Collaborator agent: Selecionar `especialista-rh`
- Agent alias: `dev`
- Collaborator name: `Carla`
- Enable conversation history sharing: **Enabled** ✅
- Collaborator instruction:
```
Carla é a especialista em Recursos Humanos da [SUA EMPRESA]. 
Ela responde dúvidas sobre políticas de RH, benefícios, férias, 
licenças, código de conduta e procedimentos internos. Use Carla 
quando o usuário tiver perguntas relacionadas a questões trabalhistas, 
benefícios de funcionários ou políticas da empresa.
```

**Collaborator 2 - Rafael:**
- Collaborator agent: Selecionar `especialista-produtos`
- Agent alias: `dev`
- Collaborator name: `Rafael`
- Enable conversation history sharing: **Enabled** ✅
- Collaborator instruction:
```
Rafael é o consultor de vendas especializado em cursos de tecnologia 
da [SUA EMPRESA]. Ele fornece informações sobre catálogo de cursos, 
preços, pacotes promocionais, formas de pagamento e recomendações 
personalizadas. Use Rafael quando o usuário quiser saber sobre cursos, 
matrículas, valores ou certificações.
```

**Criar Alias e Preparar:**
- Criar alias `dev`
- Clicar em **Prepare**
- Aguardar status: **PREPARED**

---

### FASE 5: Testes

#### 5.1. Teste via Console

**Teste 1 - Delegação RH:**
```
Pergunta: "Quantos dias de férias tenho direito?"
Esperado: Patrícia delega para Carla → Resposta baseada em politica-ferias.md
```

**Teste 2 - Delegação Vendas:**
```
Pergunta: "Quais cursos de IA vocês oferecem?"
Esperado: Patrícia delega para Rafael → Resposta baseada em catalogo-cursos.md
```

**Teste 3 - Delegação Mista:**
```
Pergunta: "Funcionários têm desconto nos cursos?"
Esperado: Patrícia coordena Carla + Rafael → Resposta consolidada
```

#### 5.2. Teste via CLI (Opcional)

```bash
# Obter IDs dos agents
aws bedrock-agent list-agents --region us-east-1 --profile $AWS_PROFILE

# Invocar supervisor
aws bedrock-agent-runtime invoke-agent \
  --agent-id "SUPERVISOR_AGENT_ID" \
  --agent-alias-id "ALIAS_ID" \
  --session-id "test-$(date +%s)" \
  --input-text "Quantos dias de férias tenho direito?" \
  --region us-east-1 \
  --profile $AWS_PROFILE \
  output.json

# Ver resposta
cat output.json
```

---

## ⚙️ Configurações Detalhadas {#configurações}

### Modelos Recomendados

| Agent | Modelo | Custo | Quando Usar |
|-------|--------|-------|-------------|
| Supervisor | Nova Pro 1.0 | Médio | Orquestração complexa |
| Collaborators | Nova Micro 1.0 | Baixo | Tarefas simples |
| Collaborators | Claude Haiku | Médio | Conversação natural |

### Estratégias de Fragmentação

| Estratégia | Tamanho | Quando Usar |
|------------|---------|-------------|
| Padrão | 300 tokens | Documentos gerais (recomendado) |
| Tamanho fixo | Customizado | Controle preciso |
| Hierárquica | Variável | Documentos estruturados |
| Semântica | Variável | Manter contexto relacionado |

### Vector Databases

| Opção | Custo | Quando Usar |
|-------|-------|-------------|
| S3 Vectors | Mais barato | POC e produção pequena (recomendado) |
| OpenSearch Serverless | Médio | Queries complexas |
| Pinecone | Alto | Alta performance |

---

## 🐛 Troubleshooting {#troubleshooting}

### Problema: "Too many tokens per day"

**Causa:** Quotas Bedrock em 0.0  
**Solução:**
1. Verificar quotas: `aws service-quotas list-service-quotas --service-code bedrock`
2. Abrir ticket AWS Support
3. Aguardar 24-48h

**Documentação:** `Documentação/Bedrock/`

### Problema: Knowledge Base sync failed

**Causa:** Permissões IAM ou throttling  
**Solução:**
1. Verificar role da KB tem acesso ao S3
2. Aguardar 5 minutos e tentar novamente
3. Verificar se arquivos estão no S3

### Problema: Supervisor não delega corretamente

**Causa:** Instruções ambíguas ou collaborators não configurados  
**Solução:**
1. Revisar instruções do Supervisor
2. Verificar Collaborator instructions
3. Testar cada collaborator individualmente primeiro
4. Verificar se "conversation history sharing" está enabled

### Problema: Respostas genéricas (não usa KB)

**Causa:** KB não sincronizada ou não associada ao agent  
**Solução:**
1. Verificar status da KB: deve estar "ACTIVE"
2. Clicar em "Sync" na KB
3. Verificar se KB está adicionada ao agent
4. Testar pergunta específica do documento

---

## 💰 Custos {#custos}

### Estimativa por Fase

| Fase | Componentes | Custo Mensal |
|------|-------------|--------------|
| **POC** (100 interações) | 3 agents + 2 KBs + S3 | $0.23 |
| **Produção Pequena** (1K interações) | 3 agents + 2 KBs + S3 | $2.00 |
| **Produção Média** (10K interações) | 3 agents + 2 KBs + S3 + CloudWatch | $19.86 |

### Detalhamento

**Agents:**
- Supervisor (Nova Pro): $0.10 (POC) a $10.00 (10K)
- Collaborator RH (Nova Micro): $0.01 (POC) a $3.00 (10K)
- Collaborator Vendas (Claude Haiku): $0.08 (POC) a $6.00 (10K)

**Knowledge Bases:**
- Embeddings (Titan v2): < $0.01
- S3 Vectors: $0.02

**S3 Storage:** < $0.01

**Documentação completa:** `Documentação/CUSTOS.md`

---

## ✅ Checklist Final {#checklist}

### Antes de Começar
- [ ] Conta AWS ativa
- [ ] AWS CLI configurado
- [ ] Quotas Bedrock verificadas/aprovadas
- [ ] Documentos preparados (RH, Cursos, etc)

### Infraestrutura
- [ ] Bucket S3 criado
- [ ] Documentos uploaded para S3
- [ ] Estrutura de pastas criada (/RH/, /Cursos/)

### Knowledge Bases
- [ ] KB de RH criada e sincronizada
- [ ] KB de Cursos criada e sincronizada
- [ ] Status: ACTIVE em ambas

### Agents
- [ ] Collaborator RH criado e preparado
- [ ] Collaborator Vendas criado e preparado
- [ ] Supervisor criado com collaborators configurados
- [ ] Aliases criados para todos
- [ ] Status: PREPARED em todos

### Testes
- [ ] Teste de delegação RH funcionando
- [ ] Teste de delegação Vendas funcionando
- [ ] Teste de delegação mista funcionando
- [ ] Respostas baseadas em documentos (não genéricas)

### Monitoramento (Opcional)
- [ ] CloudWatch Logs habilitado
- [ ] Alarme de custo configurado
- [ ] Scripts de monitoramento instalados

### Documentação
- [ ] IDs dos agents documentados
- [ ] IDs das KBs documentados
- [ ] Instruções customizadas salvas
- [ ] Backup de configuração feito

---

## 📚 Arquivos de Referência

| Arquivo | Conteúdo |
|---------|----------|
| `README.md` | Visão geral do projeto |
| `DEPLOYMENT.md` | Guia de deploy simplificado |
| `ARCHITECTURE.md` | Arquitetura técnica |
| `Documentação/agents-maestriacloud.md` | Configuração detalhada dos agents |
| `Documentação/CUSTOS.md` | Análise completa de custos |
| `Documentação/Bedrock/` | Troubleshooting de quotas |
| `tests/` | Scripts de teste e monitoramento |

---

## 🎯 Próximos Passos

Após implementação básica:

1. **Adicionar Action Groups (Lambda)**
   - Consultar sistemas externos
   - Criar tickets automaticamente
   - Integrar com APIs

2. **Implementar Guardrails**
   - Filtrar conteúdo ofensivo
   - Validar respostas
   - Compliance e segurança

3. **Integrar com Frontend**
   - Slack
   - Microsoft Teams
   - WhatsApp
   - Website próprio

4. **Otimizar Custos**
   - Cache de respostas frequentes
   - Ajustar modelos por uso
   - Monitoramento contínuo

5. **Escalar para Produção**
   - Múltiplos ambientes (dev, staging, prod)
   - CI/CD pipeline
   - Backup automatizado

---

## 📞 Suporte

**Dúvidas sobre este guia:**
- Revisar `README.md` e `DEPLOYMENT.md`
- Consultar `Documentação/Bedrock/` para problemas de quotas
- Executar scripts em `tests/` para diagnóstico

**Problemas com AWS:**
- AWS Support: https://console.aws.amazon.com/support/
- Documentação Bedrock: https://docs.aws.amazon.com/bedrock/

---

**Tempo estimado de implementação:** 2-4 horas (após quotas aprovadas)  
**Dificuldade:** Intermediária  
**Custo inicial:** < $1 para testes

**Última atualização:** 20/02/2026  
**Autor:** Bruno Mendes Augusto  
**Empresa:** Maestriacloud
