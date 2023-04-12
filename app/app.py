"""Main application file"""
import json
import os


def lambda_handler(event, context):
    """Lambda handler"""
    print(event)
    print(context)
    api_version = os.environ.get("API_VERSION")
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": api_version,
            }
        ),
    }
