"""
Lambda: Criar Ticket
Action Group para criar tickets em sistemas de gerenciamento
"""

import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    agent_params = event.get('parameters', [])
    params = {p['name']: p['value'] for p in agent_params}
    
    titulo = params.get('titulo')
    descricao = params.get('descricao')
    cliente = params.get('cliente')
    prioridade = params.get('prioridade', 'Média')
    
    if not titulo or not descricao:
        return format_response(False, "Título e descrição são obrigatórios")
    
    # Criar ticket
    ticket_id = f"TKT-{str(uuid.uuid4())[:8].upper()}"
    
    ticket = {
        "ticket_id": ticket_id,
        "titulo": titulo,
        "descricao": descricao,
        "cliente": cliente,
        "prioridade": prioridade,
        "status": "Novo",
        "criado_em": datetime.now().isoformat(),
        "criado_por": "AI Agent"
    }
    
    # Em produção: salvar no DynamoDB ou API externa
    # table = dynamodb.Table('tickets-table')
    # table.put_item(Item=ticket)
    
    return format_response(
        True,
        f"Ticket {ticket_id} criado com sucesso",
        ticket
    )

def format_response(success, message, data=None):
    return {
        "messageVersion": "1.0",
        "response": {
            "actionGroup": "CriarTicket",
            "function": "criar_ticket",
            "functionResponse": {
                "responseState": "SUCCESS" if success else "FAILURE",
                "responseBody": {
                    "TEXT": {
                        "body": json.dumps({
                            "success": success,
                            "message": message,
                            "data": data
                        }, ensure_ascii=False)
                    }
                }
            }
        }
    }
