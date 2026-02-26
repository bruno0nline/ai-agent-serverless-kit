# 🗂️ Plano de Reorganização do Repositório

**Data:** 26/02/2026  
**Objetivo:** Limpar, organizar e profissionalizar a estrutura do projeto

---

## 📊 Análise Atual

### ✅ Estrutura Boa (Manter)
```
/BedrockFlows/OrderStatusAssistant/     # Projeto Flow bem organizado
/Documentação/                          # Documentação estruturada
/Lambda/                                # Lambdas organizadas por tipo
/PythonAwsBedrockActionGroupDemo/       # Action Group completo
/RAG-Knowledge-Base/                    # Knowledge Bases separadas
/Scripts/                               # Scripts AWS por serviço
/tests/                                 # Scripts de teste
```

### ⚠️ Problemas Identificados

1. **Screenshots (40 arquivos)** - Muitos prints de debug/troubleshooting
2. **Arquivos duplicados** - `lambda_function.py` vs `lambda_query_order.py`
3. **Arquivos temporários** - `.bak`, `Zone.Identifier`, zips grandes
4. **Pasta confusa** - `wsl.localhost/` (parece erro de cópia)
5. **Arquivos soltos na raiz** - `AI`, `davinci.txt`
6. **Instaladores grandes** - 240MB de instaladores

---

## 🎯 Ações Propostas

### 1. Screenshots (Limpar 90%)

**Manter apenas (3 arquivos):**
- `2026-02-26 10_19_07-.png` - Flow funcionando (sucesso final)
- `2026-02-26 09_33_19-Prompt Management.png` - Configuração do Prompt
- `2026-02-25 13_40_14-Window.png` - Arquitetura do projeto

**Excluir:** Todos os outros prints de debug/erro (37 arquivos)

### 2. BedrockFlows - Consolidar

**Problema:** Arquivos duplicados/antigos
- `lambda_function.py` (antigo)
- `lambda_query_order.py` (atual - funcionando)
- `sample-orders.json` (10 pedidos - substituído)
- `sample-orders-25.json` (25 pedidos - atual)

**Ação:**
- Renomear `lambda_query_order.py` → `lambda_function.py`
- Excluir `sample-orders.json` (manter apenas o de 25)
- Mover eventos de teste para subpasta organizada

### 3. Arquivos Temporários (Excluir)

```
/PythonAwsBedrockActionGroupDemo/python_dependencies.zip (19MB)
/PythonAwsBedrockActionGroupDemo/aws-lambda-layer.zip (19MB)
/PythonAwsBedrockActionGroupDemo/python/ (pasta completa - já está no zip)
/PythonAwsBedrockActionGroupDemo/venv/ (ambiente virtual - não vai pro Git)
/RAG-Knowledge-Base/KB-RH/*.Zone.Identifier (arquivos Windows)
/README.md.bak
/AI (arquivo binário estranho)
/davinci.txt
```

### 4. Pasta Estranha (Excluir)

```
/wsl.localhost/ (parece erro de cópia do Windows)
```

### 5. Instaladores (Mover para .gitignore)

**Problema:** 240MB de instaladores no repositório

**Ação:**
- Adicionar ao `.gitignore`
- Criar `INSTALADORES.md` com links de download
- Remover do Git (manter local se quiser)

### 6. Reorganizar Raiz

**Arquivos na raiz (manter organizados):**
```
✅ README.md
✅ LICENSE
✅ .gitignore
✅ ROADMAP.md
✅ ARCHITECTURE.md
✅ DEPLOYMENT.md
✅ CONTRIBUTING.md
✅ TECH-STACK-2026.md
✅ GIT-SETUP.md
✅ PUSH-TO-GITHUB.md
✅ GUIA-REPLICACAO.md
✅ DOCUMENTACAO-INDICE.md
✅ PROMPT-CONTEXTO.md
✅ PROMPT-RAPIDO.txt
✅ bedrock-quotas.json
✅ AI.code-workspace
```

**Mover para /docs/:**
```
→ git-push.sh
→ git-push.ps1
```

---

## 📁 Estrutura Final Proposta

