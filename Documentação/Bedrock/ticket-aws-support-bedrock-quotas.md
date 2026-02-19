# Ticket AWS Support - Aumento de Quotas do Amazon Bedrock

## Informações Básicas

**Tipo de Caso:** Service Limit Increase  
**Serviço:** Amazon Bedrock  
**Categoria:** Service Quotas  
**Severidade:** Normal (ou Business-critical se for urgente)  
**Região:** us-east-1 (US East - N. Virginia)  
**Account ID:** 624012998785

---

## Título do Ticket

**Solicitação de Aumento de Quotas para Amazon Bedrock - Tokens por Dia**

---

## Descrição do Problema

Olá equipe AWS Support,

Estou desenvolvendo uma aplicação de IA usando Amazon Bedrock e estou enfrentando erros de throttling (HTTP 429) em todas as operações do serviço.

### Erro Recebido

```
ThrottlingException: Too many requests, please wait before trying again.
Status Code: 429
Error Message: "Too many tokens per day"
```

### Operações Afetadas

1. **Knowledge Base Sync**: Falha ao sincronizar Knowledge Base com modelo de embedding
2. **Playground**: Impossível testar modelos no console
3. **Agent Testing**: Não consigo testar agentes criados
4. **Model Invocation**: Todas invocações de modelos falham

### Análise de Quotas Atual

Executei o comando AWS CLI para verificar as quotas:

```bash
aws service-quotas list-service-quotas --service-code bedrock --region us-east-1 --profile Master
```

**Resultado:** TODAS as quotas de "tokens per day" estão configuradas em **0.0** (zero), incluindo:

- Model invocation max tokens per day for Anthropic Claude 3 Haiku: **0.0**
- Model invocation max tokens per day for Anthropic Claude Sonnet 4 V1: **0.0**
- Model invocation max tokens per day for Amazon Nova 2 Lite: **0.0**
- Model invocation max tokens per day for Cohere Embed V4: **0.0**
- Global cross-region model inference tokens per day: **0.0**

---

## Contexto de Uso

**Tipo de Aplicação:** POC/Teste de Agente de IA para RH  
**Empresa:** Maestriacloud (Minas Gerais, Brasil)  
**Objetivo:** Criar assistente virtual de RH usando RAG (Retrieval-Augmented Generation)

### Componentes Criados

1. **Knowledge Base:** PoliticasRH-KnowledgeBase (ID: A4Q25RNG54)
   - Fonte: S3 (s3://maestriatec-rag-knowledge-base/RH/)
   - Embedding Model: Amazon Titan Text Embeddings v2.0
   - Vector DB: Amazon S3 Vectors

2. **Agent:** agent-rh-chatbot
   - Modelo: Amazon Nova Micro 1.0
   - Função: Assistente de RH para atendimento de funcionários

### Volume Esperado (POC)

- **Uso diário estimado:** ~100.000 tokens/dia
- **Modelos principais:**
  - Amazon Titan Text Embeddings v2.0 (para Knowledge Base)
  - Amazon Nova Micro 1.0 (para Agent)
  - Anthropic Claude 3 Haiku (testes alternativos)

---

## Solicitação de Aumento de Quotas

Solicito o aumento das seguintes quotas para permitir o desenvolvimento e teste da aplicação:

### Quotas Prioritárias (Essenciais)

1. **Amazon Titan Text Embeddings v2.0**
   - Quota Code: (verificar no console)
   - Valor Atual: 0.0
   - Valor Solicitado: **500.000 tokens/dia**
   - Justificativa: Necessário para sincronizar Knowledge Base e processar embeddings

2. **Amazon Nova Micro 1.0**
   - Quota Code: (verificar no console)
   - Valor Atual: 0.0
   - Valor Solicitado: **300.000 tokens/dia**
   - Justificativa: Modelo principal do agente de RH

3. **Anthropic Claude 3 Haiku**
   - Quota Code: L-A60EE1AF
   - Valor Atual: 0.0
   - Valor Solicitado: **200.000 tokens/dia**
   - Justificativa: Modelo alternativo para testes e comparações

### Quotas Secundárias (Desejáveis)

4. **Anthropic Claude 3.5 Sonnet**
   - Valor Solicitado: **100.000 tokens/dia**
   - Justificativa: Testes com modelo mais avançado

5. **Cohere Embed V4**
   - Quota Code: L-F1BB08BB
   - Valor Solicitado: **200.000 tokens/dia**
   - Justificativa: Alternativa de embedding para comparação

---

## Informações Adicionais

### Arquitetura da Solução

```
Usuário → AWS Bedrock Agent (agent-rh-chatbot)
           ↓
       Amazon Nova Micro 1.0 (Foundation Model)
           ↓
       Knowledge Base (PoliticasRH-KnowledgeBase)
           ↓
       Amazon Titan Embeddings v2.0 + S3 Vectors
           ↓
       S3 Bucket (s3://maestriatec-rag-knowledge-base/RH/)
```

### Documentos na Knowledge Base

- beneficios.md
- codigo-conduta.md
- politica-ferias.md
- Total: ~2.5KB de texto

### Timeline

- **Início do projeto:** 12/02/2026
- **Erro identificado:** 13/02/2026
- **Urgência:** Média (POC em desenvolvimento)

---

## Perguntas para o Support

1. Por que todas as quotas de "tokens per day" estão em 0.0 por padrão?
2. Existe algum processo de aprovação necessário antes de usar o Bedrock?
3. Quanto tempo leva para o aumento de quotas ser aplicado?
4. As quotas são resetadas diariamente em que horário (UTC)?
5. Existe alguma quota "free tier" disponível para testes iniciais?

---

## Evidências

### Screenshot do Erro (anexar ao ticket)

- Erro de sync da Knowledge Base (429 ThrottlingException)
- Erro no Playground do Bedrock
- Erro ao testar Agent

### Comandos Executados

```bash
# Listar quotas do Bedrock
aws service-quotas list-service-quotas --service-code bedrock --region us-east-1 --profile Master

# Listar modelos disponíveis
aws bedrock list-foundation-models --by-provider amazon --region us-east-1 --profile Master

# Verificar arquivos no S3
aws s3 ls s3://maestriatec-rag-knowledge-base/RH/ --recursive --profile Master
```

---

## Contato

**Nome:** [Seu Nome]  
**Email:** [Seu Email]  
**Telefone:** [Seu Telefone] (opcional)  
**Melhor horário para contato:** [Horário]

---

## Observações Finais

Esta é uma POC (Proof of Concept) para avaliar o Amazon Bedrock antes de implementar em produção. O sucesso deste teste determinará a adoção do serviço pela empresa Maestriacloud.

Agradeço a atenção e aguardo retorno.

Atenciosamente,
[Seu Nome]
