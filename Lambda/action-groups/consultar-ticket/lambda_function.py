"""
Lambda Function: Consultar Ticket
Action Group para o Bedrock Agent consultar tickets em sistemas externos

Caso de uso: Consultoria de TI
- Consultar status de tickets de clientes
- Buscar histórico de atendimentos
- Verificar SLA e prioridades
"""

import json
import boto3
import os
from datetime import datetime

# Cliente DynamoDB (exemplo - pode ser substituído por API externa)
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TICKETS_TABLE', 'tickets-table')

def lambda_handler(event, context):
    """
    Handler principal da Lambda
    
    Parâmetros esperados do Agent:
    - ticket_id: ID do ticket a consultar
    - cliente: Nome do cliente (opcional)
    """
    
    print(f"Event recebido: {json.dumps(event)}")
    
    # Extrair parâmetros do Agent
    agent_params = event.get('parameters', [])
    params = {p['name']: p['value'] for p in agent_params}
    
    ticket_id = params.get('ticket_id')
    cliente = params.get('cliente')
    
    if not ticket_id:
        return format_response(
            success=False,
            message="ticket_id é obrigatório"
        )
    
    try:
        # Consultar ticket (exemplo com DynamoDB)
        ticket = consultar_ticket_dynamodb(ticket_id)
        
        if not ticket:
            return format_response(
                success=False,
                message=f"Ticket {ticket_id} não encontrado"
            )
        
        # Filtrar por cliente se especificado
        if cliente and ticket.get('cliente') != cliente:
            return format_response(
                success=False,
                message=f"Ticket {ticket_id} não pertence ao cliente {cliente}"
            )
        
        # Formatar resposta para o Agent
        return format_response(
            success=True,
            data=ticket,
            message=f"Ticket {ticket_id} encontrado com sucesso"
        )
        
    except Exception as e:
        print(f"Erro ao consultar ticket: {str(e)}")
        return format_response(
            success=False,
            message=f"Erro ao consultar ticket: {str(e)}"
        )

def consultar_ticket_dynamodb(ticket_id):
    """
    Consulta ticket no DynamoDB
    
    Em produção, substituir por:
    - API do sistema de tickets (Jira, ServiceNow, etc)
    - Banco de dados relacional (RDS)
    - Outro sistema de gerenciamento
    """
    
    # Exemplo de dados mockados para POC
    # Em produção, fazer query real no DynamoDB ou API externa
    tickets_mock = {
        "TKT-001": {
            "ticket_id": "TKT-001",
            "cliente": "Empresa XYZ",
            "titulo": "Erro no deploy da aplicação",
            "descricao": "Aplicação não está subindo após deploy",
            "status": "Em andamento",
            "prioridade": "Alta",
            "sla": "4 horas",
            "tempo_restante": "2h 15min",
            "responsavel": "João Silva",
            "criado_em": "2026-02-16 09:00:00",
            "atualizado_em": "2026-02-16 10:30:00"
        },
        "TKT-002": {
            "ticket_id": "TKT-002",
            "cliente": "Empresa ABC",
            "titulo": "Solicitação de aumento de recursos",
            "descricao": "Aumentar capacidade do RDS",
            "status": "Aguardando aprovação",
            "prioridade": "Média",
            "sla": "24 horas",
            "tempo_restante": "18h 45min",
            "responsavel": "Maria Santos",
            "criado_em": "2026-02-15 14:00:00",
            "atualizado_em": "2026-02-15 16:00:00"
        }
    }
    
    return tickets_mock.get(ticket_id)

def format_response(success, message, data=None):
    """
    Formata resposta no formato esperado pelo Bedrock Agent
    """
    response = {
        "messageVersion": "1.0",
        "response": {
            "actionGroup": "ConsultarTicket",
            "function": "consultar_ticket",
            "functionResponse": {
                "responseState": "SUCCESS" if success else "FAILURE",
                "responseBody": {
                    "TEXT": {
                        "body": json.dumps({
                            "success": success,
                            "message": message,
                            "data": data,
                            "timestamp": datetime.now().isoformat()
                        }, ensure_ascii=False)
                    }
                }
            }
        }
    }
    
    return response
