import json
import boto3
import uuid

dynamo_db = boto3.resource('dynamodb')
dynamo_db_client = boto3.client('dynamodb')
items_table = dynamo_db.Table('items_mechshop_api')
paginator = dynamo_db_client.get_paginator('scan')

def handler(event, context):

    if event['httpMethod'] == 'GET':

        # response = paginator.paginate(
        #     TableName='mechshop_items',
        #     Select='ALL_ATTRIBUTES',
        #     PaginationConfig={
        #         'PageSize': 6
        #     }
        # )

        response = items_table.scan()

        print(response);

        return {
            'statusCode': 200,
            'headers': { 
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*', 
            },
            'body': json.dumps({
                'success': True,
                'payload': {
                    'items': response['Items'],
                }
            })
        }

    if event['httpMethod'] == 'POST':
        body = json.loads(event['body'])

        print(body)

        item_id = str(uuid.uuid1())
        item = {
            'id': item_id,
            'title': body.get('title'),
            'price': body.get('price'),
            'description': body.get('description'),
        }

        items_table.put_item(Item=item)

        return {
            'statusCode': 200,
            'headers': { 
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*', 
            },
            'body': json.dumps({
                'success': True,
                'payload': {
                    'itemId': item_id,
                }
            })
        }
    else:
        return {
            'statusCode': 402,
            'body': 'Method not allowed!'
        }