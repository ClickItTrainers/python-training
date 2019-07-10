def on_launch(request, session):
    """
        Called when the user launches the skill without specifying what they want
    """
    return welcome_response()

def on_intent(request, session):
    """
        Called when the user specifies an intent for this skill
    """
    intent = request['intent']
    intent_name = request['intent']['name']

    if intent_name == 'test':
        return test_response()
    elif intent_name == 'AMAZON.HelpIntent':
        return welcome_response()
    if intent_name == 'AMAZON.CancelIntent' or intent_name == 'AMAZON.StopIntent':
        return goodbye_response()
    else:
        raise ValueError('Invalid intent')
    
def on_session_ended(request, session):
    """
        Called when the user want to exit from the application
    """
    return goodbye_response()


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def test_response():
    session_attributes = {}
    card_title = 'Test'
    speech_output = 'Esto es un mensaje de Prueba'
    reprompt_text = 'No me respondiste, pero esto es un mensaje de prueba'
    should_end_session = False

    return build_response(
        session_attributes,
        build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session)
    )

def welcome_response():
    session_attributes = {}
    card_title = "Bienvenido"
    speech_output = "Bienvenido a tu aplicacion personalizada de Alexa!"
    reprompt_text = "Tal vez no me escuchaste, pero bienvenido a tu app personalizada de Alexa!"
    should_end_session = False

    return build_response(
        session_attributes,
        build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session)
    )

def goodbye_response():
    session_attributes = {}
    card_title = 'Hasta luego'
    speech_output = 'Hasta luego, gracias por conversar conmigo'
    reprompt_text = 'Tal vez no me escuchaste, pero hasta luego'
    should_end_session = True

    return build_response(
        session_attributes,
        build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session)
    )

def lambda_handler(event, context):
    """
        Route the incoming request based on type (LaunchRequest, IntentRequest, etc.)
        The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")

    if event['session']['new']:
        # Called when a session starts. 
        # Possible use is to generate data before the launching of your skill.
        pass
    
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    if event['request']['type'] == 'IntentRequest':
        return on_intent(event['request'], event['session'])
    #if event['request']['type'] == 'SessionEndedRequest':
    #    return on_session_ended()