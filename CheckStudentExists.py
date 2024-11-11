import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Student')

def lambda_handler(event, context):
    # Extract studentId from query parameters
    student_id = event['queryStringParameters']['studentId']
    
    # Check if item exists in DynamoDB
    response = table.get_item(Key={'studentId': student_id})
    exists = 'Item' in response
    
    return {
        'statusCode': 200,
        'body': json.dumps({'exists': exists})
    }
