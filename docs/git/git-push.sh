#!/bin/bash

# Script para fazer push inicial do projeto para GitHub
# Uso: bash git-push.sh

echo "🚀 AI Agent Serverless Kit - Git Setup"
echo "======================================="
echo ""

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Verificar se está na pasta correta
if [ ! -f "README.md" ]; then
    echo -e "${RED}❌ Erro: README.md não encontrado${NC}"
    echo "Execute este script na raiz do projeto"
    exit 1
fi

echo -e "${YELLOW}📋 Passo 1: Verificando Git...${NC}"
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git não está instalado${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Git encontrado${NC}"
echo ""

echo -e "${YELLOW}📋 Passo 2: Verificando chave SSH...${NC}"
if ssh -T git@github.com 2>&1 | grep -q "successfully authenticated"; then
    echo -e "${GREEN}✅ Autenticação SSH funcionando${NC}"
else
    echo -e "${RED}❌ Erro de autenticação SSH${NC}"
    echo "Execute: ssh-add ~/.ssh/GitHubKey"
    exit 1
fi
echo ""

echo -e "${YELLOW}📋 Passo 3: Inicializando repositório...${NC}"
if [ ! -d ".git" ]; then
    git init
    echo -e "${GREEN}✅ Repositório inicializado${NC}"
else
    echo -e "${GREEN}✅ Repositório já existe${NC}"
fi
echo ""

echo -e "${YELLOW}📋 Passo 4: Configurando remote...${NC}"
if git remote | grep -q "origin"; then
    echo -e "${YELLOW}⚠️  Remote 'origin' já existe, removendo...${NC}"
    git remote remove origin
fi
git remote add origin git@github.com:bruno0nline/ai-agent-serverless-kit.git
echo -e "${GREEN}✅ Remote configurado${NC}"
echo ""

echo -e "${YELLOW}📋 Passo 5: Adicionando arquivos...${NC}"
git add .
echo -e "${GREEN}✅ Arquivos adicionados${NC}"
echo ""

echo -e "${YELLOW}📋 Passo 6: Criando commit...${NC}"
git commit -m "feat: initial commit - AI Agent Serverless Kit

- Complete project structure
- AWS Bedrock Agent with RAG
- Knowledge Base configuration
- Comprehensive documentation (PT-BR)
- Deployment guide (15 min setup)
- Tech stack recommendations (2026)
- Troubleshooting guides
- Cost analysis and ROI calculator
- Roadmap (POC → Production → Commercial)

Tech Stack:
- AWS Bedrock Agent
- Amazon Nova Micro (LLM)
- Amazon Titan Embeddings v2.0
- S3 Vectors (Vector DB)
- 100% Serverless
- Low cost (\$2-12/month)

Features:
- RAG (Retrieval-Augmented Generation)
- Knowledge Base integration
- Multi-document support
- CloudWatch monitoring
- Easy replication

Documentation:
- README.md (overview)
- ROADMAP.md (project phases)
- DEPLOYMENT.md (step-by-step)
- ARCHITECTURE.md (technical details)
- TECH-STACK-2026.md (recommendations)
- Documentação/Bedrock/ (troubleshooting)

Status: POC validated, production-ready"

echo -e "${GREEN}✅ Commit criado${NC}"
echo ""

echo -e "${YELLOW}📋 Passo 7: Criando branch main...${NC}"
git branch -M main
echo -e "${GREEN}✅ Branch main criada${NC}"
echo ""

echo -e "${YELLOW}📋 Passo 8: Fazendo push para GitHub...${NC}"
if git push -u origin main; then
    echo -e "${GREEN}✅ Push realizado com sucesso!${NC}"
    echo ""
    echo "🎉 Projeto publicado no GitHub!"
    echo "🔗 https://github.com/bruno0nline/ai-agent-serverless-kit"
    echo ""
    echo "📝 Próximos passos:"
    echo "1. Acesse o repositório no GitHub"
    echo "2. Adicione uma descrição e topics"
    echo "3. Configure GitHub Pages (se quiser)"
    echo "4. Compartilhe com a comunidade!"
else
    echo -e "${RED}❌ Erro ao fazer push${NC}"
    echo "Verifique sua conexão e permissões"
    exit 1
fi
