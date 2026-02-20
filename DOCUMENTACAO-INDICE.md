# 📚 Índice da Documentação

**Guia rápido para encontrar o que você precisa**

---

## 🎯 Para Começar

| Documento | Quando Usar |
|-----------|-------------|
| **[README.md](README.md)** | Visão geral do projeto, status atual |
| **[GUIA-REPLICACAO.md](GUIA-REPLICACAO.md)** | ⭐ Recriar solução do zero em outra empresa |
| **[DEPLOYMENT.md](DEPLOYMENT.md)** | Deploy rápido (15 min) |

---

## 🏗️ Arquitetura e Configuração

| Documento | Conteúdo |
|-----------|----------|
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | Diagrama e componentes técnicos |
| **[Documentação/agents-maestriacloud.md](Documentação/agents-maestriacloud.md)** | Configuração detalhada dos 3 agents |
| **[TECH-STACK-2026.md](TECH-STACK-2026.md)** | Stack tecnológica e comparações |

---

## 💰 Custos e ROI

| Documento | Conteúdo |
|-----------|----------|
| **[Documentação/CUSTOS.md](Documentação/CUSTOS.md)** | Análise completa de custos, ROI, otimização |
| **[ROADMAP.md](ROADMAP.md)** | Planejamento POC → Produção → Comercial |

---

## 🐛 Troubleshooting

| Documento | Problema |
|-----------|----------|
| **[Documentação/Bedrock/RESUMO-EXECUTIVO.md](Documentação/Bedrock/RESUMO-EXECUTIVO.md)** | ⭐ Problemas com quotas Bedrock |
| **[Documentação/Bedrock/resolucao-throttling-quotas.md](Documentação/Bedrock/resolucao-throttling-quotas.md)** | HTTP 429 - Throttling |
| **[Documentação/Bedrock/STATUS-TICKET.md](Documentação/Bedrock/STATUS-TICKET.md)** | Histórico do ticket AWS |

---

## 🧪 Testes e Monitoramento

| Documento | Conteúdo |
|-----------|----------|
| **[tests/README.md](tests/README.md)** | Scripts de teste, backup e monitoramento |
| **[tests/test_multi_agent.py](tests/test_multi_agent.py)** | Testes automatizados multi-agent |
| **[tests/monitor_costs.py](tests/monitor_costs.py)** | Monitoramento de custos |
| **[tests/backup_config.py](tests/backup_config.py)** | Backup de configuração |

---

## 📦 Componentes Específicos

### Lambda Functions

| Documento | Conteúdo |
|-----------|----------|
| **[PythonAwsBedrockActionGroupDemo/README.md](PythonAwsBedrockActionGroupDemo/README.md)** | Lambda de consulta de feriados |
| **[Lambda/README.md](Lambda/README.md)** | Outras Lambdas (tickets, status, etc) |

### Knowledge Bases

| Documento | Conteúdo |
|-----------|----------|
| **[RAG-Knowledge-Base/README.md](RAG-Knowledge-Base/README.md)** | Estrutura das Knowledge Bases |
| **[RAG-Knowledge-Base/KB-RH/](RAG-Knowledge-Base/KB-RH/)** | Documentos de RH |
| **[RAG-Knowledge-Base/KB-Cursos/](RAG-Knowledge-Base/KB-Cursos/)** | Catálogo de cursos |

---

## 📖 Aprendizado

| Documento | Conteúdo |
|-----------|----------|
| **[Documentação/Inteligência Artificial AWS Bedrock.md](Documentação/Inteligência%20Artificial%20AWS%20Bedrock.md)** | Anotações do curso |
| **[Curso/Conteudo do curso.txt](Curso/Conteudo%20do%20curso.txt)** | Módulos do curso |

---

## 🚀 Fluxos de Trabalho

### Implementar em Nova Empresa

1. Ler: **[GUIA-REPLICACAO.md](GUIA-REPLICACAO.md)**
2. Verificar quotas: **[Documentação/Bedrock/](Documentação/Bedrock/)**
3. Seguir: **[DEPLOYMENT.md](DEPLOYMENT.md)**
4. Testar: **[tests/README.md](tests/README.md)**

### Resolver Problema de Quotas

1. Ler: **[Documentação/Bedrock/RESUMO-EXECUTIVO.md](Documentação/Bedrock/RESUMO-EXECUTIVO.md)**
2. Executar comandos: **[Documentação/Bedrock/comandos-prontos.md](Documentação/Bedrock/comandos-prontos.md)**
3. Abrir ticket: **[Documentação/Bedrock/ticket-aws-support-bedrock-quotas.md](Documentação/Bedrock/ticket-aws-support-bedrock-quotas.md)**

### Monitorar Custos

1. Executar: `python3 tests/monitor_costs.py`
2. Revisar: **[Documentação/CUSTOS.md](Documentação/CUSTOS.md)**
3. Otimizar conforme necessário

### Fazer Backup

1. Executar: `python3 tests/backup_config.py`
2. Verificar pasta: `backup/`
3. Guardar em local seguro

---

## 🎯 Documentos por Persona

### Desenvolvedor

- [GUIA-REPLICACAO.md](GUIA-REPLICACAO.md) - Implementação técnica
- [ARCHITECTURE.md](ARCHITECTURE.md) - Arquitetura
- [tests/README.md](tests/README.md) - Scripts e testes
- [Documentação/agents-maestriacloud.md](Documentação/agents-maestriacloud.md) - Configuração agents

### Gestor de Projeto

- [README.md](README.md) - Visão geral
- [ROADMAP.md](ROADMAP.md) - Planejamento
- [Documentação/CUSTOS.md](Documentação/CUSTOS.md) - Custos e ROI
- [TECH-STACK-2026.md](TECH-STACK-2026.md) - Stack tecnológica

### DevOps

- [DEPLOYMENT.md](DEPLOYMENT.md) - Deploy
- [tests/backup_config.py](tests/backup_config.py) - Backup
- [tests/monitor_costs.py](tests/monitor_costs.py) - Monitoramento
- [Documentação/Bedrock/](Documentação/Bedrock/) - Troubleshooting

---

## 📊 Estatísticas da Documentação

- **Total de documentos:** 30+
- **Linhas de código:** 5.000+
- **Scripts Python:** 4
- **Guias completos:** 8
- **Última atualização:** 20/02/2026

---

**Dica:** Use Ctrl+F para buscar palavras-chave neste índice!
