# Inteligência Artificial sem servidor na AWS

## Instalação do WSL no Windows

```bash
wsl --install
wsl --update
wsl --list --online
wsl --install Ubuntu-24.04
wsl --install Ubuntu-24.04 --name IA

wsl --list --verbose
wsl -d Ubuntu-24.04 -u root
ls /home
cat /etc/passwd | grep /home
passwd seu_usuario
123456
exit
wsl -d Ubuntu-24.04
```

**Recomendado:** Reiniciar o SO após a instalação

### Abrir o terminal

```bash
wsl --list
wsl -d Ubuntu-24.04
exit
```

## Windows: Dependências WSL

### Atualizar o sistema

```bash
sudo apt update -y && sudo apt upgrade -y
```

### Instalar pacotes básicos (git, zsh, Python, utilitários)

```bash
sudo apt install -y git zsh curl wget unzip build-essential ca-certificates openssh-client python3 python3-venv python3-pip python3-boto3 python3-notebook
```

### Configurar Git e gerar chave SSH

```bash
git config --global user.name "Bruno Mendes Augusto"
git config --global user.email "brunomendesaugusto@gmail.com"
git config --global init.defaultBranch Main
```

Gerar chave (substitua o e-mail):

```bash
mkdir -p ~/.ssh
cd ~/.ssh
ssh-keygen -t rsa -C "brunomendesaugusto@gmail.com" -f ~/.ssh/GitHubKey -N ""
cat ~/.ssh/GitHubKey.pub   # copie e cole no GitHub/GitLab
vi ~/.ssh/config
```

Configuração SSH:

```
Host github.com
        PreferredAuthentications publickey
        Identityfile /home/bruno/.ssh/GitHubKey
```

Testar conexão:

```bash
ssh -T git@github.com
```

### Instalar Oh My Zsh e definir zsh como shell padrão

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Definir zsh como padrão (pode pedir senha):

```bash
sudo chsh -s "$(which zsh)" $USER
```

Se chsh não funcionar, reinicie o WSL/PC e abra novamente.

```bash
nano ~/.zshrc
source ~/.zshrc

omz pluin list
omz pluin enable aws
```

## AWS CLI (recomendado instalar v2 via instalador oficial)

```bash
uname -m
```

Baixar e instalar:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Verificar:

```bash
aws --version

aws s3 ls --profile Prod
aws s3 ls --profile Dev

aws sso login --sso-session Maestriacloud

asp Master
```

### Usar o arquivo do Windows como login no SSO

```bash
ln -s /mnt/c/Users/bma/.aws ~/.aws
```

## How to Install Amazon Q CLI on Windows

<https://builder.aws.com/content/2ySpxVfiIsy46THpP6YdlYgQZpD/how-to-install-amazon-q-cli-on-windows>

## How to Install Kiro CLI on Linux

```bash
curl -fsSL https://cli.kiro.dev/install | bash
```

<https://app.kiro.dev/account/usage>

## Criar virtualenv Python e instalar boto3

```bash
python3 -m venv ~/venv/ia
source ~/venv/ia/bin/activate
pip install --upgrade pip
pip install boto3
```

Opcional: instalar utilitários úteis:

```bash
pip install awscli-local pre-commit
```

## Testes rápidos

```bash
git --version
zsh --version
python3 --version
pip --version
aws --version
```

Testar boto3:

```bash
python -c "import boto3; print('boto3', boto3.__version__)"
```

## Amazon Bedrock

Agora estamos estudando o Amazon Bedrock.

### Preços

Diferenças de modelos, prompts diferentes para a mesma resposta, single prompt e chat.

### Registro em log de invocação de modelos

Habilitar o Registro em log de invocação de modelos e enviar para o CloudWatch.

### Criação de um modelo de prompt e versionamento

Exemplo usando a documentação abaixo:

<https://builder.aws.com/content/321xnRrCd7ZPRefMbMmIhD6QprR/aws-prompt-manager-tutorial-completo-com-exemplo-pratico-de-sistema-de-agendamento>

### Modelos e Guardrails

