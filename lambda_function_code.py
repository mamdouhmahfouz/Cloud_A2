import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    for record in event['Records']:
        message = json.loads(record['body']) 

       
        if 'Message' in message:
            message = json.loads(message['Message'])

        print(f"Processing order: {message['orderId']}")

       
        table.put_item(Item=message)

    return {
        'statusCode': 200,
        'body': json.dumps('Order processed successfully')
    }