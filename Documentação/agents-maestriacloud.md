# 🤖 Documentação dos Agents - Maestriacloud

**Projeto:** AI Agent Serverless Kit - Maestriacloud  
**Data de criação:** Fevereiro 2026  
**Versão:** 1.0  

---

## 📊 Visão Geral

Este documento contém todas as configurações, instruções e detalhes dos agents criados no AWS Bedrock para a Maestriacloud. Use este documento como referência para recriar ou replicar os agents em outros ambientes.

---

## 🎯 Arquitetura Multi-Agent

```
                    ┌─────────────────────┐
                    │   Patrícia          │
                    │   (Supervisor)      │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
        ┌───────▼────────┐           ┌───────▼────────┐
        │   Carla        │           │   Rafael       │
        │   (RH)         │           │   (Vendas)     │
        └────────────────┘           └────────────────┘
```

---

## 1️⃣ Agent Supervisor - Patrícia

### Informações Básicas

| Campo | Valor |
|-------|-------|
| **Agent Name** | `supervisor` |
| **Agent ID** | (gerado automaticamente) |
| **Nome Humanizado** | Patrícia |
| **Modelo** | Amazon Nova Pro 1.0 (On-demand) |
| **Multi-agent collaboration** | ✅ Enabled |
| **User Input** | ✅ Enabled |
| **Idle session timeout** | 600 segundos (10 minutos) |

### Descrição

```
Supervisor agent que orquestra e delega tarefas entre agentes especializados (RH e Vendas) da Maestriacloud. Identifica a necessidade do cliente e direciona para o agente colaborador apropriado.
```

### Instruções para o Agent

```
Você é o Supervisor Agent da Maestriacloud, seu nome é Patrícia, responsável por orquestrar e delegar tarefas entre agentes especializados.

AGENTES COLABORADORES DISPONÍVEIS:
1. **Carla** - Especialista em Recursos Humanos
   - Políticas de RH, benefícios, férias, licenças
   - Código de conduta e procedimentos internos
   - Dúvidas de funcionários

2. **Rafael** - Especialista em Vendas de Cursos
   - Catálogo de cursos de tecnologia
   - Preços, pacotes promocionais e formas de pagamento
   - Recomendações de cursos baseadas no perfil do cliente

SUA FUNÇÃO:
- Analisar a solicitação do usuário e identificar qual agente colaborador é mais adequado
- Delegar a tarefa para o agente especializado apropriado
- Se a solicitação envolver múltiplas áreas, coordenar entre os agentes
- Consolidar respostas de múltiplos agentes quando necessário
- Fornecer uma experiência fluida e integrada ao usuário

REGRAS DE DELEGAÇÃO:
- Perguntas sobre RH, políticas internas, benefícios → Carla (especialista-rh)
- Perguntas sobre cursos, vendas, preços, matrículas → Rafael (especialista-produtos)
- Perguntas gerais sobre a empresa → você pode responder diretamente
- Dúvidas ambíguas → pergunte ao usuário para clarificar antes de delegar

ESTILO:
- Seja cordial e profissional
- Apresente-se como Patrícia quando apropriado
- Explique brevemente para qual especialista está direcionando (quando relevante)
- Mantenha o contexto da conversa ao delegar tarefas
- Garanta que o usuário receba uma resposta completa e satisfatória

Seu objetivo é garantir que cada solicitação seja atendida pelo agente mais qualificado, proporcionando uma experiência eficiente e profissional.
```

### Collaborators Configuration

#### Collaborator 1: Carla (especialista-rh)

| Campo | Valor |
|-------|-------|
| **Collaborator agent** | `especialista-rh` |
| **Agent alias** | `dev` |
| **Collaborator name** | `Carla` |
| **Enable conversation history sharing** | ✅ Enabled (recomendado) |