Modelos de geração de texto e vídeo, habilitar o debug de erros no Bedrock, barreiras de proteção Guardrails.

## Raciocínio Automatizado (Automated Reasoning)

Estudando raciocínio automatizado para reduzir alucinação de modelos.

### Hallucination is Inevitable: An Innate Limitation of Large Language Models

<https://arxiv.org/abs/2401.11817>

### Policy de Raciocínio Automatizado

Criada a policy `aws-security-baseline-policy` com as seguintes validações:

- **EC2**: IMDSv2 obrigatório
- **S3**: Criptografia habilitada
- **RDS**: Backup automático ativado
- **Security Groups**: Portas 22 e 3389 não podem estar abertas para 0.0.0.0/0

### Testes da Policy

Criados testes manuais válidos e inválidos:

**Exemplos de testes válidos:**
- "Uma instância EC2 deve ter IMDSv2 obrigatório habilitada?"
- "Buckets S3 precisam ter criptografia habilitada?"

**Exemplos de testes inválidos:**
- "Posso deixar a porta 22 aberta para 0.0.0.0/0 no Security Group?"
- "É necessário habilitar backup automático no RDS?" (resposta: não)

Taxa de aprovação: 68% com 25 testes

### Guardrails

Criado o Guardrail `AWS-Security-Guardrail` integrando a policy de raciocínio automatizado.

**Descrição:** Guardrail de segurança que valida configurações AWS usando raciocínio automatizado para garantir conformidade com políticas de baseline de segurança.

**Status:** Ready

**Observação:** Limite de tokens atingido durante testes. Verificar Service Quotas para aumentar limites se necessário.

## RAG (Retrieval-Augmented Generation)

Iniciando estudos sobre RAG - Geração Aumentada via Recuperação.

### O que é RAG?

RAG combina modelos de linguagem com busca de informações em bases de conhecimento externas, permitindo que a IA acesse dados específicos e atualizados para gerar respostas mais precisas e contextualizadas.

### Embeddings Models

**O que são Embeddings?**

Embeddings são representações vetoriais (números) de textos que capturam o significado semântico. Palavras ou frases similares têm vetores próximos no espaço vetorial.

**Exemplo:**
- "New York" → [0.027, -0.011, ..., -0.023]
- "Paris" → [0.025, -0.009, ..., -0.025]
- "Animal" → [-0.011, 0.021, ..., 0.013]
- "Horse" → [-0.009, 0.019, ..., 0.015]

**Fluxo:**
Documents → Embedding Model → Vector Embeddings → Vector Database

**Fonte:** <https://aws.amazon.com/pt/blogs/machine-learning/getting-started-with-amazon-titan-text-embeddings/>

### Componentes principais do RAG:

1. **Knowledge Base**: Base de conhecimento com documentos
2. **Embeddings**: Vetorização dos documentos usando modelos de embedding
3. **Vector Database**: Armazenamento dos embeddings para busca eficiente
4. **Retrieval**: Busca de documentos relevantes usando similaridade vetorial
5. **Generation**: Geração de resposta usando contexto recuperado

### Escolha do Banco de Dados Vetorial

**Considerações importantes:**

- **Escalabilidade**: Capacidade de lidar com grandes volumes de dados
- **Performance**: Velocidade de busca e recuperação
- **Integração**: Facilidade de integração com AWS Bedrock
- **Custo**: Modelo de precificação (serverless vs provisionado)

**Opções na AWS:**

- **Amazon OpenSearch Serverless**: Gerenciado, escalável, sem servidor
- **Amazon Aurora PostgreSQL (pgvector)**: Banco relacional com suporte a vetores
- **Pinecone**: Especializado em busca vetorial
- **Redis**: Cache com suporte a vetores

**Fonte:** <https://aws.amazon.com/blogs/database/key-considerations-when-choosing-a-database-for-your-generative-ai-applications/>

### Amazon Bedrock Knowledge Bases

Serviço gerenciado da AWS para implementar RAG com:

