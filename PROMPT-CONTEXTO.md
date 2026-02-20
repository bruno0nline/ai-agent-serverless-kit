# 🤖 Prompt de Contexto - AI Agent Serverless Kit

**Use este prompt ao iniciar um novo chat com Kiro para restaurar o contexto do projeto.**

---

## 📋 PROMPT PARA COPIAR E COLAR

```
Olá! Estou trabalhando no projeto AI Agent Serverless Kit - uma solução Multi-Agent usando AWS Bedrock.

Por favor, leia os seguintes arquivos para entender o contexto do projeto:

1. README.md - Visão geral e status atual
2. GUIA-REPLICACAO.md - Documentação completa de implementação
3. DOCUMENTACAO-INDICE.md - Índice de toda documentação
4. Documentação/agents-maestriacloud.md - Configuração dos agents
5. Documentação/CUSTOS.md - Análise de custos

RESUMO DO PROJETO:
- Empresa: Maestriacloud (Minas Gerais, Brasil)
- Objetivo: Sistema de atendimento automatizado com IA
- Arquitetura: Multi-Agent (1 Supervisor + 2 Collaborators)
- Status: Multi-Agent Collaboration concluído (20/02/2026)
- Próximo: Bedrock Flows (Módulo 63)

RECURSOS AWS CRIADOS:
- 3 Agents: supervisor (Patrícia), especialista-rh (Carla), especialista-produtos (Rafael)
- 3 Knowledge Bases: RH, Cursos, AWS
- 1 Lambda Function: Consulta_Feriados
- S3 Bucket: maestriatec-rag-knowledge-base
- Região: us-east-1
- Profile AWS: Master

ESTRUTURA DO PROJETO:
- /tests/ - Scripts Python de teste e monitoramento
- /Documentação/ - Toda documentação técnica
- /RAG-Knowledge-Base/ - Documentos das Knowledge Bases
- /Lambda/ - Funções Lambda
- /PythonAwsBedrockActionGroupDemo/ - Action Group de feriados

ONDE BUSCAR INFORMAÇÕES:
- Implementação do zero: GUIA-REPLICACAO.md
- Problemas de quotas: Documentação/Bedrock/RESUMO-EXECUTIVO.md
- Custos e ROI: Documentação/CUSTOS.md
- Configuração agents: Documentação/agents-maestriacloud.md
- Scripts de teste: tests/README.md
- Índice geral: DOCUMENTACAO-INDICE.md

Estou usando:
- Sistema: Ubuntu 24.04 (WSL no Windows)
- Python: virtualenv em ~/venv/ia
- AWS CLI: configurado com SSO
- Git: repositório https://github.com/bruno0nline/ai-agent-serverless-kit.git

Por favor, confirme que leu os arquivos e está pronto para me ajudar com o projeto!
```

---

## 🎯 VARIAÇÕES DO PROMPT

### Para Troubleshooting Específico

```
Olá! Preciso de ajuda com o projeto AI Agent Serverless Kit.

Leia: README.md, GUIA-REPLICACAO.md e Documentação/Bedrock/RESUMO-EXECUTIVO.md

Problema: [DESCREVA SEU PROBLEMA AQUI]

Contexto:
- Projeto: Multi-Agent com AWS Bedrock
- Região: us-east-1
- Profile: Master
- Status: [DESCREVA O STATUS]
```

### Para Adicionar Nova Funcionalidade

```
Olá! Quero adicionar uma nova funcionalidade ao AI Agent Serverless Kit.

Leia: README.md, ARCHITECTURE.md e Documentação/agents-maestriacloud.md

Nova funcionalidade: [DESCREVA O QUE QUER ADICIONAR]

Contexto atual:
- 3 Agents funcionando (Supervisor + 2 Collaborators)
- 3 Knowledge Bases ativas
- Lambda Action Group implementada
- Região: us-east-1
```

### Para Análise de Custos

