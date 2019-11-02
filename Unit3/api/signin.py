import json
import boto3
from boto3.dynamodb.conditions import Attr
from datetime import datetime, timedelta
from os import environ
import jwt

USERS_TABLE = environ.get('USERS_TABLE', 'users_mechshop_api')
JWT_SECRET = environ.get('JWT_SECRET', 'm3chsh0p_4p1')

dynamodb = boto3.resource('dynamodb')
users_table = dynamodb.Table(USERS_TABLE)

def handler(event, context):
    try:

        body = json.loads(event.get('body'))

        response = users_table.scan(
            FilterExpression=Attr('email').eq(body.get('email'))
        )

        if response['Count'] == 0:
            raise Exception('Wrong email or password!')

        user = response['Items'][0]

        if user.get('password') != body.get('password'):
            raise Exception('Wrong email or password!')

        expires_in = datetime.now() + timedelta(seconds=3600)

        token = jwt.encode({
            'user_id': user.get('id'), 'exp': expires_in
        }, JWT_SECRET, algorithm='HS256')

        return {
            'statusCode': 200,
            'headers': {
                'content-type': 'application/json',
                'access-control-allow-origin': '*',
            },
            'body': json.dumps({
                'success': True,
                'payload': {
                    'token': str(token, 'utf-8')
                }
            })
        }

    except Exception as e:
        print(str(e))

        return {
            'statusCode': 500,
            'headers': {
                'content-type': 'application/json',
                'access-control-allow-origin': '*',
            },
            'body': json.dumps({
                'error': 'Something went wrong, please try it again'
            })
        }
