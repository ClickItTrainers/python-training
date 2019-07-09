import boto3
import json
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
users_table = dynamodb.Table('users')

def respond(**kwargs):
    status_code = kwargs.get('StatusCode', 200)
    body = kwargs.get('Body', { 'success': True })
    headers = body.get('Headers', { 'Content-Type': 'application/json' })
    
    if 'Error' in kwargs:
        error = kwargs.get('Error')
        message = str(error)
        status_code = 500
        body = {
            'message': message
        }
    
    return {
        'statusCode': status_code,
        'headers': headers,
        'body': json.dumps(body)
    }

def lambda_handler(event, context):
    
    """
    Description: Users Endpoint for Creation & Read of these.
    URL: /users
    Methods: GET, POST, DELETE
    """

    print('Incoming request: {}'.format(str(event)))
    
    if event['httpMethod'] == 'POST':
        
        """ We get the incoming data from the request and create a new id for new user """
        body = json.loads(event.get('body'))
        user_id = str(uuid.uuid1()).replace('-', '')
        
        user = {
            'id': user_id,
            'email': body.get('email'),
            'first_name': body.get('first_name'),
            'last_name': body.get('last_name'),
            'created_at': datetime.now().isoformat()
        }
        
        try:
            response = users_table.put_item(Item=user)
            
            return respond(Body={
                'success': True,
                'payload': {
                    'userId': user_id,
                    'email': user.get('email')
                }
            })
            
        except Exception as e:
            
            return respond(Error=e)
    elif event['httpMethod'] == 'GET':

        """ If the incoming request includes the user id as a parameter
            we search that user specifically and return it
        """
        if event['pathParameters'] != None and 'user' in event['pathParameters']:
            user_id = event['pathParameters']['user']

            print('getting-user id={}'.format(user_id))

            try:

                response = users_table.get_item(Key={ 'id': user_id })

                return respond(Body={
                    'success': True,
                    'user': response['Item']        
                })
            except Exception as e:
                return respond(Error="Cannot retrieve user. Reason {}".format(str(e)))

        """ Scan DynamoDB Table to get all Users. """
        response = users_table.scan()

        """ As we don't know the amount of users in our table we do a while cause dynamo by default
            paginates the incoming data to limit each batch to 1MB
            Resource:
            https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.scan
        """
        items = response['Items']

        while True:
            if response.get('LastEvaluatedKey'):
                response = users_table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                items += response['Items']
            else:
                break

        return respond(
            Body={
                'success': True,
                'data': items
            }
        )
    elif event['httpMethod'] == 'DELETE' and 'user' in event['pathParameters']:
        user_id = event['pathParameters']['user']

        try :
            response = users_table.delete_item(
                Key={ 'id': user_id }
            )

            return respond(Body={
                'success': True
            })
        except Exception as e:
            return respond(Error=e)
    else:
        return respond(
            StatusCode=400,
            Body={
                'message': 'Method not allowed!'    
            }
        )
