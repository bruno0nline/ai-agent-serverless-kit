import boto3

def list_rds_instances():
    rds = boto3.client('rds')
    paginator = rds.get_paginator('describe_db_instances')
    
    for page in paginator.paginate():
        for db in page['DBInstances']:
            print(f"{db['DBInstanceIdentifier']} - Engine: {db['Engine']} - Status: {db['DBInstanceStatus']}")

if __name__ == "__main__":
    list_rds_instances()
