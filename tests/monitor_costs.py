#!/usr/bin/env python3
"""
Script para monitorar custos do AWS Bedrock
Maestriacloud - AI Agent Serverless Kit
"""

import boto3
import json
from datetime import datetime, timedelta

REGION = 'us-east-1'
PROFILE = 'Master'

def get_bedrock_costs(start_date, end_date):
    """Obtém custos do Bedrock no período"""
    session = boto3.Session(profile_name=PROFILE, region_name=REGION)
    ce_client = session.client('ce', region_name='us-east-1')  # Cost Explorer é global
    
    try:
        response = ce_client.get_cost_and_usage(
            TimePeriod={
                'Start': start_date.strftime('%Y-%m-%d'),
                'End': end_date.strftime('%Y-%m-%d')
            },
            Granularity='DAILY',
            Metrics=['UnblendedCost'],
            Filter={
                'Dimensions': {
                    'Key': 'SERVICE',
                    'Values': ['Amazon Bedrock']
                }
            }
        )
        
        return response['ResultsByTime']
    
    except Exception as e:
        print(f"Erro ao obter custos: {e}")
        return []

def format_cost_report(results):
    """Formata relatório de custos"""
    print("=" * 80)
    print("RELATÓRIO DE CUSTOS - AMAZON BEDROCK")
    print("=" * 80)
    print(f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print()
    
    total_cost = 0.0
    
    for result in results:
        date = result['TimePeriod']['Start']
        amount = float(result['Total']['UnblendedCost']['Amount'])
        total_cost += amount
        
        if amount > 0:
            print(f"{date}: ${amount:.4f}")
    
    print("-" * 80)
    print(f"TOTAL: ${total_cost:.4f}")
    print("=" * 80)
    
    return total_cost

def estimate_monthly_cost(daily_avg):
    """Estima custo mensal baseado na média diária"""
    monthly = daily_avg * 30
    
    print("\n" + "=" * 80)
    print("PROJEÇÃO DE CUSTOS")
    print("=" * 80)
    print(f"Média diária: ${daily_avg:.4f}")
    print(f"Projeção mensal (30 dias): ${monthly:.2f}")
    print("=" * 80)

def save_cost_report(results, filename="cost_report.json"):
    """Salva relatório em JSON"""
    report = {
        "generated_at": datetime.now().isoformat(),
        "service": "Amazon Bedrock",
        "region": REGION,
        "costs": []
    }
    
    total = 0.0
    for result in results:
        cost = float(result['Total']['UnblendedCost']['Amount'])
        total += cost
        report['costs'].append({
            "date": result['TimePeriod']['Start'],
            "amount": cost
        })
    
    report['total'] = total
    report['average_daily'] = total / len(results) if results else 0
    report['projected_monthly'] = report['average_daily'] * 30
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Relatório salvo em: {filename}")

def main():
    """Função principal"""
    # Últimos 7 dias
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    print(f"Consultando custos de {start_date.strftime('%Y-%m-%d')} a {end_date.strftime('%Y-%m-%d')}...")
    print()
    
    results = get_bedrock_costs(start_date, end_date)
    
    if results:
        total = format_cost_report(results)
        daily_avg = total / len(results) if results else 0
        estimate_monthly_cost(daily_avg)
        save_cost_report(results)
    else:
        print("⚠️  Nenhum custo encontrado no período.")
        print("Isso pode significar:")
        print("  - Ainda não há custos registrados")
        print("  - Os custos ainda não foram processados pela AWS")
        print("  - Você não tem permissão para acessar Cost Explorer")

if __name__ == '__main__':
    main()
