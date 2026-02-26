#!/bin/bash

# Script para criar a Lambda Function
# Execute apenas quando autorizado!

REGION="us-east-1"
PROFILE="Master"
FUNCTION_NAME="query-order-status"
ROLE_NAME="lambda-dynamodb-role"

echo "=========================================="
echo "Deploy da Lambda Function"
echo "=========================================="
echo ""

# 1. Criar role IAM para Lambda
echo "1. Criando role IAM..."
cat > trust-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

aws iam create-role \
    --role-name $ROLE_NAME \
    --assume-role-policy-document file://trust-policy.json \
    --profile $PROFILE

# 2. Anexar políticas necessárias
echo "2. Anexando políticas..."
aws iam attach-role-policy \
    --role-name $ROLE_NAME \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole \
    --profile $PROFILE

aws iam attach-role-policy \
    --role-name $ROLE_NAME \
    --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess \
    --profile $PROFILE

echo "Aguardando role propagar..."
sleep 10

# 3. Criar pacote de deploy
echo "3. Criando pacote de deploy..."
zip lambda-package.zip lambda_function.py

# 4. Criar Lambda Function
echo "4. Criando Lambda Function..."
ROLE_ARN=$(aws iam get-role --role-name $ROLE_NAME --profile $PROFILE --query 'Role.Arn' --output text)

aws lambda create-function \
    --function-name $FUNCTION_NAME \
    --runtime python3.12 \
    --role $ROLE_ARN \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://lambda-package.zip \
    --timeout 30 \
    --memory-size 256 \
    --region $REGION \
    --profile $PROFILE

echo ""
echo "=========================================="
echo "✅ Lambda criada com sucesso!"
echo "ARN: $(aws lambda get-function --function-name $FUNCTION_NAME --region $REGION --profile $PROFILE --query 'Configuration.FunctionArn' --output text)"
echo "=========================================="
