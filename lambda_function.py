import json

def lambda_handler(event, context):
    message = event['queryStringParameters']['message']
    response_message = "Hello, you said: " + message
    return {
        "statusCode": 200,
        "headers": { "Access-Control-Allow-Origin": "*" },
        "body": json.dumps({
            "response": response_message
        })
    }
