#!/usr/bin/env python3
"""
Script para backup completo da configuração dos Agents e Knowledge Bases
Maestriacloud - AI Agent Serverless Kit
"""

import boto3
import json
import os
from datetime import datetime

REGION = 'us-east-1'
PROFILE = 'Master'
BACKUP_DIR = 'backup'

def ensure_backup_dir():
    """Garante que o diretório de backup existe"""
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

def backup_agent(bedrock_client, agent_id, agent_name):
    """Faz backup de um agent específico"""
    try:
        # Obter detalhes do agent
        agent_details = bedrock_client.get_agent(agentId=agent_id)
        
        # Obter aliases
        aliases = bedrock_client.list_agent_aliases(agentId=agent_id)
        
        # Obter action groups
        action_groups = bedrock_client.list_agent_action_groups(
            agentId=agent_id,
            agentVersion='DRAFT'
        )
        
        # Obter knowledge bases associadas
        kb_associations = bedrock_client.list_agent_knowledge_bases(
            agentId=agent_id,
            agentVersion='DRAFT'
        )
        
        backup_data = {
            "agent": agent_details['agent'],
            "aliases": aliases.get('agentAliasSummaries', []),
            "action_groups": action_groups.get('actionGroupSummaries', []),
            "knowledge_bases": kb_associations.get('agentKnowledgeBaseSummaries', []),
            "backup_timestamp": datetime.now().isoformat()
        }
        
        # Salvar
        filename = f"{BACKUP_DIR}/agent_{agent_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(backup_data, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"✅ Agent '{agent_name}' backup salvo: {filename}")
        return filename
    
    except Exception as e:
        print(f"❌ Erro ao fazer backup do agent '{agent_name}': {e}")
        return None

def backup_knowledge_base(bedrock_client, kb_id, kb_name):
    """Faz backup de uma knowledge base"""
    try:
        # Obter detalhes da KB
        kb_details = bedrock_client.get_knowledge_base(knowledgeBaseId=kb_id)
        
        # Obter data sources
        data_sources = bedrock_client.list_data_sources(knowledgeBaseId=kb_id)
        
        backup_data = {
            "knowledge_base": kb_details['knowledgeBase'],
            "data_sources": data_sources.get('dataSourceSummaries', []),
            "backup_timestamp": datetime.now().isoformat()
        }
        
        # Salvar
        filename = f"{BACKUP_DIR}/kb_{kb_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(backup_data, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"✅ Knowledge Base '{kb_name}' backup salvo: {filename}")
        return filename
    
    except Exception as e:
        print(f"❌ Erro ao fazer backup da KB '{kb_name}': {e}")
        return None

def backup_all():
    """Faz backup de todos os agents e knowledge bases"""
    print("=" * 80)
    print("BACKUP DE CONFIGURAÇÃO - BEDROCK AGENTS & KNOWLEDGE BASES")
    print("=" * 80)
    print(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Região: {REGION}")
    print(f"Profile: {PROFILE}")
    print("=" * 80)
    print()
    
    ensure_backup_dir()
    
    session = boto3.Session(profile_name=PROFILE, region_name=REGION)
    bedrock_client = session.client('bedrock-agent')
    
    backup_summary = {
        "timestamp": datetime.now().isoformat(),
        "region": REGION,
        "agents": [],
        "knowledge_bases": []
    }
    
    # Backup de Agents
    print("📦 Fazendo backup dos Agents...")
    try:
        agents_response = bedrock_client.list_agents()
        for agent in agents_response.get('agentSummaries', []):
            filename = backup_agent(bedrock_client, agent['agentId'], agent['agentName'])
            if filename:
                backup_summary['agents'].append({
                    "name": agent['agentName'],
                    "id": agent['agentId'],
                    "backup_file": filename
                })
    except Exception as e:
        print(f"❌ Erro ao listar agents: {e}")
    
    print()
    
    # Backup de Knowledge Bases
    print("📦 Fazendo backup das Knowledge Bases...")
    try:
        kb_response = bedrock_client.list_knowledge_bases()
        for kb in kb_response.get('knowledgeBaseSummaries', []):
            filename = backup_knowledge_base(bedrock_client, kb['knowledgeBaseId'], kb['name'])
            if filename:
                backup_summary['knowledge_bases'].append({
                    "name": kb['name'],
                    "id": kb['knowledgeBaseId'],
                    "backup_file": filename
                })
    except Exception as e:
        print(f"❌ Erro ao listar knowledge bases: {e}")
    
    # Salvar sumário
    summary_file = f"{BACKUP_DIR}/backup_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(backup_summary, f, indent=2, ensure_ascii=False)
    
    print()
    print("=" * 80)
    print("RESUMO DO BACKUP")
    print("=" * 80)
    print(f"Agents: {len(backup_summary['agents'])}")
    print(f"Knowledge Bases: {len(backup_summary['knowledge_bases'])}")
    print(f"Sumário salvo em: {summary_file}")
    print("=" * 80)

if __name__ == '__main__':
    backup_all()
