# Knowledge Base - AWS Cloud Professional

## Sobre esta Knowledge Base

Esta base de conhecimento contém documentação técnica sobre serviços e melhores práticas da AWS, voltada para profissionais de cloud computing.

## Conteúdo

### 1. AWS Well-Architected Framework
**Arquivo:** `aws-well-architected.md`

Documentação completa sobre os 6 pilares do Well-Architected Framework:
- Excelência Operacional
- Segurança
- Confiabilidade
- Eficiência de Performance
- Otimização de Custos
- Sustentabilidade

### 2. AWS Security Best Practices
**Arquivo:** `aws-security-best-practices.md`

Guia abrangente de segurança cobrindo:
- IAM e gerenciamento de identidades
- Segurança de rede (VPC, Security Groups, NACLs)
- Criptografia e proteção de dados
- Detecção de ameaças (GuardDuty, Security Hub)
- Compliance e governança
- Incident response

### 3. AWS Compute Services
**Arquivo:** `aws-compute-services.md`

Documentação detalhada sobre serviços de computação:
- Amazon EC2 (tipos, pricing, Auto Scaling)
- AWS Lambda (serverless, limits, best practices)
- Amazon ECS (containers, Fargate)
- Amazon EKS (Kubernetes gerenciado)
- AWS Batch (processamento em lote)

## Como Usar

### Para RAG (Retrieval-Augmented Generation)

1. **Upload para S3:**
   ```bash
   aws s3 sync . s3://seu-bucket/knowledge-base/ \
       --exclude "README.md" \
       --exclude ".git/*"
   ```

2. **Criar Knowledge Base no Bedrock:**
   - Acesse Amazon Bedrock Console
   - Vá em "Knowledge bases" → "Create knowledge base"
   - Configure data source apontando para o bucket S3
   - Escolha modelo de embedding (recomendado: Amazon Titan Embeddings)
   - Selecione vector database (recomendado: OpenSearch Serverless)

3. **Sincronizar dados:**
   - Após criar, clique em "Sync"
   - Aguarde a indexação dos documentos

### Para Consultas

**Exemplo de perguntas que esta KB pode responder:**

- "Quais são os tipos de instâncias EC2 otimizadas para memória?"
- "Como implementar MFA no IAM?"
- "Qual a diferença entre ECS e EKS?"
- "Quais são os pilares do Well-Architected Framework?"
- "Como configurar IMDSv2 em instâncias EC2?"
- "Quais serviços usar para detecção de ameaças?"

## Estrutura dos Documentos

Todos os documentos seguem uma estrutura consistente:

```
# Título Principal
## Visão Geral
### Subtópicos
- Listas e exemplos
- Best practices
- Referências
```

## Manutenção

### Adicionar Novos Documentos

1. Crie arquivo .md na pasta
2. Siga o padrão de estrutura existente
3. Atualize este README
4. Faça sync com S3
5. Re-sincronize a Knowledge Base no Bedrock

### Atualizar Documentos

1. Edite o arquivo .md
2. Faça sync com S3
3. Re-sincronize a Knowledge Base no Bedrock

## Próximos Tópicos a Adicionar

- [ ] AWS Storage Services (S3, EBS, EFS, FSx)
- [ ] AWS Database Services (RDS, DynamoDB, Aurora)
- [ ] AWS Networking (VPC, Route 53, CloudFront)
- [ ] AWS Monitoring (CloudWatch, X-Ray, CloudTrail)
- [ ] AWS DevOps (CodePipeline, CodeBuild, CodeDeploy)
- [ ] AWS Serverless (API Gateway, Step Functions, EventBridge)
- [ ] AWS Cost Optimization Strategies
- [ ] AWS Migration Strategies (6 R's)

## Referências Oficiais

- AWS Documentation: <https://docs.aws.amazon.com/>
- AWS Architecture Center: <https://aws.amazon.com/architecture/>
- AWS Whitepapers: <https://aws.amazon.com/whitepapers/>
- AWS Well-Architected: <https://aws.amazon.com/architecture/well-architected/>
- AWS Security: <https://aws.amazon.com/security/>

## Versão

**Versão:** 1.0  
**Última atualização:** Fevereiro 2026  
**Autor:** Bruno Mendes Augusto
