# 🧪 Scripts de Teste e Monitoramento

Scripts Python para testar, monitorar e fazer backup dos Agents e Knowledge Bases do AWS Bedrock.

---

## 📋 Scripts Disponíveis

### 1. `list_agents.py` - Listar Agents e Knowledge Bases

Lista todos os agents e knowledge bases configurados, incluindo IDs e aliases.

**Uso:**
```bash
python3 list_agents.py
```

**Saída:**
- Lista de agents com IDs e aliases
- Lista de knowledge bases com IDs
- Arquivo `bedrock_config.json` com configuração exportada

**Custo:** ❌ Nenhum (apenas leitura)

---

### 2. `test_multi_agent.py` - Testes Multi-Agent

Executa testes automatizados para validar a orquestração multi-agent.

**Casos de teste:**
1. Delegação RH (Carla)
2. Delegação Vendas (Rafael)
3. Delegação Mista (Carla + Rafael)
4. Pergunta Geral (Patrícia)

**Uso:**
```bash
python3 test_multi_agent.py
```

**⚠️ IMPORTANTE:**
- Edite o script e substitua `SUPERVISOR_AGENT_ID` e `SUPERVISOR_ALIAS_ID` pelos IDs reais
- Execute `list_agents.py` primeiro para obter os IDs

**Saída:**
- Respostas de cada teste no console
- Arquivo `test_results_YYYYMMDD_HHMMSS.json` com resultados detalhados

**Custo:** ⚠️ Sim (invoca agents do Bedrock)
- Estimativa: ~$0.01 por execução completa (4 testes)

---

### 3. `monitor_costs.py` - Monitoramento de Custos

Consulta e monitora os custos do Amazon Bedrock nos últimos 7 dias.

**Uso:**
```bash
python3 monitor_costs.py
```

**Saída:**
- Relatório de custos diários
- Projeção de custo mensal
- Arquivo `cost_report.json` com dados detalhados

**Custo:** ❌ Nenhum (apenas leitura do Cost Explorer)

**Requisitos:**
- Permissão para acessar AWS Cost Explorer
- Pode levar até 24h para custos aparecerem

---

### 4. `backup_config.py` - Backup de Configuração

Faz backup completo da configuração de todos os agents e knowledge bases.

**Uso:**
```bash
python3 backup_config.py
```

**Saída:**
- Arquivos JSON individuais para cada agent e KB na pasta `backup/`
- Arquivo `backup_summary_YYYYMMDD_HHMMSS.json` com resumo

**Custo:** ❌ Nenhum (apenas leitura)

**Recomendação:** Execute antes de fazer mudanças importantes

---

## 🚀 Quick Start

### 1. Configurar ambiente

```bash
# Ativar virtualenv (se necessário)
source ~/venv/ia/bin/activate

# Instalar dependências (se necessário)
pip install boto3
```

### 2. Verificar configuração AWS

```bash
# Testar acesso
aws bedrock-agent list-agents --region us-east-1 --profile Master
```

### 3. Listar agents e obter IDs

```bash
cd /home/bruno/AI/tests
python3 list_agents.py
```

### 4. Atualizar IDs no script de teste

Edite `test_multi_agent.py` e substitua:
```python
SUPERVISOR_AGENT_ID = 'seu-agent-id-aqui'
SUPERVISOR_ALIAS_ID = 'seu-alias-id-aqui'
```

### 5. Executar testes (opcional - gera custo)

```bash
python3 test_multi_agent.py
```

### 6. Monitorar custos

```bash
python3 monitor_costs.py
```

### 7. Fazer backup

```bash
python3 backup_config.py
```

---

## 📊 Estrutura de Arquivos Gerados

```
tests/
├── list_agents.py
├── test_multi_agent.py
├── monitor_costs.py
├── backup_config.py
├── README.md
├── bedrock_config.json              # Configuração exportada
├── test_results_*.json              # Resultados de testes
├── cost_report.json                 # Relatório de custos
└── ../backup/
    ├── agent_supervisor_*.json      # Backup do Supervisor
    ├── agent_especialista-rh_*.json # Backup do Agent RH
    ├── agent_especialista-produtos_*.json # Backup do Agent Vendas
    ├── kb_PoliticasRH_*.json        # Backup KB RH
    ├── kb_PoliticasCurso_*.json     # Backup KB Cursos
    └── backup_summary_*.json        # Resumo do backup
```

---

## 💰 Estimativa de Custos

| Script | Custo | Frequência Recomendada |
|--------|-------|------------------------|
| `list_agents.py` | $0.00 | Sempre que necessário |
| `test_multi_agent.py` | ~$0.01 | Após mudanças importantes |
| `monitor_costs.py` | $0.00 | Semanal |
| `backup_config.py` | $0.00 | Antes de mudanças |

**Total mensal estimado:** < $0.10 (uso moderado)

---

## 🔧 Troubleshooting

### Erro: "Unable to locate credentials"

```bash
# Verificar profile AWS
aws configure list --profile Master

# Fazer login SSO (se necessário)
aws sso login --profile Master
```

### Erro: "AccessDeniedException"

Verifique se seu usuário IAM tem as permissões:
- `bedrock:ListAgents`
- `bedrock:GetAgent`
- `bedrock:ListKnowledgeBases`
- `bedrock:GetKnowledgeBase`
- `ce:GetCostAndUsage` (para monitor_costs.py)

### Erro: "ThrottlingException"

Aguarde alguns segundos e tente novamente. Os scripts já incluem delays entre requisições.

---

## 📝 Notas

- Todos os scripts usam o profile `Master` e região `us-east-1`
- Para mudar, edite as constantes `PROFILE` e `REGION` em cada script
- Os backups são incrementais (não sobrescrevem backups anteriores)
- Arquivos JSON podem ser usados para restaurar configurações manualmente

---

**Última atualização:** 20/02/2026  
**Versão:** 1.0  
**Autor:** Bruno Mendes Augusto  
**Empresa:** Maestriacloud
