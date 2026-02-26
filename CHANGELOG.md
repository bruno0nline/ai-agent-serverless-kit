# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [2.0.0] - 2026-02-26

### ✨ Adicionado
- **Bedrock Flow OrderStatusAssistant** - Flow completo funcionando
  - Lambda Function consultando DynamoDB (25 pedidos)
  - Prompt Management com respostas amigáveis
  - Integração Input → Lambda → Prompt → Output
- README.md na pasta Screenshots documentando arquivos mantidos
- CHANGELOG.md para rastrear mudanças do projeto
- REORGANIZACAO-PLANO.md com plano detalhado de limpeza

### 🔄 Modificado
- **Reorganização completa do repositório**
  - Screenshots: 40 → 4 arquivos (apenas importantes + README)
  - Renomeados para nomes descritivos (flow-funcionando-sucesso.png, etc)
  - BedrockFlows: lambda_query_order.py → lambda_function.py (padrão AWS)
  - sample-orders-25.json → sample-orders.json (versão atual)
- **.gitignore atualizado**
  - Adicionados padrões para Zone.Identifier, backups, zips
  - Configurado para ignorar pasta python/ do Lambda Layer
- **README.md** - Versão atualizada para 2.0

### 🗑️ Removido
- 37 screenshots de debug/troubleshooting (movidos para backup local)
- Arquivos temporários: AI, davinci.txt, README.md.bak
- Arquivos Windows: *.Zone.Identifier
- Pasta estranha: wsl.localhost/

### 📦 Preservado
- **TODOS os arquivos de código e configuração**
- **TODOS os exemplos e templates**
- **TODA a documentação**
- Versão antiga da Lambda (lambda_function_OLD.py) para referência
- Sample com 10 pedidos (sample-orders-10.json) para testes menores

---

## [1.1.0] - 2026-02-20

### ✨ Adicionado
- Multi-Agent Collaboration
  - Supervisor Agent: Patrícia (Amazon Nova Pro 1.0)
  - Collaborator Agent RH: Carla (Amazon Nova Micro 1.0)
  - Collaborator Agent Vendas: Rafael (Claude 3.5 Haiku v1)
- Knowledge Base de Cursos (PoliticasCurso-Knowledge-Base)
- Scripts de teste automatizados
- Documentação completa de custos

### 🔧 Corrigido
- Problema de throttling do Bedrock resolvido (ticket AWS #624012998785)
- Acesso aos modelos Bedrock liberado

---

## [1.0.0] - 2026-02-19

### ✨ Adicionado
- Lambda Action Group para consulta de feriados brasileiros
- Lambda Layer com biblioteca holidays (Docker build)
- Guardrail implementado (Filtro-de-Conteudo-Ofensivo)
- Agent RH testado e funcionando
- Integração Lambda + Bedrock Agent

---

## [0.9.0] - 2026-02-16

### ✨ Adicionado
- Configuração do ambiente (WSL, AWS CLI, Python)
- Estudos sobre Amazon Bedrock (Pricing, Guardrails, Automated Reasoning)
- Estudos sobre RAG (Embeddings, Vector Databases, Knowledge Bases)
- Criação de Knowledge Base (AWS-RAG-Knowledge-Base)
- Criação de Single Agent (agent-rh-chatbot)
- Criação de Knowledge Base de RH (PoliticasRH-KnowledgeBase)
- Análise de quotas do Bedrock
- Documentação completa de troubleshooting

---

## Tipos de Mudanças

- **✨ Adicionado** - para novas funcionalidades
- **🔄 Modificado** - para mudanças em funcionalidades existentes
- **🗑️ Removido** - para funcionalidades removidas
- **🔧 Corrigido** - para correção de bugs
- **🔒 Segurança** - para vulnerabilidades corrigidas
- **📦 Preservado** - para itens mantidos intencionalmente

---

**Formato de versão:** MAJOR.MINOR.PATCH
- **MAJOR:** Mudanças incompatíveis na API
- **MINOR:** Novas funcionalidades compatíveis
- **PATCH:** Correções de bugs compatíveis
