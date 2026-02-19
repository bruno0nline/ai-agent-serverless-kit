# Guia de Integração - Lambda com Bedrock Agent

## 📋 Visão Geral

Como integrar Lambda functions com Bedrock Agent usando Action Groups.

---

## 🔧 Passo a Passo

### 1. Deploy da Lambda

```bash
cd Lambda/action-groups/consultar-ticket
pip install -r requirements.txt -t .
zip -r function.zip .

aws lambda create-function \
  --function-name consultar-ticket \
  --runtime python3.11 \
  --role arn:aws:iam::ACCOUNT_ID:role/lambda-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip
```

### 2. Permissão para o Agent

```bash
aws lambda add-permission \
  --function-name consultar-ticket \
  --statement-id bedrock-agent \
  --action lambda:InvokeFunction \
  --principal bedrock.amazonaws.com
```

### 3. Criar Action Group no Agent

Via Console:
1. Bedrock → Agents → Seu Agent
2. Action Groups → Add
3. Nome: ConsultarTicket
4. Lambda: consultar-ticket
5. Upload OpenAPI schema
6. Save

---

## 📝 OpenAPI Schema Exemplo

```yaml
openapi: 3.0.0
info:
  title: Consultar Ticket
  version: 1.0.0
paths:
  /consultar-ticket:
    post:
      operationId: consultar_ticket
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                ticket_id:
                  type: string
              required:
                - ticket_id
```

---

## 🧪 Testar

Perguntar ao Agent:
- "Qual o status do ticket TKT-001?"
- "Me mostre informações do ticket TKT-002"

O Agent vai automaticamente chamar a Lambda!
