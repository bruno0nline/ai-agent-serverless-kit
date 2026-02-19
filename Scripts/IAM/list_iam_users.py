import boto3

def list_iam_users():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_users')
    
    for page in paginator.paginate():
        for user in page['Users']:
            print(f"{user['UserName']} - Criado em: {user['CreateDate']}")

if __name__ == "__main__":
    list_iam_users()
