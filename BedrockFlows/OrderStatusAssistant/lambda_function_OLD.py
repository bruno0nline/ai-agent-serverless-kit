import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VeganSweetOrders')

def lambda_handler(event, context):
    """
    Lambda para consultar status de pedido no DynamoDB
    Integrada com Bedrock Flows
    """
    
    # Extrair order_id do evento do Bedrock Flow
    order_id = event.get('order_id', '')
    
    if not order_id:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'order_id é obrigatório',
                'status': 'error'
            })
        }
    
    try:
        # Consultar pedido no DynamoDB
        response = table.get_item(Key={'order_id': order_id})
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({
                    'message': f'Pedido {order_id} não encontrado',
                    'status': 'not_found'
                })
            }
        
        item = response['Item']
        
        # Converter Decimal para tipos nativos
        def decimal_default(obj):
            if isinstance(obj, Decimal):
                return float(obj)
            raise TypeError
        
        # Retornar dados do pedido
        return {
            'statusCode': 200,
            'body': json.dumps({
                'order_id': item['order_id'],
                'customer_id': item['customer_id'],
                'description': item['description'],
                'order_date': item['order_date'],
                'rating': int(item['rating']),
                'status': item['status'],
                'message': f'Pedido encontrado com status: {item["status"]}'
            }, default=decimal_default)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f'Erro ao consultar pedido: {str(e)}',
                'status': 'error'
            })
        }
