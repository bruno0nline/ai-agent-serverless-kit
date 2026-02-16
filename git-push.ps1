# Script PowerShell para fazer push inicial do projeto para GitHub
# Uso: .\git-push.ps1

Write-Host "🚀 AI Agent Serverless Kit - Git Setup" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se está na pasta correta
if (-not (Test-Path "README.md")) {
    Write-Host "❌ Erro: README.md não encontrado" -ForegroundColor Red
    Write-Host "Execute este script na raiz do projeto" -ForegroundColor Yellow
    exit 1
}

Write-Host "📋 Passo 1: Verificando Git..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "✅ Git encontrado: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git não está instalado" -ForegroundColor Red
    exit 1
}
Write-Host ""

Write-Host "📋 Passo 2: Verificando chave SSH..." -ForegroundColor Yellow
$sshTest = ssh -T git@github.com 2>&1
if ($sshTest -match "successfully authenticated") {
    Write-Host "✅ Autenticação SSH funcionando" -ForegroundColor Green
} else {
    Write-Host "❌ Erro de autenticação SSH" -ForegroundColor Red
    Write-Host "Execute: ssh-add ~/.ssh/GitHubKey" -ForegroundColor Yellow
    exit 1
}
Write-Host ""

Write-Host "📋 Passo 3: Inicializando repositório..." -ForegroundColor Yellow
if (-not (Test-Path ".git")) {
    git init
    Write-Host "✅ Repositório inicializado" -ForegroundColor Green
} else {
    Write-Host "✅ Repositório já existe" -ForegroundColor Green
}
Write-Host ""

Write-Host "📋 Passo 4: Configurando remote..." -ForegroundColor Yellow
$remotes = git remote
if ($remotes -contains "origin") {
    Write-Host "⚠️  Remote 'origin' já existe, removendo..." -ForegroundColor Yellow
    git remote remove origin
}
git remote add origin git@github.com:bruno0nline/ai-agent-serverless-kit.git
Write-Host "✅ Remote configurado" -ForegroundColor Green
Write-Host ""

Write-Host "📋 Passo 5: Adicionando arquivos..." -ForegroundColor Yellow
git add .
Write-Host "✅ Arquivos adicionados" -ForegroundColor Green
Write-Host ""

Write-Host "📋 Passo 6: Criando commit..." -ForegroundColor Yellow
$commitMessage = @"
feat: initial commit - AI Agent Serverless Kit

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
- Low cost (`$2-12/month)

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

Status: POC validated, production-ready
"@

git commit -m $commitMessage
Write-Host "✅ Commit criado" -ForegroundColor Green
Write-Host ""

Write-Host "📋 Passo 7: Criando branch main..." -ForegroundColor Yellow
git branch -M main
Write-Host "✅ Branch main criada" -ForegroundColor Green
Write-Host ""

Write-Host "📋 Passo 8: Fazendo push para GitHub..." -ForegroundColor Yellow
try {
    git push -u origin main
    Write-Host "✅ Push realizado com sucesso!" -ForegroundColor Green
    Write-Host ""
    Write-Host "🎉 Projeto publicado no GitHub!" -ForegroundColor Cyan
    Write-Host "🔗 https://github.com/bruno0nline/ai-agent-serverless-kit" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "📝 Próximos passos:" -ForegroundColor Yellow
    Write-Host "1. Acesse o repositório no GitHub"
    Write-Host "2. Adicione uma descrição e topics"
    Write-Host "3. Configure GitHub Pages (se quiser)"
    Write-Host "4. Compartilhe com a comunidade!"
} catch {
    Write-Host "❌ Erro ao fazer push" -ForegroundColor Red
    Write-Host "Verifique sua conexão e permissões" -ForegroundColor Yellow
    Write-Host $_.Exception.Message -ForegroundColor Red
    exit 1
}
