# Lambda Function: Consultar Ticket

## 📋 Descrição

Action Group para o Bedrock Agent consultar tickets em sistemas de gerenciamento.

**Caso de uso:** Consultoria de TI
- Consultar status de tickets de clientes
- Buscar histórico de atendimentos
- Verificar SLA e prioridades

---

## 🎯 Parâmetros

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| ticket_id | string | Sim | ID do ticket a consultar |
| cliente | string | Não | Nome do cliente (filtro) |

---

## 📤 Resposta

```json
{
  "success": true,
  "message": "Ticket TKT-001 encontrado com sucesso",
  "data": {
    "ticket_id": "TKT-001",
    "cliente": "Empresa XYZ",
    "titulo": "Erro no deploy da aplicação",
    "status": "Em andamento",
    "prioridade": "Alta",
    "sla": "4 horas",
    "tempo_restante": "2h 15min",
    "responsavel": "João Silva"
  }
}
```

---

## 🚀 Deploy

```bash
# Instalar dependências
pip install -r requirements.txt -t .

# Criar ZIP
zip -r function.zip .

# Deploy
aws lambda create-function \
  --function-name consultar-ticket \
  --runtime python3.11 \
  --role arn:aws:iam::ACCOUNT_ID:role/lambda-execution-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip \
  --timeout 30 \
  --memory-size 256
```

---

## 🔗 Integração com Agent

### OpenAPI Schema

```yaml
openapi: 3.0.0
info:
  title: Consultar Ticket API
  version: 1.0.0
paths:
  /consultar-ticket:
    post:
      summary: Consulta informações de um ticket
      operationId: consultar_ticket
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                ticket_id:
                  type: string
                  description: ID do ticket
                cliente:
                  type: string
                  description: Nome do cliente (opcional)
              required:
                - ticket_id
      responses:
        '200':
          description: Ticket encontrado
```

---

## 🧪 Testes

```bash
# Teste local
python -c "
import lambda_function
event = {
    'parameters': [
        {'name': 'ticket_id', 'value': 'TKT-001'}
    ]
}
result = lambda_function.lambda_handler(event, None)
print(result)
"
```

---

## 🔧 Configuração

### Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| TICKETS_TABLE | Nome da tabela DynamoDB | tickets-table |

### Permissões IAM

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:Query"
      ],
      "Resource": "arn:aws:dynamodb:*:*:table/tickets-table"
    }
  ]
}
```

---

## 📝 Notas

- Atualmente usa dados mockados para POC
- Em produção, integrar com sistema real (Jira, ServiceNow, etc)
- Considerar cache para reduzir latência
- Implementar retry logic para APIs externas