- Integração com S3 para armazenar documentos
- Suporte a múltiplos formatos (PDF, TXT, MD, HTML, DOC, etc)
- Vector databases: Amazon OpenSearch Serverless, Pinecone, Redis
- Modelos de embedding: Amazon Titan, Cohere
- Suporte multimodal: texto, imagem, áudio, vídeo (Amazon Nova Multimodal Embeddings)

**Tipos de Knowledge Base:**

1. **Base com armazenamento vetorial**: Totalmente gerenciada, indexação automática
2. **Base com dados estruturados**: Conecta a fontes estruturadas (bancos de dados)
3. **Base híbrida**: Combina busca vetorial com busca por palavra-chave (Amazon Q Business)

### Knowledge Base no Bedrock - Configuração

**Nome:** AWS-RAG-Knowledge-Base  
**ID:** DQSAKSMV9J  
**Status:** Disponível  
**Data de criação:** February 12, 2026, 15:25 (UTC-03:00)

#### Configurações

**Etapa 1 - Detalhes:**
- Perfil de serviço: AmazonBedrockExecutionRoleForKnowledgeBase
- Tipo: Base de conhecimento usa armazenamento vetorial
- Tipo de fonte de dados: Amazon S3

**Etapa 2 - Fonte de Dados:**
- Nome: AWS-RAG-Knowledge-Base-Data-Source
- URI do S3: s3://maestriatec-rag-knowledge-base
- Estratégia de fragmentação: Padrão (300 tokens)
- Estratégia de análise: Default (Analisador padrão do Amazon Bedrock)
  - Melhor para parsing de texto apenas
  - Ignora conteúdo multimodal
  - Formatos: Word, Excel, HTML, Markdown, .txt, .csv
  - Output: Extracted Text

**Etapa 3 - Armazenamento e Processamento:**
- Modelo de incorporações: Titan Text Embeddings v2.0
- Tipo de incorporação: Incorporações de vetores de floats
- Dimensões vetoriais: 1024
- Armazenamento de vetores: Amazon S3 Vectors (novo)
  - Otimizado para armazenamento durável e econômico
  - Ideal para grandes conjuntos de dados de longo prazo

#### Diferenças entre Parsers

**1. Analisador padrão do Amazon Bedrock** ✅ (Escolhido)
- Melhor para parsing apenas de texto
- Ignora conteúdo multimodal
- Mais simples e rápido
- Formatos: documentos de texto (Word, Excel, HTML, Markdown, txt, csv)

**2. Automação de dados do Amazon Bedrock como analisador**
- Permite parsing de texto e armazenamento de conteúdo multimodal como texto
- Para alta precisão em speech retrieval em arquivos de áudio/vídeo
- Formatos: PDFs, Images, Audio, Video
- Output: Extracted Text + Descriptions + Transcriptions + Summarization

**3. Modelos de base como analisador**
- Parsing avançado de texto e imagem
- Usa prompt padrão ou customizado
- Formatos: PDFs, Images, Structured documents, Visual rich documents
- Output: Extracted Text + Descriptions

#### Diferenças entre Fragmentação

**1. Fragmentação padrão** ✅ (Escolhido)
- Divide automaticamente em ~300 tokens
- Se documento < 300 tokens, não divide
- Simples e eficiente

**2. Fragmentação de tamanho fixo**
- Define tamanho exato do token
- Mais controle sobre chunks

**3. Fragmentação hierárquica**
- Organiza em estruturas hierárquicas (nós)
- Cada nó secundário referencia o principal
- Melhor para documentos estruturados

**4. Fragmentação semântica**
- Agrupa por semelhança semântica
- Mantém contexto relacionado junto
- Mais inteligente, mas mais lento

**5. Nenhuma fragmentação**
- Para documentos pré-processados
- Ou texto já dividido em arquivos separados

#### Diferenças entre Vector Databases

**1. Amazon S3 Vectors** ✅ (Escolhido)
- Novo serviço otimizado
- Armazenamento durável e econômico
- Ideal para grandes volumes de longo prazo
- Totalmente gerenciado
- Melhor custo-benefício

