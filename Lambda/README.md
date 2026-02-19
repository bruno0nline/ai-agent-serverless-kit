# Lambda Functions - AI Agent Solution

## 📋 Visão Geral

Este diretório contém todas as Lambda functions usadas na solução de Agente de IA para consultoria de TI.

---

## 🎯 Casos de Uso

### 1. Action Groups (Integração com Agent)
Lambda functions que o Agent pode chamar para executar ações específicas:
- Consultar sistemas externos (tickets, documentação, status)
- Executar operações em bancos de dados
- Integrar com APIs de terceiros
- Processar dados em tempo real

### 2. Processamento de Documentos
Lambda functions para preparar documentos antes de irem para a Knowledge Base:
- Converter formatos (PDF → Markdown)
- Extrair metadados
- Limpar e formatar texto
- Dividir documentos grandes

### 3. Webhooks e Eventos
Lambda functions acionadas por eventos:
- Receber mensagens do Slack/Teams
- Processar uploads no S3
- Responder a eventos do EventBridge
- Integrar com sistemas de ticketing

### 4. APIs Customizadas
Lambda functions expostas via API Gateway:
- Endpoint para invocar o Agent
- APIs de gerenciamento
- Webhooks para integrações
- Health checks

---

## 📁 Estrutura

```
Lambda/
├── action-groups/          # Functions para Action Groups
├── document-processing/    # Processamento de documentos
├── webhooks/              # Webhooks e integrações
├── api/                   # APIs customizadas
└── shared/                # Código compartilhado
```

---

## 🚀 Tecnologias

- **Runtime:** Python 3.11
- **Framework:** AWS Lambda
- **IaC:** AWS SAM / CDK
- **Testes:** pytest
- **CI/CD:** GitHub Actions

---

## 📖 Documentação

Ver README.md em cada subdiretório para detalhes específicos.
