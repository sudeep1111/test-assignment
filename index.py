import boto3
import os
import json

def handler(event, context):
    ssm = boto3.client('ssm')
    s3 = boto3.client('s3')
    
    parameter = ssm.get_parameter(Name='UserName', WithDecryption=False)
    user_name = parameter['Parameter']['Value']
    
    bucket_name = os.environ['BUCKET_NAME']
    file_name = 'username.txt'
    
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=user_name)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully stored the SSM Parameter in S3!')
    }
