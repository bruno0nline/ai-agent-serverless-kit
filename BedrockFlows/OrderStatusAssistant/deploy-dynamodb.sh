#!/bin/bash

# Script para criar e popular a tabela DynamoDB
# Execute apenas quando autorizado!

REGION="us-east-1"
PROFILE="Master"
TABLE_NAME="VeganSweetOrders"

echo "=========================================="
echo "Deploy do OrderStatusAssistant - DynamoDB"
echo "=========================================="
echo ""

# 1. Criar tabela DynamoDB
echo "1. Criando tabela $TABLE_NAME..."
aws dynamodb create-table \
    --table-name $TABLE_NAME \
    --attribute-definitions AttributeName=order_id,AttributeType=S \
    --key-schema AttributeName=order_id,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --region $REGION \
    --profile $PROFILE

echo "Aguardando tabela ficar ativa..."
aws dynamodb wait table-exists \
    --table-name $TABLE_NAME \
    --region $REGION \
    --profile $PROFILE

echo "✅ Tabela criada com sucesso!"
echo ""

# 2. Popular tabela com dados de exemplo
echo "2. Populando tabela com dados de exemplo..."
aws dynamodb batch-write-item \
    --request-items file://sample-orders.json \
    --region $REGION \
    --profile $PROFILE

echo "✅ Dados inseridos com sucesso!"
echo ""

# 3. Verificar dados
echo "3. Verificando dados inseridos..."
aws dynamodb scan \
    --table-name $TABLE_NAME \
    --region $REGION \
    --profile $PROFILE \
    --query "Items[*].[order_id.S, status.S]" \
    --output table

echo ""
echo "=========================================="
echo "✅ Deploy concluído!"
echo "=========================================="
