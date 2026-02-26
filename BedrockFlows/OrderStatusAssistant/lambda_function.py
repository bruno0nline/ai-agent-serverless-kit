import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VeganSweetOrders')

def lambda_handler(event, context):
    try:
        print(f"Evento recebido: {json.dumps(event)}")
        
        # Extrai order_id do evento (suporta múltiplos formatos)
        order_id = None
        
        # Formato 1: Direto no evento (teste simples)
        if 'order_id' in event:
            order_id = event['order_id']
            print(f"Order ID extraído do formato simples: {order_id}")
        
        # Formato 2: Bedrock Flow (node.inputs)
        elif 'node' in event and 'inputs' in event['node']:
            for input_item in event['node']['inputs']:
                if input_item.get('name') == 'codeHookInput':
                    order_id = input_item.get('value')
                    print(f"Order ID extraído do Bedrock Flow: {order_id}")
                    break
        
        # Formato 3: Bedrock Flow alternativo (fields)
        elif 'fields' in event and len(event['fields']) > 0:
            content = event['fields'][0].get('content', {})
            order_id = content.get('document')
            print(f"Order ID extraído do Bedrock Flow (fields): {order_id}")
        
        if not order_id:
            print("Order ID não encontrado no evento")
            return "Unknown"
        
        # Consulta o pedido no DynamoDB
        response = table.get_item(Key={'order_id': order_id})
        print(f"Resposta do DynamoDB: {response}")
        
        # Verifica se o pedido existe
        if 'Item' not in response:
            print("Pedido não encontrado no DynamoDB")
            return "Unknown"
        
        # Retorna apenas o status como string
        status = str(response['Item']['status'])
        print(f"Status retornado: {status}")
        return status
        
    except Exception as e:
        print(f"Erro: {str(e)}")
        return "Unknown"
