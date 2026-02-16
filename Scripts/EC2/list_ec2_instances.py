import boto3

def list_ec2_instances():
    ec2 = boto3.client('ec2')
    paginator = ec2.get_paginator('describe_instances')
    
    for page in paginator.paginate():
        for reservation in page['Reservations']:
            for instance in reservation['Instances']:
                name = next((tag['Value'] for tag in instance.get('Tags', []) if tag['Key'] == 'Name'), 'Sem nome')
                print(f"{instance['InstanceId']} - {name} - Estado: {instance['State']['Name']}")

if __name__ == "__main__":
    list_ec2_instances()
