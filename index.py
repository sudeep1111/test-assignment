import boto3
import os

def lambda_handler(event, context):
    ssm = boto3.client('ssm')
    s3 = boto3.client('s3')
    parameter_name = os.environ['PARAMETER_NAME']

    response = ssm.get_parameter(Name=parameter_name, WithDecryption=False)
    value = response['Parameter']['Value']

    bucket_name = 'DXT-Assignment'
    key = 'user_name.txt'
    s3.put_object(Bucket=bucket_name, Key=key, Body=value)

    return f"Stored value '{value}' in S3 bucket '{bucket_name}' with key '{key}'"
