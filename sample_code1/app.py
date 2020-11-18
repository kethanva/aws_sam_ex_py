import json

import requests

def lambda_handler(event, context):

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
    except requests.RequestException as e:
        print(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "version": 8,
            "ip":ip.text
        }),
    }
