# API and keys (36-41)

## Imports the requests library
import requests

## Imports the json library
import json

## Imports the load_dotenv() and the os libraries
from dotenv import load_dotenv
load_dotenv()

import os
subscription_key = os.getenv('SUBSCRIPTION_KEY_AZURE_COGNITIVE_SERVICES_COMPUTER_VISION')

vision_service_address = 'https://test-python-api.cognitiveservices.azure.com/vision/v2.0/'
address = vision_service_address + 'analyze'

parameters = {'visualFeatures':'Description,Color',
              'language':'pt'}

image_path = "swiss_cheese.jpg"
image_data = open(image_path, "rb").read()

headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': subscription_key}

response = requests.post(address, headers=headers, params=parameters, data=image_data)

response.raise_for_status()

results = response.json()
print(json.dumps(results))
print()

print('Request Id:', results['requestId'])
print('Image format:',results['metadata']['format'])
for color in results['color']['dominantColors']:
    print('Dominant color:', color)
