import boto3

def list_lambda_functions():
    lambda_client = boto3.client('lambda')
    paginator = lambda_client.get_paginator('list_functions')
    
    for page in paginator.paginate():
        for function in page['Functions']:
            print(f"{function['FunctionName']} - Runtime: {function['Runtime']} - Última modificação: {function['LastModified']}")

if __name__ == "__main__":
    list_lambda_functions()
