# AWS Compute Services - Guia Completo

## Amazon EC2 (Elastic Compute Cloud)

### Visão Geral
Servidores virtuais escaláveis na nuvem AWS. Oferece controle completo sobre a configuração do sistema operacional e aplicações.

### Tipos de Instâncias

**Categorias Principais:**

1. **General Purpose (T, M)**
   - T3/T4g: Burstable, ideal para workloads variáveis
   - M5/M6i: Balanceado CPU/memória, uso geral

2. **Compute Optimized (C)**
   - C5/C6i: Alto desempenho de CPU
   - Ideal para: batch processing, gaming servers, HPC

3. **Memory Optimized (R, X, Z)**
   - R5/R6i: Alta memória para bancos de dados
   - X2: Até 4TB de RAM
   - Z1d: Alta frequência de CPU + memória

4. **Storage Optimized (I, D, H)**
   - I3/I4i: NVMe SSD, baixa latência
   - D2/D3: HDD denso, data warehousing
   - H1: HDD, MapReduce, HDFS

5. **Accelerated Computing (P, G, F)**
   - P4: GPU para ML/AI
   - G4: GPU para graphics/ML inference
   - F1: FPGA customizável

### Modelos de Precificação

**On-Demand:**
- Pague por hora/segundo
- Sem compromisso
- Ideal para: workloads imprevisíveis, testes

**Reserved Instances:**
- Desconto de até 75%
- Compromisso de 1 ou 3 anos
- Tipos: Standard, Convertible, Scheduled

**Savings Plans:**
- Desconto de até 72%
- Flexível entre tipos de instância
- Compromisso de uso por hora ($/hora)

**Spot Instances:**
- Desconto de até 90%
- Pode ser interrompido pela AWS
- Ideal para: batch jobs, big data, CI/CD

**Dedicated Hosts:**
- Servidor físico dedicado
- Compliance e licenciamento
- Mais caro

### IMDSv2 (Instance Metadata Service v2)

**Por que usar:**
- Proteção contra SSRF attacks
- Autenticação baseada em sessão
- Obrigatório para segurança

**Configuração:**
```bash
# Forçar IMDSv2
aws ec2 modify-instance-metadata-options \
    --instance-id i-1234567890abcdef0 \
    --http-tokens required \
    --http-put-response-hop-limit 1
```

### Auto Scaling

**Componentes:**
- Launch Template/Configuration
- Auto Scaling Group
- Scaling Policies

**Tipos de Scaling:**
1. **Target Tracking**: Mantém métrica em valor alvo
2. **Step Scaling**: Escala baseado em thresholds
3. **Scheduled Scaling**: Escala em horários específicos
4. **Predictive Scaling**: ML para prever demanda

## AWS Lambda

### Visão Geral
Compute serverless que executa código em resposta a eventos. Pague apenas pelo tempo de execução.

### Características

**Limites:**
- Memória: 128 MB a 10 GB
- Timeout: Até 15 minutos
- Payload: 6 MB (síncrono), 256 KB (assíncrono)
- /tmp storage: 512 MB a 10 GB
- Concurrent executions: 1000 (padrão, pode aumentar)

**Runtimes Suportados:**
- Python 3.8, 3.9, 3.10, 3.11, 3.12
- Node.js 16.x, 18.x, 20.x
- Java 8, 11, 17, 21
- .NET 6, 8
- Go 1.x
- Ruby 3.2
- Custom Runtime (usando Lambda Layers)

### Modelos de Invocação

**Síncrono:**
- API Gateway
- Application Load Balancer
- Cognito
- Aguarda resposta

**Assíncrono:**
- S3 Events
- SNS
- EventBridge
- Retry automático (2x)

**Stream-based:**
- DynamoDB Streams
- Kinesis Data Streams
- SQS
- Polling contínuo

### Best Practices

1. **Otimização de Performance**
   - Use variáveis de ambiente
   - Reutilize conexões (fora do handler)
   - Use Lambda Layers para dependências
   - Configure Provisioned Concurrency para latência previsível

2. **Segurança**
   - Least privilege IAM roles
   - Use Secrets Manager para credenciais
   - Habilite VPC apenas se necessário
   - Use Lambda@Edge para proteção adicional

