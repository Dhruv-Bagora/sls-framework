import json
import boto3
from decimal import Decimal

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Student')

# Helper function to convert Decimal types to float or int
def decimal_to_standard(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    if isinstance(obj, list):
        return [decimal_to_standard(i) for i in obj]
    if isinstance(obj, dict):
        return {k: decimal_to_standard(v) for k, v in obj.items()}
    return obj

def lambda_handler(event, context):
    # Retrieve all items from the DynamoDB table
    response = table.scan()
    
    # Convert any Decimal values in the response to standard Python types
    items = decimal_to_standard(response.get('Items', []))
    
    # Return all items or a "No students found" message if empty
    if items:
        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('No students found')
        }
