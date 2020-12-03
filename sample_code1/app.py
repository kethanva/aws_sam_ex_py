import json

import requests

def lambda_handler(event, context):

    try:
        ip = "10.10.1.1" 
        #requests.get("http://checkip.amazonaws.com/") 
    except requests.RequestException as e:
        print(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "version": 12,
            "ip":ip
#            "ip":ip.text
        }),
    }
