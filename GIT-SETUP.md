# 🚀 Setup Git e Push para GitHub

## Comandos para executar no terminal

### 1. Inicializar Git (se ainda não foi feito)

```bash
# Navegar para a pasta do projeto
cd "P:\Meu Drive\Documentos\Cursos\AI"

# Inicializar repositório Git
git init

# Verificar status
git status
```

---

### 2. Configurar Git (se necessário)

```bash
# Configurar nome e email
git config --global user.name "Bruno Mendes Augusto"
git config --global user.email "brunomendesaugusto@gmail.com"

# Verificar configuração
git config --list
```

---

### 3. Adicionar Remote (GitHub)

```bash
# Adicionar repositório remoto via SSH
git remote add origin git@github.com:bruno0nline/ai-agent-serverless-kit.git

# Verificar remote
git remote -v
```

---

### 4. Preparar Arquivos para Commit

```bash
# Adicionar todos os arquivos (exceto os do .gitignore)
git add .

# Verificar o que será commitado
git status

# Se quiser ver detalhes
git diff --cached
```

---

### 5. Fazer o Primeiro Commit

```bash
# Commit inicial
git commit -m "feat: initial commit - AI Agent Serverless Kit

- Complete project structure
- AWS Bedrock Agent with RAG
- Knowledge Base configuration
- Comprehensive documentation
- Deployment guide
- Tech stack recommendations
- Troubleshooting guides"

# Verificar commit
git log --oneline
```

---

### 6. Push para GitHub

```bash
# Push para branch main
git push -u origin main

# Se der erro de branch, criar main primeiro:
git branch -M main
git push -u origin main
```

---

## 🔑 Verificar Chave SSH

Se der erro de autenticação SSH:

```bash
# Verificar se a chave SSH está configurada
ssh -T git@github.com

# Deve retornar: "Hi bruno0nline! You've successfully authenticated..."
```

Se não funcionar:

```bash
# Listar chaves SSH
ls -la ~/.ssh

# Adicionar chave ao ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/GitHubKey

# Testar novamente
ssh -T git@github.com
```

---

## 📝 Commits Futuros

Para commits futuros, use este padrão:

```bash
# 1. Ver o que mudou
git status

# 2. Adicionar arquivos
git add .
# ou específicos:
git add arquivo1.md arquivo2.py

# 3. Commit com mensagem descritiva
git commit -m "tipo: descrição curta

Descrição detalhada (opcional)"

# 4. Push
git push
```

### Tipos de commit (Conventional Commits):

- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Documentação
- `style:` - Formatação
- `refactor:` - Refatoração
- `test:` - Testes
- `chore:` - Tarefas gerais

**Exemplos:**
```bash
git commit -m "feat: add Slack integration"
git commit -m "fix: resolve quota check error"
git commit -m "docs: update deployment guide"
git commit -m "chore: update dependencies"
```

---

## 🌿 Trabalhando com Branches

### Criar branch para nova feature

```bash
# Criar e mudar para nova branch
git checkout -b feature/nome-da-feature

# Fazer alterações...
git add .
git commit -m "feat: adiciona nova feature"

# Push da branch
git push -u origin feature/nome-da-feature
```

### Merge via Pull Request (Recomendado)

1. Push da branch
2. Ir no GitHub
3. Criar Pull Request
4. Revisar e fazer merge

### Merge local (Alternativa)

```bash
# Voltar para main
git checkout main

# Fazer merge
git merge feature/nome-da-feature

# Push
git push

# Deletar branch local (opcional)
git branch -d feature/nome-da-feature

# Deletar branch remota (opcional)
git push origin --delete feature/nome-da-feature
```

---

## 🔄 Atualizar do GitHub

```bash
# Baixar alterações
git pull origin main

# Ou se preferir rebase
git pull --rebase origin main
```

---

## 🧹 Comandos Úteis

### Ver histórico
```bash
git log --oneline --graph --all
```

### Ver diferenças
```bash
git diff                    # Mudanças não staged
git diff --staged          # Mudanças staged
git diff HEAD              # Todas as mudanças
```

### Desfazer mudanças
```bash
git restore arquivo.txt    # Desfazer mudanças não commitadas
git reset HEAD~1           # Desfazer último commit (mantém mudanças)
git reset --hard HEAD~1    # Desfazer último commit (perde mudanças)
```

### Ver branches
```bash
git branch                 # Branches locais
git branch -r              # Branches remotas
git branch -a              # Todas as branches
```

### Limpar arquivos não rastreados
```bash
git clean -n               # Ver o que seria deletado
git clean -f               # Deletar arquivos não rastreados
git clean -fd              # Deletar arquivos e diretórios
```

---

## ⚠️ Arquivos Ignorados

O `.gitignore` já está configurado para ignorar:

- ✅ Credenciais AWS (`.aws/`, `*.pem`, `*.key`)
- ✅ Variáveis de ambiente (`.env*`)
- ✅ Logs (`*.log`)
- ✅ Arquivos temporários
- ✅ Screenshots (podem ter info sensível)
- ✅ Instaladores
- ✅ Dados sensíveis (`bedrock-quotas.json`)

**IMPORTANTE:** Nunca commite:
- Credenciais AWS
- Chaves SSH
- Tokens de acesso
- Informações sensíveis

---

## 📊 Verificar Tamanho do Repositório

```bash
# Ver tamanho dos arquivos
git count-objects -vH

# Ver arquivos grandes
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  awk '/^blob/ {print substr($0,6)}' | \
  sort --numeric-sort --key=2 | \
  tail -10
```

---

## 🆘 Problemas Comuns

### Erro: "Permission denied (publickey)"
```bash
# Verificar chave SSH
ssh -T git@github.com

# Adicionar chave
ssh-add ~/.ssh/GitHubKey
```

### Erro: "fatal: remote origin already exists"
```bash
# Remover remote existente
git remote remove origin

# Adicionar novamente
git remote add origin git@github.com:bruno0nline/ai-agent-serverless-kit.git
```

### Erro: "Updates were rejected"
```bash
# Forçar push (cuidado!)
git push -f origin main

# Ou fazer pull primeiro
git pull origin main --rebase
git push origin main
```

### Arquivo muito grande
```bash
# Remover do histórico (cuidado!)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch caminho/arquivo-grande" \
  --prune-empty --tag-name-filter cat -- --all

# Forçar push
git push origin --force --all
```

---

## ✅ Checklist Antes do Push

- [ ] Removi informações sensíveis?
- [ ] Testei as mudanças localmente?
- [ ] Atualizei a documentação?
- [ ] Commit message está clara?
- [ ] `.gitignore` está correto?

---

**Pronto para começar!** Execute os comandos da seção 1-6 em ordem. 🚀
