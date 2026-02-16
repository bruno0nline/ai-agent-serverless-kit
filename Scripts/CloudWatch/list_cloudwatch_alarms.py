import boto3

def list_cloudwatch_alarms():
    cloudwatch = boto3.client('cloudwatch')
    paginator = cloudwatch.get_paginator('describe_alarms')
    
    for page in paginator.paginate():
        for alarm in page['MetricAlarms']:
            print(f"{alarm['AlarmName']} - Estado: {alarm['StateValue']} - Métrica: {alarm['MetricName']}")

if __name__ == "__main__":
    list_cloudwatch_alarms()
