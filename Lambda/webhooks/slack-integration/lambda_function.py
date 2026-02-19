"""
Lambda: Integração Slack
Webhook para receber mensagens do Slack e invocar o Agent
"""

import json
import boto3
import os

bedrock_agent = boto3.client('bedrock-agent-runtime')

AGENT_ID = os.environ.get('AGENT_ID')
AGENT_ALIAS_ID = os.environ.get('AGENT_ALIAS_ID', 'TSTALIASID')

def lambda_handler(event, context):
    """
    Recebe evento do Slack e invoca o Bedrock Agent
    """
    
    # Parse do body do Slack
    body = json.loads(event.get('body', '{}'))
    
    # Verificação de URL do Slack (challenge)
    if 'challenge' in body:
        return {
            'statusCode': 200,
            'body': json.dumps({'challenge': body['challenge']})
        }
    
    # Extrair mensagem do Slack
    slack_event = body.get('event', {})
    user_message = slack_event.get('text', '')
    channel = slack_event.get('channel')
    user = slack_event.get('user')
    
    # Ignorar mensagens do bot
    if slack_event.get('bot_id'):
        return {'statusCode': 200, 'body': 'OK'}
    
    # Invocar Bedrock Agent
    try:
        response = bedrock_agent.invoke_agent(
            agentId=AGENT_ID,
            agentAliasId=AGENT_ALIAS_ID,
            sessionId=f"slack-{channel}-{user}",
            inputText=user_message
        )
        
        # Extrair resposta do Agent
        agent_response = ""
        for event in response['completion']:
            if 'chunk' in event:
                chunk = event['chunk']
                if 'bytes' in chunk:
                    agent_response += chunk['bytes'].decode('utf-8')
        
        # Enviar resposta de volta ao Slack
        send_slack_message(channel, agent_response)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Processado com sucesso'})
        }
        
    except Exception as e:
        print(f"Erro ao invocar agent: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def send_slack_message(channel, text):
    """
    Envia mensagem para o Slack
    Requer configuração do Slack Bot Token
    """
    # Implementar usando Slack SDK ou requests
    # slack_client.chat_postMessage(channel=channel, text=text)
    pass
