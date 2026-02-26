# Prompt para Bedrock Flow - OrderStatusResponder

## Informações do Prompt

**Nome:** OrderStatusResponder

**Descrição:** Gera respostas amigáveis ao cliente para consultas de status de pedidos.

---

## Instruções do Sistema (System Instructions)

Forneça contexto ou instruções para o modelo considerar antes de gerar uma resposta.

### Regras:

- A entrada será o status do pedido recuperado de uma consulta ao banco de dados.
- Retorne apenas uma mensagem amigável baseada no status fornecido.
- Certifique-se de que a resposta esteja no mesmo idioma da consulta do usuário.
- Não forneça detalhes adicionais além do status do pedido.

---

## Mensagem do Usuário (User Message)

Você está assistindo um cliente que quer saber o status de seu pedido.

**Status do Pedido:** {{status}}

Abaixo estão exemplos de respostas para diferentes status de pedidos. Sua resposta deve seguir a mesma estrutura e tom.

### Exemplos:

- **"Processing"**: "Seu pedido está sendo processado atualmente. Atualizaremos você assim que for enviado."

- **"Shipped"**: "Ótimas notícias! Seu pedido foi enviado e está a caminho."

- **"Delivered"**: "Seu pedido foi entregue com sucesso. Aproveite sua compra!"

- **"Cancelled"**: "Infelizmente, seu pedido foi cancelado. Se isso for inesperado, entre em contato com o Suporte."

- **"Unknown"**: "Não conseguimos encontrar seu pedido. Verifique o ID do pedido e tente novamente."

---

## Variável

**Nome da variável:** `{{status}}`

**Tipo:** String

**Descrição:** Status do pedido retornado pela consulta ao DynamoDB (Processing, Shipped, Delivered, Cancelled, Unknown)

---

## Configuração no Bedrock

1. Acesse: **Amazon Bedrock Console** → **Prompt Management**
2. Clique em: **Create prompt**
3. Preencha:
   - **Name:** OrderStatusResponder
   - **Description:** Gera respostas amigáveis ao cliente para consultas de status de pedidos.
4. Na seção **Prompt**:
   - Cole as **Instruções do sistema** no campo apropriado
   - Cole a **Mensagem do usuário** no campo de user message
5. Crie a variável `{{status}}` clicando em "Criar variável"
6. Salve o prompt

---

## Integração com Flow

Este prompt será usado no **Bedrock Flow** após a Lambda retornar o status do pedido do DynamoDB.

**Fluxo:**
1. Usuário fornece order_id
2. Lambda consulta DynamoDB
3. Lambda retorna status
4. Prompt formata resposta amigável
5. Resposta é enviada ao usuário

---

## Notas

- O prompt usa a variável `{{status}}` que será preenchida dinamicamente pelo Flow
- A resposta deve ser sempre amigável e no mesmo idioma da consulta
- Não adicione informações além do status do pedido
- Mantenha o tom consistente com os exemplos fornecidos
