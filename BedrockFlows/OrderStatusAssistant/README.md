# OrderStatusAssistant - Bedrock Flow

Fluxo do Bedrock para consultar status de pedidos no DynamoDB.

## 📁 Estrutura do Projeto

```
OrderStatusAssistant/
├── lambda_function.py              # Lambda para consultar DynamoDB
├── sample-orders.json              # Dados de exemplo (10 pedidos)
├── deploy-dynamodb.sh              # Script para criar tabela
├── deploy-lambda.sh                # Script para criar Lambda
├── test-events/                    # Eventos de teste
│   ├── test-delivered.json         # Pedido entregue
│   ├── test-cancelled.json         # Pedido cancelado
│   ├── test-shipped.json           # Pedido enviado
│   └── test-processing.json        # Pedido em processamento
└── README.md                       # Este arquivo
```

## 🎯 Objetivo

Demonstrar como o Bedrock Flow pode:
1. Receber um `order_id` como input
2. Chamar uma Lambda Function
3. Lambda consulta DynamoDB
4. Retornar status do pedido formatado

## 📊 Estrutura da Tabela DynamoDB

**Nome:** `VeganSweetOrders`

**Schema:**
- `order_id` (String, Partition Key) - ID único do pedido
- `customer_id` (Number) - ID do cliente
- `description` (String) - Descrição do produto
- `order_date` (String) - Data do pedido (YYYY-MM-DD)
- `rating` (Number) - Avaliação (1-5)
- `status` (String) - Status do pedido

**Status possíveis:**
- `Delivered` - Entregue
- `Shipped` - Enviado
- `Processing` - Em processamento
- `Cancelled` - Cancelado

## 🚀 Deploy (quando autorizado)

### 1. Criar tabela DynamoDB e popular dados

```bash
cd /home/bruno/AI/BedrockFlows/OrderStatusAssistant
chmod +x deploy-dynamodb.sh
./deploy-dynamodb.sh
```

### 2. Criar Lambda Function

```bash
chmod +x deploy-lambda.sh
./deploy-lambda.sh
```

### 3. Configurar Bedrock Flow

No console do Bedrock Flows:

1. **Flow Input Node:**
   - Output: `document` (String)

2. **Lambda Function Node:**
   - Nome: `LambdaFunctionNode_1`
   - Lambda: `query-order-status`
   - Input: `codeHookInput` → mapear `order_id` do Flow Input
   - Output: `functionResponse` (String)

3. **Prompt Node:**
   - Nome: `Prompt_1`
   - Input: `status` → mapear `functionResponse` da Lambda
   - Prompt: Formatar resposta amigável
   - Output: `modelCompletion` (String)

4. **Flow Output Node:**
   - Input: `document` → mapear `modelCompletion` do Prompt
   - Output: Resposta final

## 🧪 Testar Lambda Localmente

```bash
# Testar pedido entregue
aws lambda invoke \
    --function-name query-order-status \
    --payload file://test-events/test-delivered.json \
    --region us-east-1 \
    --profile Master \
    response.json

cat response.json | jq
```

## 📝 Exemplo de Resposta

**Input:**
```json
{
  "order_id": "e97c7827-7f6c-4fd0-9e84-61a7ad836b6c"
}
```

**Output da Lambda:**
```json
{
  "statusCode": 200,
  "body": {
    "order_id": "e97c7827-7f6c-4fd0-9e84-61a7ad836b6c",
    "customer_id": 1255,
    "description": "Almond caramel delight",
    "order_date": "2025-09-11",
    "rating": 4,
    "status": "Delivered",
    "message": "Pedido encontrado com status: Delivered"
  }
}
```

## 🎨 Configuração do Prompt Node

```
Você é um assistente de atendimento da VeganSweet, uma loja de doces veganos.

Com base nas informações do pedido abaixo, forneça uma resposta amigável ao cliente:

{{status}}

Seja educado, claro e objetivo. Se o pedido foi entregue, agradeça pela compra.
Se foi cancelado, ofereça ajuda. Se está em processamento ou enviado, informe o status atual.
```

## 💰 Custos Estimados

- **DynamoDB:** PAY_PER_REQUEST (sem custo fixo)
- **Lambda:** 256MB, ~100ms por execução
- **Bedrock Flow:** ~$0.01 por execução

**Total para 100 consultas/mês:** ~$0.50

## 🔗 IDs de Teste

Use estes IDs para testar diferentes status:

- **Delivered:** `e97c7827-7f6c-4fd0-9e84-61a7ad836b6c`
- **Cancelled:** `f0e74f98-1c76-47fe-9975-240c6becf7d4`
- **Shipped:** `155acd09-61d6-46a0-9fb6-8be1e4441bff`
- **Processing:** `55f33cff-2686-4a9b-ab45-e0ab18951d0f`

## 📚 Próximos Passos

1. ✅ Criar arquivos do projeto
2. ⏳ Deploy DynamoDB (aguardando autorização)
3. ⏳ Deploy Lambda (aguardando autorização)
4. ⏳ Configurar Bedrock Flow
5. ⏳ Testar fluxo completo
6. ⏳ Adicionar mais funcionalidades (atualizar status, cancelar pedido, etc)

---

**Última atualização:** 25/02/2026
