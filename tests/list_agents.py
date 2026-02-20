#!/usr/bin/env python3
"""
Script para listar IDs dos Agents e Knowledge Bases
Maestriacloud - AI Agent Serverless Kit
"""

import boto3
import json

REGION = 'us-east-1'
PROFILE = 'Master'

def list_agents():
    """Lista todos os agents"""
    session = boto3.Session(profile_name=PROFILE, region_name=REGION)
    bedrock_client = session.client('bedrock-agent')
    
    print("=" * 80)
    print("AGENTS DISPONÍVEIS")
    print("=" * 80)
    
    try:
        response = bedrock_client.list_agents()
        
        for agent in response.get('agentSummaries', []):
            print(f"\nNome: {agent['agentName']}")
            print(f"Agent ID: {agent['agentId']}")
            print(f"Status: {agent['agentStatus']}")
            print(f"Atualizado: {agent['updatedAt']}")
            
            # Listar aliases
            aliases = bedrock_client.list_agent_aliases(agentId=agent['agentId'])
            print("Aliases:")
            for alias in aliases.get('agentAliasSummaries', []):
                print(f"  - {alias['agentAliasName']}: {alias['agentAliasId']}")
            
            print("-" * 80)
    
    except Exception as e:
        print(f"Erro ao listar agents: {e}")

def list_knowledge_bases():
    """Lista todas as knowledge bases"""
    session = boto3.Session(profile_name=PROFILE, region_name=REGION)
    bedrock_client = session.client('bedrock-agent')
    
    print("\n" + "=" * 80)
    print("KNOWLEDGE BASES DISPONÍVEIS")
    print("=" * 80)
    
    try:
        response = bedrock_client.list_knowledge_bases()
        
        for kb in response.get('knowledgeBaseSummaries', []):
            print(f"\nNome: {kb['name']}")
            print(f"KB ID: {kb['knowledgeBaseId']}")
            print(f"Status: {kb['status']}")
            print(f"Atualizado: {kb['updatedAt']}")
            print("-" * 80)
    
    except Exception as e:
        print(f"Erro ao listar knowledge bases: {e}")

def export_config():
    """Exporta configuração para arquivo JSON"""
    session = boto3.Session(profile_name=PROFILE, region_name=REGION)
    bedrock_client = session.client('bedrock-agent')
    
    config = {
        "agents": [],
        "knowledge_bases": []
    }
    
    # Agents
    try:
        response = bedrock_client.list_agents()
        for agent in response.get('agentSummaries', []):
            aliases = bedrock_client.list_agent_aliases(agentId=agent['agentId'])
            config['agents'].append({
                "name": agent['agentName'],
                "id": agent['agentId'],
                "status": agent['agentStatus'],
                "aliases": [
                    {"name": a['agentAliasName'], "id": a['agentAliasId']}
                    for a in aliases.get('agentAliasSummaries', [])
                ]
            })
    except Exception as e:
        print(f"Erro ao exportar agents: {e}")
    
    # Knowledge Bases
    try:
        response = bedrock_client.list_knowledge_bases()
        for kb in response.get('knowledgeBaseSummaries', []):
            config['knowledge_bases'].append({
                "name": kb['name'],
                "id": kb['knowledgeBaseId'],
                "status": kb['status']
            })
    except Exception as e:
        print(f"Erro ao exportar knowledge bases: {e}")
    
    # Salvar
    output_file = "bedrock_config.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"\n✅ Configuração exportada para: {output_file}")

if __name__ == '__main__':
    list_agents()
    list_knowledge_bases()
    export_config()
