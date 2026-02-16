import boto3

def list_s3_buckets():
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_buckets')
    
    for page in paginator.paginate():
        for bucket in page['Buckets']:
            print(f"{bucket['Name']} - Criado em: {bucket['CreationDate']}")

if __name__ == "__main__":
    list_s3_buckets()