**Collaborator instruction:**
```
Carla é a especialista em Recursos Humanos da Maestriacloud. Ela responde dúvidas sobre políticas de RH, benefícios, férias, licenças, código de conduta e procedimentos internos. Use Carla quando o usuário tiver perguntas relacionadas a questões trabalhistas, benefícios de funcionários ou políticas da empresa.
```

#### Collaborator 2: Rafael (especialista-produtos)

| Campo | Valor |
|-------|-------|
| **Collaborator agent** | `especialista-produtos` |
| **Agent alias** | `dev` |
| **Collaborator name** | `Rafael` |
| **Enable conversation history sharing** | ✅ Enabled (recomendado) |

**Collaborator instruction:**
```
Rafael é o consultor de vendas especializado em cursos de tecnologia da Maestriacloud. Ele fornece informações sobre catálogo de cursos, preços, pacotes promocionais, formas de pagamento e recomendações personalizadas. Use Rafael quando o usuário quiser saber sobre cursos, matrículas, valores ou certificações.
```

### Collaboration Configuration

- **Tipo:** Supervisor
- **Descrição:** This supervisor agent will coordinate a final response from the agent.

---

## 2️⃣ Agent RH - Carla

### Informações Básicas

| Campo | Valor |
|-------|-------|
| **Agent Name** | `especialista-rh` |
| **Agent ID** | `EUTPHYTJC5` |
| **Nome Humanizado** | Carla |
| **Modelo** | Amazon Nova Micro 1.0 (On-demand) |
| **Multi-agent collaboration** | ❌ Disabled (é um collaborator) |
| **User Input** | ✅ Enabled |
| **Idle session timeout** | 600 segundos (10 minutos) |
| **Alias** | `dev` (ID: G8BSGM44RH) |

### Descrição

```
Assistente de RH que responde dúvidas sobre políticas, benefícios, férias, licenças e procedimentos internos da empresa de forma rápida, precisa e baseada em documentos oficiais de RH.
```

### Instruções para o Agent

```
Você é um assistente virtual de Recursos Humanos da Maestriacloud, seu nome é Carla, empresa de tecnologia em Minas Gerais.

Sua missão é:
- Responder dúvidas sobre políticas de RH, benefícios e processos
- Ser sempre cordial, profissional e empática
- Fornecer informações precisas sobre a empresa
- Quando não souber algo, orientar o funcionário a procurar o RH presencial
- Usar linguagem clara e acessível

Sempre baseie suas respostas nos documentos da base de conhecimento.
```

### Knowledge Base

| Campo | Valor |
|-------|-------|
| **Knowledge Base Name** | `PoliticasRH-KnowledgeBase` |
| **Knowledge Base ID** | `A4Q25RNG54` |
| **Data Source** | S3: `s3://maestriatec-rag-knowledge-base/RH/` |
| **Embedding Model** | Amazon Titan Text Embeddings v2.0 |
| **Vector Database** | Amazon S3 Vectors |
| **Chunking Strategy** | Default (300 tokens) |

**Knowledge Base instruction for Agent:**
```
Use essa base de conhecimento para responder perguntas sobre políticas de RH da Maestriacloud.
```

### Documentos na Knowledge Base

- `beneficios.md` - Informações sobre benefícios oferecidos
- `codigo-conduta.md` - Código de conduta da empresa
- `politica-ferias.md` - Políticas de férias e licenças

---

## 3️⃣ Agent Vendas - Rafael

### Informações Básicas

| Campo | Valor |
|-------|-------|
| **Agent Name** | `especialista-produtos` |
| **Agent ID** | (gerado automaticamente) |
| **Nome Humanizado** | Rafael |
| **Modelo** | Claude 3.5 Haiku v1 (On-demand) |
| **Multi-agent collaboration** | ❌ Disabled (é um collaborator) |
| **User Input** | ✅ Enabled |
| **Idle session timeout** | 600 segundos (10 minutos) |
| **Alias** | `dev` (ID: FNLYMRPFQA) |

### Descrição