```
Olá! Preciso analisar custos do projeto AI Agent Serverless Kit.

Leia: Documentação/CUSTOS.md e tests/README.md

Contexto:
- Projeto: Multi-Agent Bedrock
- Uso atual: [DESCREVA SEU USO]
- Objetivo: [OTIMIZAR/PROJETAR/ANALISAR]
```

### Para Deploy em Nova Empresa

```
Olá! Vou replicar o AI Agent Serverless Kit em uma nova empresa.

Leia: GUIA-REPLICACAO.md e DEPLOYMENT.md

Nova empresa: [NOME DA EMPRESA]
Caso de uso: [DESCREVA O CASO DE USO]
Região AWS: [REGIÃO]

Por favor, me guie pelo processo de implementação passo a passo.
```

---

## 📝 CHECKLIST ANTES DE USAR O PROMPT

Antes de colar o prompt em um novo chat, verifique:

- [ ] Você está no diretório correto: `/home/bruno/AI`
- [ ] Git está atualizado: `git pull origin main`
- [ ] AWS CLI está logado: `aws s3 ls --profile Master`
- [ ] Virtualenv ativado (se necessário): `source ~/venv/ia/bin/activate`

---

## 🔄 ATUALIZAR ESTE PROMPT

Quando o projeto evoluir, atualize este arquivo com:

1. Novo status do projeto
2. Novos recursos AWS criados
3. Novos documentos importantes
4. Mudanças na estrutura

**Última atualização:** 20/02/2026  
**Versão:** 1.0 - Multi-Agent Collaboration concluído

---

## 💡 DICAS DE USO

### Dica 1: Seja Específico
Quanto mais específico você for sobre o que precisa, melhor a IA pode ajudar.

### Dica 2: Mencione Arquivos Relevantes
Se você sabe qual arquivo tem a informação, mencione no prompt:
```
"Verifique o arquivo Documentação/agents-maestriacloud.md 
e me ajude a configurar um novo collaborator agent"
```

### Dica 3: Forneça Contexto de Erro
Se tiver um erro, cole a mensagem completa:
```
"Estou recebendo este erro ao executar tests/test_multi_agent.py:
[COLE O ERRO AQUI]

Por favor, leia tests/README.md e me ajude a resolver."
```

### Dica 4: Use Comandos AWS
Peça para a IA executar comandos AWS para verificar recursos:
```
"Execute 'aws bedrock-agent list-agents' e me mostre 
o status dos meus agents"
```

### Dica 5: Peça para Ler Múltiplos Arquivos
```
"Leia README.md, GUIA-REPLICACAO.md e Documentação/CUSTOS.md 
e me dê um resumo do projeto e custos estimados"
```

---

## 🚀 EXEMPLO DE CONVERSA COMPLETA

**Você:**
```
[COLA O PROMPT PRINCIPAL]
```

**Kiro:**
```
✅ Li todos os arquivos solicitados. Entendi que você está trabalhando 
no AI Agent Serverless Kit com Multi-Agent Collaboration usando AWS Bedrock.

Status atual:
- 3 Agents configurados e funcionando
- Multi-Agent concluído em 20/02/2026
- Próximo passo: Bedrock Flows (Módulo 63)

Como posso ajudar hoje?
```

**Você:**
```
Preciso adicionar um novo collaborator agent para atendimento técnico. 
Como faço isso?
```

**Kiro:**
```
Vou te guiar pelo processo. Baseado no GUIA-REPLICACAO.md, 
você precisa seguir estes passos:

1. Criar documentos técnicos e fazer upload para S3
2. Criar nova Knowledge Base
3. Criar novo Collaborator Agent
4. Adicionar ao Supervisor

Vamos começar?
```

---

## 📞 SUPORTE

Se o prompt não funcionar como esperado:

1. Verifique se os arquivos mencionados existem
2. Atualize o repositório: `git pull origin main`
3. Verifique se está no diretório correto: `pwd`
4. Tente um prompt mais específico

---

**Arquivo criado em:** 20/02/2026  
**Autor:** Bruno Mendes Augusto  
**Projeto:** AI Agent Serverless Kit - Maestriacloud
