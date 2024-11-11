import json
import boto3
from datetime import datetime

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Student')

def lambda_handler(event, context):
    # Check if 'body' exists in the event
    if event.get('body') is None:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid request: No data provided')
        }

    # Parse the JSON body
    body = json.loads(event['body'])
    student_id = body['studentId']
    name = body['name']
    age = body['age']
    
    # Item to be inserted
    item = {
        'studentId': student_id,
        'name': name,
        'age': age,
        'createdAt': datetime.now().isoformat()
    }
    
    # Insert the item into DynamoDB
    table.put_item(Item=item)
    
    # Response
    return {
        'statusCode': 200,
        'body': json.dumps('Student created successfully!')
    }
