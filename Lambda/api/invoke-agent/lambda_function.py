"""
Lambda: Invoke Agent API
API Gateway endpoint para invocar o Bedrock Agent
"""

import json
import boto3
import os
import uuid

bedrock_agent = boto3.client('bedrock-agent-runtime')

AGENT_ID = os.environ.get('AGENT_ID')
AGENT_ALIAS_ID = os.environ.get('AGENT_ALIAS_ID', 'TSTALIASID')

def lambda_handler(event, context):
    """
    Endpoint HTTP para invocar o Agent
    
    POST /invoke
    {
        "message": "Qual o status do ticket TKT-001?",
        "session_id": "optional-session-id"
    }
    """
    
    # CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS'
    }
    
    # Handle OPTIONS (preflight)
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }
    
    try:
        # Parse body
        body = json.loads(event.get('body', '{}'))
        message = body.get('message')
        session_id = body.get('session_id', str(uuid.uuid4()))
        
        if not message:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'message é obrigatório'})
            }
        
        # Invocar Agent
        response = bedrock_agent.invoke_agent(
            agentId=AGENT_ID,
            agentAliasId=AGENT_ALIAS_ID,
            sessionId=session_id,
            inputText=message
        )
        
        # Extrair resposta
        agent_response = ""
        for event_chunk in response['completion']:
            if 'chunk' in event_chunk:
                chunk = event_chunk['chunk']
                if 'bytes' in chunk:
                    agent_response += chunk['bytes'].decode('utf-8')
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'response': agent_response,
                'session_id': session_id
            }, ensure_ascii=False)
        }
        
    except Exception as e:
        print(f"Erro: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }
