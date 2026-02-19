"""
Lambda: Verificar Status de Serviço AWS
Action Group para verificar status de recursos AWS
"""

import json
import boto3
from datetime import datetime

ec2 = boto3.client('ec2')
rds = boto3.client('rds')

def lambda_handler(event, context):
    agent_params = event.get('parameters', [])
    params = {p['name']: p['value'] for p in agent_params}
    
    servico = params.get('servico', '').lower()
    recurso_id = params.get('recurso_id')
    
    if servico == 'ec2':
        result = verificar_ec2(recurso_id)
    elif servico == 'rds':
        result = verificar_rds(recurso_id)
    else:
        return format_response(False, f"Serviço {servico} não suportado")
    
    return format_response(True, "Status verificado", result)

def verificar_ec2(instance_id):
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]
        
        return {
            "instance_id": instance_id,
            "estado": instance['State']['Name'],
            "tipo": instance['InstanceType'],
            "ip_publico": instance.get('PublicIpAddress', 'N/A'),
            "zona": instance['Placement']['AvailabilityZone']
        }
    except Exception as e:
        return {"erro": str(e)}

def verificar_rds(db_id):
    try:
        response = rds.describe_db_instances(DBInstanceIdentifier=db_id)
        db = response['DBInstances'][0]
        
        return {
            "db_id": db_id,
            "estado": db['DBInstanceStatus'],
            "engine": db['Engine'],
            "classe": db['DBInstanceClass'],
            "storage": f"{db['AllocatedStorage']} GB"
        }
    except Exception as e:
        return {"erro": str(e)}

def format_response(success, message, data=None):
    return {
        "messageVersion": "1.0",
        "response": {
            "actionGroup": "VerificarStatusServico",
            "function": "verificar_status",
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