```
Especialista em vendas de cursos de tecnologia. Fornece informações sobre catálogo de cursos, preços, pacotes promocionais, modalidades de pagamento e benefícios. Foco em IA, Cloud AWS e Data Science.
```

### Instruções para o Agent

```
Você é um consultor de vendas especializado da Maestriacloud, seu nome é Rafael, empresa de tecnologia em Minas Gerais. Sua missão é ajudar clientes a encontrar o curso ideal para suas necessidades e objetivos de carreira.

DIRETRIZES DE ATENDIMENTO:
- Seja prestativo e detalhado ao explicar cursos, preços, pacotes e formas de pagamento
- Sempre mencione modalidades disponíveis (presencial, online, híbrida) quando relevante
- Destaque certificações e benefícios inclusos nos cursos
- Seja proativo em sugerir cursos relacionados quando apropriado
- Se um detalhe específico do curso não estiver em sua base de conhecimento, diga: "Não tenho essa informação específica disponível. Entre em contato com nossa equipe de admissões para mais detalhes."

ESPECIALIZAÇÃO EM:
- Data Science, Machine Learning e IA Generativa
- Cloud Computing (AWS, certificações)
- Desenvolvimento Full Stack e Mobile
- Python, JavaScript e linguagens modernas

ABORDAGEM COMERCIAL:
- Identifique o nível de experiência do cliente (iniciante, intermediário, avançado)
- Pergunte sobre objetivos de carreira para recomendar o melhor curso
- Apresente pacotes promocionais quando houver economia significativa
- Explique opções de pagamento (à vista com desconto, parcelado, financiamento)
- Destaque o ROI e benefícios de longo prazo dos cursos

Seu objetivo é ajudar estudantes em potencial a encontrar o curso ideal para suas necessidades e fornecer informações precisas para apoiar sua jornada educacional.
```

### Knowledge Base

| Campo | Valor |
|-------|-------|
| **Knowledge Base Name** | `PoliticasCurso-Knowledge-Base` |
| **Knowledge Base ID** | (gerado automaticamente) |
| **Data Source** | S3: `s3://maestriatec-rag-knowledge-base/Cursos/` |
| **Embedding Model** | Amazon Titan Text Embeddings v2.0 |
| **Vector Database** | Amazon S3 Vectors |
| **Chunking Strategy** | Default (300 tokens) |

**Knowledge Base instruction for Agent:**
```
Use essa base de conhecimento para responder perguntas sobre os cursos da Maestriacloud.
```

### Documentos na Knowledge Base

- `catalogo-cursos-maestriacloud.md` - Catálogo completo de cursos de tecnologia

---

## 📞 Informações de Contato (Maestriacloud)

| Campo | Valor |
|-------|-------|
| **Site** | www.maestriacloud.com.br |
| **Email** | contato@maestriacloud.com.br |
| **WhatsApp** | (31) 98765-4321 |
| **Telefone** | (31) 3456-7890 |
| **Localização** | Minas Gerais, Brasil |
| **Horário de atendimento** | Segunda a sexta, 9h às 18h |

---

## 🔄 Fluxo de Interação

### Exemplo 1: Pergunta sobre RH

```
Usuário: "Quantos dias de férias tenho direito?"
    ↓
Patrícia (Supervisor): Identifica que é pergunta de RH
    ↓
Delega para → Carla (especialista-rh)
    ↓
Carla: Consulta Knowledge Base de RH e responde
    ↓
Patrícia: Retorna resposta consolidada ao usuário
```

### Exemplo 2: Pergunta sobre Cursos

```
Usuário: "Quais cursos de IA vocês oferecem?"
    ↓
Patrícia (Supervisor): Identifica que é pergunta de vendas
    ↓
Delega para → Rafael (especialista-produtos)
    ↓
Rafael: Consulta Knowledge Base de Cursos e responde
    ↓
Patrícia: Retorna resposta consolidada ao usuário
```