```
/home/bruno/AI/
├── .git/
├── .gitignore (atualizado)
├── README.md
├── LICENSE
├── ROADMAP.md
├── ARCHITECTURE.md
├── DEPLOYMENT.md
├── CONTRIBUTING.md
├── TECH-STACK-2026.md
├── GUIA-REPLICACAO.md
├── DOCUMENTACAO-INDICE.md
├── PROMPT-CONTEXTO.md
├── PROMPT-RAPIDO.txt
├── bedrock-quotas.json
├── AI.code-workspace
│
├── BedrockFlows/
│   └── OrderStatusAssistant/
│       ├── README.md
│       ├── lambda_function.py (renomeado)
│       ├── sample-orders.json (25 pedidos)
│       ├── PROMPT-INSTRUCTIONS.md
│       ├── prompt-text.txt
│       ├── deploy-lambda.sh
│       ├── deploy-dynamodb.sh
│       └── test-events/
│           ├── test-query-delivered.json
│           ├── test-query-processing.json
│           ├── test-query-shipped.json
│           ├── test-query-cancelled.json
│           └── test-query-notfound.json
│
├── PythonAwsBedrockActionGroupDemo/
│   ├── README.md
│   ├── lambda_function_bedrock.py
│   ├── lambda_function_regular.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── create_zip.py
│   ├── COMANDOS-WINDOWS.md
│   ├── LICENSE
│   ├── .gitignore
│   └── test/
│
├── Lambda/
│   ├── README.md
│   ├── INTEGRATION-GUIDE.md
│   ├── action-groups/
│   ├── api/
│   └── webhooks/
│
├── RAG-Knowledge-Base/
│   ├── README.md
│   ├── KB-RH/
│   ├── KB-Cursos/
│   └── KB-Aws-Security/
│
├── Documentação/
│   ├── Inteligência Artificial AWS Bedrock.md
│   ├── agents-maestriacloud.md
│   ├── CUSTOS.md
│   ├── comandos-kiro.txt
│   ├── prompt-kiro.txt
│   ├── Script Bruno.txt
│   ├── Bedrock/
│   └── Kiro/
│
├── Scripts/
│   ├── S3/
│   ├── EC2/
│   ├── IAM/
│   ├── RDS/
│   ├── CloudWatch/
│   ├── Lambda/
│   └── DynamoDB/
│
├── tests/
│   ├── README.md
│   ├── test_multi_agent.py
│   ├── list_agents.py
│   ├── monitor_costs.py
│   └── backup_config.py
│
├── Configurações/
│   ├── variavel-de-ambientes.txt
│   └── profile-sso.txt
│
├── Curso/
│   ├── Domine AWS Bedrock...txt
│   └── Conteudo do curso.txt
│
├── Screenshots/ (apenas 3 arquivos importantes)
│   ├── flow-funcionando-sucesso.png
│   ├── prompt-management-config.png
│   └── arquitetura-projeto.png
│
├── docs/ (nova pasta)
│   ├── GIT-SETUP.md
│   ├── PUSH-TO-GITHUB.md
│   ├── git-push.sh
│   ├── git-push.ps1
│   └── INSTALADORES.md (novo)
│
├── backup/ (mantém backups de config)
│
└── Instaladores/ (local only - não vai pro Git)
```

---

## 🔧 Atualizar .gitignore

```gitignore
# Adicionar:
Instaladores/
*.Zone.Identifier
*.bak
python_dependencies.zip
aws-lambda-layer.zip
venv/
python/
__pycache__/
*.pyc
.DS_Store
wsl.localhost/
AI
davinci.txt
```

---

## ✅ Checklist de Execução

### Fase 1: Limpeza (5 min)
- [ ] Excluir 37 screenshots desnecessários
- [ ] Excluir arquivos temporários (zips, venv, python/)
- [ ] Excluir arquivos estranhos (wsl.localhost/, AI, davinci.txt)
- [ ] Excluir arquivos .Zone.Identifier e .bak

### Fase 2: Reorganização (5 min)
- [ ] Renomear lambda_query_order.py → lambda_function.py
- [ ] Renomear sample-orders-25.json → sample-orders.json
- [ ] Excluir lambda_function.py antigo
- [ ] Renomear 3 screenshots importantes
- [ ] Criar pasta /docs/
- [ ] Mover scripts git para /docs/
- [ ] Criar INSTALADORES.md

### Fase 3: Git (5 min)
- [ ] Atualizar .gitignore
- [ ] git add .
- [ ] git commit -m "refactor: reorganização completa do repositório"
- [ ] git push origin main

### Fase 4: Documentação (5 min)
- [ ] Atualizar README.md com nova estrutura
- [ ] Atualizar DOCUMENTACAO-INDICE.md
- [ ] Criar CHANGELOG.md

---

## 📈 Resultado Esperado

**Antes:**
- 350+ arquivos
- ~300MB (com instaladores)
- Estrutura confusa
- Muitos arquivos temporários

**Depois:**
- ~100 arquivos essenciais
- ~50MB (sem instaladores)
- Estrutura profissional
- Fácil navegação
- Pronto para colaboração

---

## 🎯 Próximos Passos

1. ✅ Aprovar este plano
2. ✅ Executar limpeza e reorganização
3. ✅ Commit e push para GitHub
4. ✅ Iniciar Seção 7 - Projeto YouTube

---

**Aguardando aprovação para iniciar! 🚀**
