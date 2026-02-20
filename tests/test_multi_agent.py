#!/usr/bin/env python3
"""
Testes automatizados para Multi-Agent Collaboration
Maestriacloud - AI Agent Serverless Kit
"""

import boto3
import json
import time
from datetime import datetime

# Configurações
REGION = 'us-east-1'
PROFILE = 'Master'

# IDs dos Agents (substitua pelos seus)
SUPERVISOR_AGENT_ID = 'supervisor'  # Substituir pelo ID real
SUPERVISOR_ALIAS_ID = 'TSTALIASID'  # Substituir pelo Alias ID real

# Casos de teste
TEST_CASES = [
    {
        "name": "Teste 1 - Delegação RH",
        "query": "Quantos dias de férias tenho direito?",
        "expected_agent": "Carla",
        "expected_kb": "KB-RH"
    },
    {
        "name": "Teste 2 - Delegação Vendas",
        "query": "Quais cursos de IA vocês oferecem?",
        "expected_agent": "Rafael",
        "expected_kb": "KB-Cursos"
    },
    {
        "name": "Teste 3 - Delegação Mista",
        "query": "Funcionários têm desconto nos cursos?",
        "expected_agent": "Carla + Rafael",
        "expected_kb": "KB-RH + KB-Cursos"
    },
    {
        "name": "Teste 4 - Pergunta Geral",
        "query": "Qual o horário de atendimento da empresa?",
        "expected_agent": "Patrícia",
        "expected_kb": "Nenhuma"
    }
]

def invoke_agent(bedrock_client, agent_id, alias_id, session_id, query):
    """Invoca o agent e retorna a resposta"""
    try:
        response = bedrock_client.invoke_agent(
            agentId=agent_id,
            agentAliasId=alias_id,
            sessionId=session_id,
            inputText=query
        )
        
        # Processar stream de resposta
        event_stream = response['completion']
        full_response = ""
        
        for event in event_stream:
            if 'chunk' in event:
                chunk = event['chunk']
                if 'bytes' in chunk:
                    full_response += chunk['bytes'].decode('utf-8')
        
        return full_response
    
    except Exception as e:
        return f"Erro: {str(e)}"

def run_tests():
    """Executa todos os testes"""
    print("=" * 80)
    print("TESTES MULTI-AGENT COLLABORATION - MAESTRIACLOUD")
    print("=" * 80)
    print(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Região: {REGION}")
    print(f"Profile: {PROFILE}")
    print("=" * 80)
    print()
    
    # Inicializar cliente Bedrock
    session = boto3.Session(profile_name=PROFILE, region_name=REGION)
    bedrock_client = session.client('bedrock-agent-runtime')
    
    results = []
    
    for i, test in enumerate(TEST_CASES, 1):
        print(f"[{i}/{len(TEST_CASES)}] {test['name']}")
        print(f"Query: {test['query']}")
        print(f"Agente esperado: {test['expected_agent']}")
        print(f"KB esperada: {test['expected_kb']}")
        print("-" * 80)
        
        # Gerar session ID único
        session_id = f"test-session-{int(time.time())}-{i}"
        
        # Invocar agent
        start_time = time.time()
        response = invoke_agent(
            bedrock_client,
            SUPERVISOR_AGENT_ID,
            SUPERVISOR_ALIAS_ID,
            session_id,
            test['query']
        )
        elapsed_time = time.time() - start_time
        
        print(f"Resposta ({elapsed_time:.2f}s):")
        print(response)
        print()
        print("=" * 80)
        print()
        
        results.append({
            "test": test['name'],
            "query": test['query'],
            "response": response,
            "elapsed_time": elapsed_time,
            "timestamp": datetime.now().isoformat()
        })
        
        # Aguardar entre testes para evitar throttling
        if i < len(TEST_CASES):
            time.sleep(2)
    
    # Salvar resultados
    output_file = f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Resultados salvos em: {output_file}")
    print(f"✅ Total de testes: {len(TEST_CASES)}")
    print(f"✅ Tempo total: {sum(r['elapsed_time'] for r in results):.2f}s")

if __name__ == '__main__':
    print("\n⚠️  ATENÇÃO: Este script invoca agents do Bedrock e pode gerar custos.")
    print("⚠️  Certifique-se de atualizar os IDs dos agents antes de executar.\n")
    
    response = input("Deseja continuar? (s/n): ")
    if response.lower() == 's':
        run_tests()
    else:
        print("Testes cancelados.")
