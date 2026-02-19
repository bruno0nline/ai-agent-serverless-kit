# Quotas Ajustáveis Prioritárias do Amazon Bedrock

## Status Atual
✅ **Identificadas quotas ajustáveis** (Adjustable: True)  
❌ **Todas com valor 0.0** (sem acesso habilitado)

---

## Quotas Cross-Region (Ajustáveis)

Estas quotas são para **inferência cross-region** (tokens por minuto):

### Priority 1 - Essenciais para o Projeto

| Quota Code | Modelo | Valor Atual | Ajustável |
|------------|--------|-------------|-----------|
| L-DCADBC78 | Anthropic Claude 3 Haiku | 0.0 | ✅ True |
| L-DC7FF66C | Amazon Nova Micro | 0.0 | ✅ True |
| L-C6F5908D | Amazon Nova 2 Lite | 0.0 | ✅ True |
| L-4C3F0FE6 | Cohere Embed V4 | 0.0 | ✅ True |

### Priority 2 - Alternativas

| Quota Code | Modelo | Valor Atual | Ajustável |
|------------|--------|-------------|-----------|
| L-479B647F | Anthropic Claude 3.5 Sonnet | 0.0 | ✅ True |
| L-4BF37C17 | Anthropic Claude 3.5 Haiku | 0.0 | ✅ True |
| L-C0326783 | Amazon Nova Pro | 0.0 | ✅ True |

---

## ⚠️ PROBLEMA IDENTIFICADO

As quotas listadas acima são para **Cross-Region Inference** (tokens por **minuto**).

**O que precisamos:**
- Quotas de **On-Demand** (tokens por **dia**)
- Quotas de **Embedding Models** (Titan Embeddings)

**Descoberta importante:**
- Quotas de **On-Demand tokens per day** NÃO são ajustáveis (Adjustable: False)
- Quotas de **Embedding models** NÃO aparecem como ajustáveis

---

## Próximos Passos

### Opção 1: Tentar Aumentar Cross-Region (Ajustáveis)

Mesmo sendo cross-region, podemos tentar aumentar para ter algum acesso:

```bash
# Claude 3 Haiku (Cross-Region)
aws service-quotas request-service-quota-increase \
  --service-code bedrock \
  --quota-code L-DCADBC78 \
  --desired-value 10000 \
  --region us-east-1 \
  --profile Master

# Amazon Nova Micro (Cross-Region)
aws service-quotas request-service-quota-increase \
  --service-code bedrock \
  --quota-code L-DC7FF66C \
  --desired-value 10000 \
  --region us-east-1 \
  --profile Master

# Amazon Nova 2 Lite (Cross-Region)
aws service-quotas request-service-quota-increase \
  --service-code bedrock \
  --quota-code L-C6F5908D \
  --desired-value 10000 \
  --region us-east-1 \
  --profile Master
```

**Observação:** Estas são quotas de tokens por **minuto**, não por dia.

---

### Opção 2: Abrir Ticket AWS Support (RECOMENDADO)

Como as quotas que realmente precisamos (On-Demand tokens per day) **NÃO são ajustáveis**, precisamos:

1. **Abrir ticket no AWS Support**
2. **Solicitar acesso inicial** aos modelos:
   - Amazon Titan Text Embeddings v2.0 (para Knowledge Base)
   - Amazon Nova Micro 1.0 (para Agent)
   - Anthropic Claude 3 Haiku (alternativa)

3. **Usar o template:** `ticket-aws-support-bedrock-quotas.md`

---

## Análise Detalhada

### Por que as quotas On-Demand não são ajustáveis?

Segundo a documentação AWS:
- Quotas de **On-Demand model invocation** requerem revisão do gerente de conta
- AWS prioriza clientes que já estão gerando tráfego
- Novas contas têm quotas iniciais em 0.0 por padrão
- Necessário justificar caso de uso e volume esperado

### Diferença entre Cross-Region e On-Demand

**Cross-Region Inference:**
- Distribui carga entre múltiplas regiões AWS
- Quota em tokens por **minuto**
- Ajustável via Service Quotas
- Requer configuração de perfil cross-region

**On-Demand Inference:**
- Uso direto na região (us-east-1)
- Quota em tokens por **dia**
- **NÃO ajustável** via Service Quotas
- Requer ticket AWS Support

---

## Comandos para Verificar Quotas Específicas

### Verificar quota do Claude Haiku (Cross-Region)
```bash
aws service-quotas get-service-quota \
  --service-code bedrock \
  --quota-code L-DCADBC78 \
  --region us-east-1 \
  --profile Master
```

### Verificar quota do Nova Micro (Cross-Region)
```bash
aws service-quotas get-service-quota \
  --service-code bedrock \
  --quota-code L-DC7FF66C \
  --region us-east-1 \
  --profile Master
```

### Listar solicitações pendentes
```bash
aws service-quotas list-requested-service-quota-change-history \
  --service-code bedrock \
  --region us-east-1 \
  --profile Master \
  --status PENDING
```

---

## Recomendação Final

### ✅ FAZER AGORA:

1. **Abrir ticket AWS Support** (prioridade máxima)
   - Usar template: `ticket-aws-support-bedrock-quotas.md`
   - Solicitar quotas On-Demand (tokens per day)
   - Justificar POC de Agente RH

2. **Opcionalmente:** Tentar aumentar quotas Cross-Region
   - Pode dar acesso temporário enquanto aguarda ticket
   - Requer configuração adicional de cross-region inference

### ❌ NÃO FAZER:

- Não esperar que quotas Cross-Region resolvam o problema principal
- Não tentar usar modelos sem quota habilitada (vai dar erro 429)
- Não fazer múltiplas solicitações simultâneas (pode ser negado)

---

**Conclusão:** As quotas ajustáveis que encontramos são para Cross-Region, mas o que realmente precisamos (On-Demand) requer ticket AWS Support.

**Próximo passo:** Abrir ticket usando o template preparado.

---

**Última atualização:** 16/02/2026  
**Projeto:** POC Agente RH - Maestriacloud