### Exemplo 3: Pergunta Mista

```
Usuário: "Funcionários têm desconto nos cursos?"
    ↓
Patrícia (Supervisor): Identifica que envolve RH + Vendas
    ↓
Delega para → Carla (RH) + Rafael (Vendas)
    ↓
Carla + Rafael: Consultam suas respectivas bases
    ↓
Patrícia: Consolida respostas e retorna ao usuário
```

---

## 🚀 Comandos AWS CLI para Deploy

### Listar Agents

```bash
aws bedrock-agent list-agents --region us-east-1 --profile Master
```

### Listar Knowledge Bases

```bash
aws bedrock-agent list-knowledge-bases --region us-east-1 --profile Master
```

### Upload de documentos para S3

```bash
# RH
aws s3 cp RAG-Knowledge-Base/RH/ s3://maestriatec-rag-knowledge-base/RH/ --recursive --profile Master

# Cursos
aws s3 cp RAG-Knowledge-Base/KB-Cursos/catalogo-cursos-maestriacloud.md s3://maestriatec-rag-knowledge-base/Cursos/ --profile Master
```

### Sincronizar Knowledge Base

```bash
# Via Console AWS Bedrock > Knowledge Bases > [Nome da KB] > Sync
```

---

## 📊 Custos Estimados

### POC (Uso Atual)

| Componente | Custo Mensal Estimado |
|------------|----------------------|
| Amazon Nova Micro (Supervisor) | ~$0.50 |
| Amazon Nova Micro (RH) | ~$0.30 |
| Claude 3.5 Haiku (Vendas) | ~$0.80 |
| S3 Vectors (2 KBs) | ~$0.20 |
| S3 Storage | ~$0.10 |
| **Total** | **~$1.90/mês** |

### Produção (1.000 interações/mês)

| Componente | Custo Mensal Estimado |
|------------|----------------------|
| Agents (3x) | ~$3.50 |
| Knowledge Bases | ~$0.80 |
| S3 | ~$0.20 |
| **Total** | **~$4.50/mês** |

---

## 🔐 Permissões IAM Necessárias

### Service Role para Agents

```
AmazonBedrockExecutionRoleForAgents_*
```

**Permissões:**
- `bedrock:InvokeModel`
- `bedrock:InvokeAgent`
- `s3:GetObject`
- `s3:ListBucket`

### Service Role para Knowledge Bases

```
AmazonBedrockExecutionRoleForKnowledgeBase_*
```

**Permissões:**
- `bedrock:InvokeModel` (para embeddings)
- `s3:GetObject`
- `s3:ListBucket`
- `aoss:APIAccessAll` (se usar OpenSearch)

---

## 📝 Notas de Implementação

### Boas Práticas

1. **Sempre criar Alias** para agents em produção
2. **Habilitar conversation history sharing** entre supervisor e collaborators
3. **Usar modelos apropriados:**
   - Supervisor: Modelo mais robusto (Nova Pro, Claude Sonnet)
   - Collaborators: Modelos mais leves (Nova Micro, Claude Haiku)
4. **Documentar todas as instruções** para facilitar manutenção
5. **Testar fluxos complexos** antes de colocar em produção

### Troubleshooting Comum

**Problema:** Agent não encontra informações na Knowledge Base
- **Solução:** Verificar se a KB foi sincronizada após upload dos documentos

**Problema:** Supervisor não delega corretamente
- **Solução:** Revisar as instruções de delegação e os Collaborator instructions

**Problema:** Erro de throttling (HTTP 429)
- **Solução:** Verificar quotas do Bedrock via Service Quotas

---

## 📚 Referências

- [AWS Bedrock Agents Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
- [Multi-Agent Collaboration Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent.html)
- [Knowledge Bases Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)

---

**Última atualização:** 20 de Fevereiro de 2026  
**Versão do documento:** 1.0  
**Autor:** Bruno Mendes Augusto  
**Empresa:** Maestriacloud
