import json
import boto3
import uuid
from os import environ
from datetime import datetime, timedelta
import jwt

USERS_TABLE = environ.get('USERS_TABLE', 'users_mechshop_api')
JWT_SECRET = environ.get('JWT_SECRET', 'm3chsh0p_4p1')

dynamodb = boto3.resource('dynamodb')
users_table = dynamodb.Table(USERS_TABLE)

def handler(event, context):

    try: 
        body = json.loads(event.get('body'))

        user_id = str(uuid.uuid1())

        user = {
            'id': user_id,
            'first_name': body.get('first_name'),
            'last_name': body.get('last_name'),
            'email': body.get('email'),
            'password': body.get('password'),
            'created_at': datetime.now().isoformat()
        }

        users_table.put_item(Item=user)

        # Generate authentication token for user
        expires_in = datetime.utcnow() + timedelta(seconds=3600)

        token = jwt.encode({
            'user_id': user_id, 'exp': expires_in 
        }, 
            JWT_SECRET,
            algorithm='HS256'
        )

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
        return {
            'statusCode': 500,
            'headers': {
                'content-type': 'application/json',
                'access-control-allow-origin': '*',
            },
            'body': json.dumps({
                'message': str(e)
            })
        }