3. **Custo**
   - Otimize memória (CPU escala com memória)
   - Use ARM (Graviton2) para 20% economia
   - Monitore duração e invocações
   - Considere Step Functions para workflows longos

### Lambda Layers

**Uso:**
- Compartilhar código entre funções
- Separar dependências do código
- Reduzir tamanho do deployment package
- Até 5 layers por função

## Amazon ECS (Elastic Container Service)

### Visão Geral
Orquestração de containers Docker totalmente gerenciada.

### Launch Types

**EC2 Launch Type:**
- Você gerencia instâncias EC2
- Mais controle sobre infraestrutura
- Pode usar Spot/Reserved Instances

**Fargate Launch Type:**
- Serverless para containers
- AWS gerencia infraestrutura
- Pague por vCPU e memória usados
- Mais simples, menos controle

### Componentes

**Task Definition:**
- Blueprint do container
- Define: imagem, CPU, memória, networking, IAM role
- Versionado

**Service:**
- Mantém número desejado de tasks rodando
- Integra com ELB
- Auto scaling
- Rolling updates

**Cluster:**
- Agrupamento lógico de tasks/services
- Pode ter múltiplos launch types

### Best Practices

- Use ECR para armazenar imagens
- Scan imagens com ECR Image Scanning
- Use secrets do Secrets Manager
- Configure health checks
- Use Service Discovery para comunicação entre services
- Implemente CI/CD com CodePipeline

## Amazon EKS (Elastic Kubernetes Service)

### Visão Geral
Kubernetes gerenciado pela AWS. Control plane gerenciado, você gerencia worker nodes.

### Componentes

**Control Plane:**
- Gerenciado pela AWS
- Multi-AZ por padrão
- Atualizações automáticas disponíveis

**Worker Nodes:**
- Managed Node Groups (recomendado)
- Self-managed nodes
- Fargate (serverless)

### Add-ons Importantes

- **AWS Load Balancer Controller**: Integração com ALB/NLB
- **Amazon EBS CSI Driver**: Persistent volumes
- **Amazon EFS CSI Driver**: Shared storage
- **CoreDNS**: Service discovery
- **kube-proxy**: Network proxy
- **VPC CNI**: Networking

### Best Practices

1. **Segurança**
   - Use IRSA (IAM Roles for Service Accounts)
   - Habilite Pod Security Standards
   - Use Network Policies
   - Scan imagens regularmente

2. **Networking**
   - Use VPC CNI para performance
   - Configure Security Groups for Pods
   - Use PrivateLink para serviços AWS

3. **Observabilidade**
   - Container Insights para métricas
   - Fluent Bit para logs
   - AWS X-Ray para tracing

## AWS Batch

### Visão Geral
Execução de batch jobs em qualquer escala. Provisiona automaticamente recursos compute.

### Componentes

**Job Definition:**
- Container image
- vCPUs e memória
- IAM role
- Environment variables

**Job Queue:**
- Prioridade de jobs
- Associado a compute environments

**Compute Environment:**
- Managed ou Unmanaged
- EC2 ou Fargate
- Spot ou On-Demand

### Casos de Uso

- Processamento de imagens/vídeos
- Análise de dados em lote
- Simulações científicas
- ETL jobs
- Rendering

## Comparação de Serviços

| Serviço | Quando Usar | Gerenciamento | Custo |
|---------|-------------|---------------|-------|
| EC2 | Controle total, aplicações legadas | Alto | Médio |
| Lambda | Event-driven, curta duração | Baixo | Baixo (pay-per-use) |
| ECS | Containers, controle sobre infra | Médio | Médio |
| EKS | Kubernetes, portabilidade | Alto | Alto |
| Fargate | Containers serverless | Baixo | Médio-Alto |
| Batch | Batch processing, HPC | Baixo | Médio |

## Referências

- EC2 User Guide: <https://docs.aws.amazon.com/ec2/>
- Lambda Developer Guide: <https://docs.aws.amazon.com/lambda/>
- ECS Developer Guide: <https://docs.aws.amazon.com/ecs/>
- EKS User Guide: <https://docs.aws.amazon.com/eks/>
