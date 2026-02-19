# AWS Security Best Practices

## Gerenciamento de Identidade e Acesso (IAM)

### Princípios Fundamentais

**Least Privilege (Menor Privilégio)**
- Conceda apenas as permissões necessárias para realizar uma tarefa
- Comece com permissões mínimas e adicione conforme necessário
- Use políticas gerenciadas pela AWS quando possível
- Revise permissões regularmente

**Separation of Duties (Separação de Funções)**
- Divida responsabilidades entre múltiplos usuários/roles
- Nenhum usuário deve ter acesso completo sozinho
- Implemente aprovações para ações críticas

### IAM Best Practices

1. **Nunca use a conta root para tarefas diárias**
   - Crie usuários IAM para administradores
   - Habilite MFA na conta root
   - Delete ou desabilite access keys da root

2. **Habilite MFA (Multi-Factor Authentication)**
   - Obrigatório para usuários com privilégios elevados
   - Use MFA virtual ou hardware
   - Considere U2F keys para máxima segurança

3. **Use IAM Roles ao invés de Access Keys**
   - Para aplicações EC2: use IAM Instance Profiles
   - Para Lambda: use Execution Roles
   - Para cross-account: use Assume Role
   - Evite hardcoded credentials

4. **Rotação de Credenciais**
   - Rotacione access keys a cada 90 dias
   - Use AWS Secrets Manager para automação
   - Implemente políticas de senha forte
   - Force mudança de senha no primeiro login

5. **Monitore e Audite**
   - Habilite AWS CloudTrail em todas as regiões
   - Use AWS Config para compliance
   - Configure alertas no CloudWatch
   - Revise IAM Access Analyzer findings

## Segurança de Rede

### Amazon VPC (Virtual Private Cloud)

**Componentes de Segurança:**

1. **Security Groups (Stateful)**
   - Firewall em nível de instância
   - Apenas regras de ALLOW
   - Avalie por protocolo, porta e origem/destino

2. **Network ACLs (Stateless)**
   - Firewall em nível de subnet
   - Regras de ALLOW e DENY
   - Avaliadas em ordem numérica

3. **VPC Flow Logs**
   - Capture tráfego de rede
   - Envie para CloudWatch ou S3
   - Analise padrões suspeitos

### Proteção de Endpoints

- **AWS PrivateLink**: Acesso privado a serviços AWS
- **VPC Endpoints**: Evite tráfego pela internet
- **AWS Direct Connect**: Conexão dedicada on-premises

## Proteção de Dados

### Criptografia

**Em Repouso (At Rest):**
- Amazon S3: SSE-S3, SSE-KMS, SSE-C
- Amazon EBS: Criptografia de volumes
- Amazon RDS: Transparent Data Encryption
- Amazon DynamoDB: Encryption at rest

**Em Trânsito (In Transit):**
- Use TLS 1.2 ou superior
- Certificate Manager para certificados SSL/TLS
- Enforce HTTPS em CloudFront e ALB
- VPN ou Direct Connect para conexões on-premises

### AWS Key Management Service (KMS)

**Tipos de Chaves:**
- **AWS Managed Keys**: Gerenciadas pela AWS
- **Customer Managed Keys**: Controle total
- **Custom Key Store**: HSM dedicado (CloudHSM)

**Best Practices:**
- Use diferentes chaves para diferentes ambientes
- Habilite rotação automática de chaves
- Use key policies para controle granular
- Monitore uso de chaves com CloudTrail

## Detecção de Ameaças

### Amazon GuardDuty

**O que detecta:**
- Atividade de reconhecimento (port scanning)
- Instâncias comprometidas (malware, cryptomining)
- Contas comprometidas (credenciais vazadas)
- Comunicação com IPs maliciosos

**Integração:**
- Envia findings para Security Hub
- Automatize resposta com EventBridge + Lambda
- Integre com SIEM externo

### AWS Security Hub

**Funcionalidades:**
- Agregação de findings de múltiplos serviços
- Compliance checks (CIS, PCI-DSS, AWS Best Practices)
- Priorização de alertas por severidade
- Integração com GuardDuty, Inspector, Macie

## Compliance e Governança

### AWS Config

**Regras Gerenciadas:**
- ec2-instance-managed-by-ssm
- encrypted-volumes
- rds-multi-az-support
- s3-bucket-public-read-prohibited
- iam-password-policy

**Remediação Automática:**
- Configure SSM Automation Documents
- Corrija não-conformidades automaticamente
- Notifique equipes via SNS

### AWS Organizations

**Service Control Policies (SCPs):**
- Restrinja ações em nível de conta
- Previna desabilitação de serviços de segurança
- Force uso de regiões específicas
- Bloqueie criação de recursos não-aprovados

## Segurança de Aplicações

### AWS WAF (Web Application Firewall)

**Proteções:**
- SQL Injection
- Cross-Site Scripting (XSS)
- Rate limiting
- Geo-blocking
- Bot protection

**Managed Rules:**
- AWS Managed Rules (Core Rule Set)
- Known Bad Inputs
- SQL Database
- Linux/Windows Operating System

### AWS Shield

**Shield Standard (Gratuito):**
- Proteção contra DDoS Layer 3/4
- Automático para todos os clientes

**Shield Advanced (Pago):**
- Proteção avançada DDoS
- Equipe de resposta 24/7
- Proteção de custo durante ataques
- Integração com WAF

## Segurança de Containers

### Amazon ECS/EKS

**Best Practices:**
- Use imagens de registries confiáveis
- Scan imagens com Amazon ECR Image Scanning
- Use secrets do Secrets Manager
- Implemente network policies
- Use IAM Roles for Service Accounts (IRSA)
- Habilite logging e monitoring

## Backup e Disaster Recovery

### AWS Backup

**Estratégia 3-2-1:**
- 3 cópias dos dados
- 2 tipos diferentes de mídia
- 1 cópia offsite

**Configuração:**
- Backup plans automatizados
- Retention policies
- Cross-region backup
- Backup vault lock (WORM)

### Disaster Recovery Strategies

1. **Backup and Restore** (RPO/RTO: horas)
2. **Pilot Light** (RPO/RTO: 10s de minutos)
3. **Warm Standby** (RPO/RTO: minutos)
4. **Multi-Site Active/Active** (RPO/RTO: segundos)

## Incident Response

### Preparação

1. **Crie um Incident Response Plan**
2. **Configure CloudTrail e GuardDuty**
3. **Prepare runbooks de resposta**
4. **Treine a equipe regularmente**

### Resposta a Incidentes

**Passos:**
1. Detecção e Análise
2. Contenção (isolar recursos comprometidos)
3. Erradicação (remover ameaça)
4. Recuperação (restaurar operações)
5. Post-Incident Review (lições aprendidas)

**Ferramentas:**
- AWS Systems Manager Incident Manager
- Amazon Detective (investigação)
- AWS Security Hub (centralização)

## Referências

- AWS Security Best Practices: <https://aws.amazon.com/security/best-practices/>
- AWS Security Documentation: <https://docs.aws.amazon.com/security/>
- CIS AWS Foundations Benchmark: <https://www.cisecurity.org/benchmark/amazon_web_services>