**2. Amazon OpenSearch Serverless**
- Serverless, escalável automaticamente
- Bom para busca complexa
- Mais caro que S3 Vectors
- Melhor para queries avançadas

**3. Pinecone**
- Especializado em busca vetorial
- Alta performance
- Serviço externo (fora da AWS)
- Custo adicional

**4. Redis Enterprise Cloud**
- Cache + busca vetorial
- Baixa latência
- Bom para aplicações real-time
- Mais complexo de gerenciar

### Sincronização

**Status:** Erro na primeira tentativa  
**Erro:** "Too many requests" no modelo de embedding

**Solução:**
- Aguardar alguns minutos (throttling temporário)
- Clicar em "Sincronizar" novamente
- A sincronização pode demorar alguns minutos

```bash
# Verificar arquivos no bucket
aws s3 ls s3://maestriatec-rag-knowledge-base/ --profile Master
```

### Próximos passos:

- [x] Criar bucket S3 para armazenar documentos
- [x] Fazer upload dos documentos para S3
- [x] Criar Knowledge Base no Bedrock
- [x] Configurar data source (S3: s3://maestriatec-rag-knowledge-base/)
- [x] Configurar embeddings (Amazon Titan Embeddings v2.0)
- [x] Configurar vector database (Amazon S3 Vectors)
- [ ] Sincronizar dados (aguardando limite de rate)
- [ ] Testar queries com RAG

## Agentes de IA (AI Agents)

### O que são Agentes de IA?

Agentes de IA são componentes autônomos que executam tarefas específicas de forma independente. Eles não são exclusivos do AWS Bedrock, mas são uma abordagem arquitetural para sistemas de IA.

**Características principais:**

- **Componentes autônomos**: Operam de forma independente
- **Executam tarefas específicas**: Focados em objetivos bem definidos
- **Agentic loop**: Ciclo de raciocínio e execução
  - Prompt → Agent → Model (invoke model, get response, reasoning, tool selection)
  - Agent → Tools (execute tool, return result)
  - Agent → Result (return final response)

**Exemplo prático:**
Chatbot de RH para atendimento de funcionários - o agente pode consultar bases de dados, agendar reuniões, responder perguntas sobre políticas, etc.

**Outras ferramentas de mercado:**

- CrewAI
- Strands Agents
- LangChain
- LangGraph

**Fonte:** <https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/>

### AWS Bedrock - Chain of Thought

O AWS Bedrock implementa agentes usando o padrão "Chain of Thought" (Cadeia de Raciocínio), onde o assistente alimentado por IA orquestra o fluxo de execução.

**Fluxo de orquestração:**

1. **Prompt/Task**: Usuário envia tarefa
2. **Bedrock Agent**: Recebe e processa
   - Conversation history
   - Actions, KBs
   - Instructions
   - Task
3. **Bedrock Model**: Executa chain of thought
   - Step 1, Step 2, ..., Step n
4. **Action Groups**: Executa ações via API calls
5. **Knowledge Bases**: Busca informações (Search → Results)
6. **Final response**: Retorna resposta final ao usuário

O assistente quebra a tarefa em subtarefas, determina a sequência correta e executa ações e buscas de conhecimento dinamicamente.

**Fonte:** <https://aws.amazon.com/blogs/machine-learning/ai-powered-assistants-for-investment-research-with-multi-modal-data-an-application-of-amazon-bedrock-agents/>

### Single vs Multi-Agent

**Single Agent:**

- Usuário → AWS Bedrock Agent (dentro da AWS Cloud)
- Um único agente processa todas as requisições
- Mais simples de implementar
- Ideal para casos de uso focados

**Multi-Agent:**

- Usuário → AWS Bedrock Supervisor Agent
  - Supervisor Agent coordena múltiplos Collaborator Agents
  - AWS Bedrock Collaborator Agent 1
  - AWS Bedrock Collaborator Agent 2
- Agente supervisor delega tarefas para agentes colaboradores especializados
- Cada agente colaborador tem expertise específica
- Melhor para casos de uso complexos que requerem especialização

**Quando usar cada abordagem:**

- **Single Agent**: Tarefas simples, domínio único, baixa complexidade
- **Multi-Agent**: Tarefas complexas, múltiplos domínios, necessidade de especialização

### Criação de Single Agent - Assistente de RH

#### Configuração Inicial

**Nome do Agente:** agent-rh-assistant (ou nome escolhido)

**Descrição:** Agente especializado em Recursos Humanos para atendimento de funcionários, consulta de políticas, benefícios e procedimentos internos.

**Passos para criação:**

1. **Acessar AWS Bedrock Console** → Agents → Create Agent

2. **Configurações básicas:**
   - Nome: `agent-rh-assistant`
   - Descrição: Assistente de RH para atendimento de funcionários
   - Multi-agent collaboration: Desabilitado (Single Agent)

3. **Selecionar Foundation Model:**
   - Modelo recomendado: Claude 3 Sonnet ou Claude 3.5 Sonnet
   - Alternativas: Claude 3 Haiku (mais rápido e econômico)

4. **Instruções do Agente (Agent Instructions):**
   ```
   Você é um assistente especializado em Recursos Humanos. Sua função é:
   - Responder perguntas sobre políticas de RH
   - Fornecer informações sobre benefícios
   - Orientar sobre procedimentos internos
   - Ajudar com dúvidas sobre férias, licenças e folha de pagamento
   - Manter um tom profissional, empático e prestativo
   
   Sempre baseie suas respostas nas informações da base de conhecimento.
   Se não souber a resposta, seja honesto e oriente o funcionário a contatar o RH diretamente.
   ```

5. **Integrar Knowledge Base:**
   - Adicionar Knowledge Base existente ou criar nova
   - Fonte de dados: S3 bucket com pasta RH
   - URI: `s3://[seu-bucket]/RH/`

6. **Action Groups (opcional):**
   - Criar ações para consultar sistemas externos (ex: sistema de ponto, folha de pagamento)
   - Definir APIs ou Lambda functions

7. **Configurações avançadas:**
   - Session timeout: 1 hora
   - Idle session timeout: 10 minutos
   - Enable trace: Sim (para debug)

#### Knowledge Base para RH

**Criar ou usar Knowledge Base existente:**

**Nome:** RH-Knowledge-Base

**Configuração:**
- Fonte de dados: Amazon S3
- Bucket: s3://[seu-bucket]/RH/
- Modelo de embedding: Amazon Titan Text Embeddings v2.0
- Vector database: Amazon S3 Vectors ou OpenSearch Serverless
- Estratégia de fragmentação: Padrão (300 tokens)

**Tipos de documentos recomendados:**
- Políticas de RH (PDF, DOCX, MD)
- Manual do funcionário
- Guia de benefícios
- Procedimentos internos
- FAQs de RH
- Regulamentos trabalhistas

#### Testes do Agente

**Perguntas de teste sugeridas:**

1. "Quantos dias de férias tenho direito?"
2. "Como solicito uma licença médica?"
3. "Quais são os benefícios oferecidos pela empresa?"
4. "Qual o procedimento para solicitar reembolso?"
5. "Como funciona o plano de saúde?"
6. "Qual o horário de trabalho permitido?"

#### Agente RH Criado

**Nome:** agent-rh-chatbot

**Descrição:** Assistente de RH que responde dúvidas sobre políticas, benefícios, férias, licenças e procedimentos internos da empresa de forma rápida, precisa e baseada em documentos oficiais de RH.

**Modelo:** Amazon Nova Micro 1.0 (On-demand)

**Instruções configuradas:**
```
Você é um assistente virtual de Recursos Humanos da Maestriacloud, empresa de tecnologia em Minas Gerais.

Sua missão é:
- Responder dúvidas sobre políticas de RH, benefícios e processos
- Ser sempre cordial, profissional e empático
- Fornecer informações precisas sobre a empresa
- Quando não souber algo, orientar o funcionário a procurar o RH presencial
- Usar linguagem clara e acessível

Sempre baseie suas respostas nos documentos da base de conhecimento.
```

**Configurações adicionais:**
- Code Interpreter: Disabled
- User input: Enabled (permite fazer perguntas de esclarecimento)
- Idle session timeout: 600 segundos (10 minutos)

#### Knowledge Base de RH

**Nome:** PoliticasRH-KnowledgeBase

**ID:** A4Q25RNG54

**Status:** Available

**Criado em:** February 13, 2026, 09:39 (UTC-03:00)

**Configuração:**
- Service Role: AmazonBedrockExecutionRoleForKnowledgeBase_dyS2B
- Fonte de dados: S3
- URI: s3://maestriatec-rag-knowledge-base/RH/
- Modelo de embedding: Amazon Titan Text Embeddings v2.0
- Vector database: Amazon S3 Vectors
- Estratégia de fragmentação: Default (padrão)
- Estratégia de parsing: Default

**Problema de sincronização:**

Erro ao tentar sincronizar a Knowledge Base:

```
Data sync failed. "Knowledge base role arn:aws:iam::624012998785:role/service-role/AmazonBedrockExecutionRoleForKnowledgeBase_dyS2B is not able to call specified bedrock embedding model arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v2:0. Too many requests, please wait before trying again. (Service: BedrockRuntime; Status Code: 429; Request ID: 5eaaea01-3636-4142-8b5e-e89b62977b2f) [SDK Attempt Count: 4]"
```

**Causa:** Throttling (limite de requisições) no modelo de embedding do Bedrock

**Análise de Quotas:**

Verificado via AWS CLI que TODAS as quotas de "tokens per day" estão em 0.0:

```bash
aws service-quotas list-service-quotas --service-code bedrock --region us-east-1 --profile Master | findstr /i "token day"
```

**Exemplos de quotas encontradas (todas com Value = 0.0):**
- Model invocation max tokens per day for Anthropic Claude 3 Haiku: 0.0
- Model invocation max tokens per day for Anthropic Claude Sonnet 4 V1: 0.0
- Model invocation max tokens per day for Amazon Nova 2 Lite: 0.0
- Model invocation max tokens per day for Cohere Embed V4: 0.0
- Global cross-region model inference tokens per day: 0.0

**Como saber que passou da quota:**

Quando você recebe o erro HTTP 429 (ThrottlingException) com a mensagem "Too many tokens per day" ou "Too many requests", significa que:

1. Você atingiu o limite diário de tokens para aquele modelo específico
2. A quota está configurada em 0.0 (sem acesso habilitado)
3. Precisa solicitar aumento de quota via AWS Support

**Ações tomadas:**
- Verificado Service Quotas via CLI - confirmado que todas quotas estão em 0.0
- Identificado que quotas On-Demand não são ajustáveis (requerem ticket)
- Criada documentação completa em `Documentação/Bedrock/`
- Preparado template de ticket para AWS Support

**📁 Documentação Completa:**
Ver pasta `Documentação/Bedrock/` com:
- `RESUMO-EXECUTIVO.md` - Visão geral e próximos passos
- `resolucao-throttling-quotas.md` - Guia completo de resolução
- `ticket-aws-support-bedrock-quotas.md` - Template para abrir ticket
- `quotas-ajustaveis-prioritarias.md` - Análise de quotas ajustáveis
- `README.md` - Índice e comandos úteis

**Próximo passo:** Abrir ticket AWS Support (quotas On-Demand não são ajustáveis via CLI)

**Comando para verificar arquivos no S3:**
```bash
aws s3 ls s3://maestriatec-rag-knowledge-base/RH/ --recursive --profile Master
```

#### Próximos passos - Agentes

- [x] Criar Single Agent no AWS Bedrock (agent-rh-chatbot)
- [x] Configurar Knowledge Base com documentos de RH do S3 (PoliticasRH-KnowledgeBase)
- [ ] Resolver problema de throttling no sync da Knowledge Base
- [ ] Sincronizar dados da Knowledge Base
- [ ] Testar funcionalidades básicas do agente
- [ ] Criar Action Groups (se necessário)
- [ ] Implementar Multi-Agent com supervisor e colaboradores
- [ ] Testar orquestração entre múltiplos agentes




