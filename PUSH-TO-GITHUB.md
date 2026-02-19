# 🚀 Push para GitHub - Guia Rápido

## Opção 1: Script Automático (Recomendado) ⭐

### Windows (PowerShell)

```powershell
# Abrir PowerShell na pasta do projeto
cd "P:\Meu Drive\Documentos\Cursos\AI"

# Executar script
.\git-push.ps1
```

### Linux/Mac (Bash)

```bash
# Navegar para pasta do projeto
cd "/mnt/p/Meu Drive/Documentos/Cursos/AI"

# Dar permissão de execução
chmod +x git-push.sh

# Executar script
./git-push.sh
```

---

## Opção 2: Comandos Manuais

### Passo a Passo

```bash
# 1. Navegar para pasta
cd "P:\Meu Drive\Documentos\Cursos\AI"

# 2. Inicializar Git (se necessário)
git init

# 3. Adicionar remote
git remote add origin git@github.com:bruno0nline/ai-agent-serverless-kit.git

# 4. Adicionar arquivos
git add .

# 5. Commit
git commit -m "feat: initial commit - AI Agent Serverless Kit"

# 6. Criar branch main
git branch -M main

# 7. Push
git push -u origin main
```

---

## ⚠️ Antes de Fazer Push

### Checklist de Segurança

- [ ] Removi credenciais AWS?
- [ ] Removi chaves SSH privadas?
- [ ] Removi tokens de acesso?
- [ ] Removi informações sensíveis?
- [ ] Verifiquei o `.gitignore`?

### Arquivos que NÃO devem ir para GitHub

❌ `.aws/` - Credenciais AWS  
❌ `*.pem`, `*.key` - Chaves privadas  
❌ `.env` - Variáveis de ambiente  
❌ `bedrock-quotas.json` - Dados da conta  
❌ `Screenshots/` - Podem ter info sensível  

✅ Todos já estão no `.gitignore`!

---

## 🔑 Verificar Chave SSH

Se der erro de autenticação:

```bash
# Testar conexão SSH
ssh -T git@github.com

# Deve retornar:
# "Hi bruno0nline! You've successfully authenticated..."
```

Se não funcionar:

```bash
# Adicionar chave ao ssh-agent
ssh-add ~/.ssh/GitHubKey

# Testar novamente
ssh -T git@github.com
```

---

## 📊 Após o Push

### 1. Verificar no GitHub

Acesse: https://github.com/bruno0nline/ai-agent-serverless-kit

Verifique se:
- [ ] Todos os arquivos foram enviados
- [ ] README.md está renderizando corretamente
- [ ] Badges estão funcionando
- [ ] Links estão corretos

### 2. Configurar Repositório

No GitHub, adicione:

**Descrição:**
```
🤖 Serverless AI Agent for HR automation using AWS Bedrock, RAG, and Amazon Nova - Low-cost ($2-12/month), production-ready, and easily replicable
```

**Topics (tags):**
```
aws
bedrock
ai-agent
rag
serverless
hr-automation
chatbot
amazon-nova
knowledge-base
low-cost
generative-ai
llm
aws-cdk
python
typescript
```

**Website:** (opcional)
```
https://aws.amazon.com/bedrock/
```

### 3. Configurar GitHub Pages (Opcional)

1. Settings → Pages
2. Source: Deploy from a branch
3. Branch: main / (root)
4. Save

Seu site estará em:
```
https://bruno0nline.github.io/ai-agent-serverless-kit/
```

### 4. Adicionar Badges Extras (Opcional)

Edite o README.md e adicione:

```markdown
[![GitHub stars](https://img.shields.io/github/stars/bruno0nline/ai-agent-serverless-kit?style=social)](https://github.com/bruno0nline/ai-agent-serverless-kit/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/bruno0nline/ai-agent-serverless-kit?style=social)](https://github.com/bruno0nline/ai-agent-serverless-kit/network/members)
[![GitHub issues](https://img.shields.io/github/issues/bruno0nline/ai-agent-serverless-kit)](https://github.com/bruno0nline/ai-agent-serverless-kit/issues)
```

---

## 🔄 Atualizações Futuras

### Fazer alterações e push

```bash
# 1. Fazer alterações nos arquivos

# 2. Ver o que mudou
git status

# 3. Adicionar mudanças
git add .

# 4. Commit
git commit -m "docs: update deployment guide"

# 5. Push
git push
```

### Criar nova feature

```bash
# 1. Criar branch
git checkout -b feature/slack-integration

# 2. Fazer alterações e commit
git add .
git commit -m "feat: add Slack integration"

# 3. Push da branch
git push -u origin feature/slack-integration

# 4. Criar Pull Request no GitHub
```

---

## 🐛 Problemas Comuns

### Erro: "Permission denied (publickey)"

**Solução:**
```bash
ssh-add ~/.ssh/GitHubKey
ssh -T git@github.com
```

### Erro: "remote origin already exists"

**Solução:**
```bash
git remote remove origin
git remote add origin git@github.com:bruno0nline/ai-agent-serverless-kit.git
```

### Erro: "Updates were rejected"

**Solução:**
```bash
# Opção 1: Pull primeiro
git pull origin main --rebase
git push origin main

# Opção 2: Force push (cuidado!)
git push -f origin main
```

### Arquivo muito grande (>100MB)

**Solução:**
```bash
# Remover do commit
git rm --cached arquivo-grande.zip

# Adicionar ao .gitignore
echo "arquivo-grande.zip" >> .gitignore

# Commit novamente
git add .gitignore
git commit --amend
git push -f origin main
```

---

## 📝 Comandos Úteis

```bash
# Ver histórico
git log --oneline --graph

# Ver diferenças
git diff

# Desfazer último commit (mantém mudanças)
git reset HEAD~1

# Ver branches
git branch -a

# Mudar de branch
git checkout nome-da-branch

# Atualizar do GitHub
git pull origin main
```

---

## 🎯 Próximos Passos

Após publicar no GitHub:

1. [ ] Compartilhar no LinkedIn
2. [ ] Postar no Reddit (r/aws, r/MachineLearning)
3. [ ] Compartilhar em grupos de AWS
4. [ ] Adicionar ao seu portfólio
5. [ ] Apresentar para BS4IT
6. [ ] Usar como case em entrevistas

---

## 📧 Suporte

Problemas com Git/GitHub?
- Documentação Git: https://git-scm.com/doc
- GitHub Docs: https://docs.github.com/
- Stack Overflow: https://stackoverflow.com/questions/tagged/git

---

**Pronto para publicar!** 🚀

Execute o script ou os comandos manuais e seu projeto estará no GitHub!
