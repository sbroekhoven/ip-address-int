import sys
import os
import hashlib
import datetime
import socket
import json
import requests
from pathlib import Path
import pandas as pd
from dotenv import dotenv_values

# Cload configuration from .env file
config = dotenv_values(".env")

filepath = sys.argv[1]
if not os.path.isfile(filepath):
    print("File path {} does not exist. Exiting...".format(filepath))
    sys.exit()

hash = hashlib.sha256()
with open(filepath, 'rb') as file:
    buffer = file.read()
    hash.update(buffer)

input_filename = Path(filepath)
output_file_json = filename_replace_ext = input_filename.with_suffix('.json')
output_file_csv = filename_replace_ext = input_filename.with_suffix('.csv')
print(output_file_json)
print(output_file_csv)

print(hash.hexdigest())
print(f'Hash generated at { datetime.datetime.utcnow()}')

with open(filepath) as fp:
    for line in fp:
        ip_address = format(line.strip())
        try:
            socket.inet_aton(ip_address)
        except socket.error:
            continue

        # Defining the api-endpoint
        url = 'https://api.abuseipdb.com/api/v2/check'

        querystring = {
            'ipAddress': ip_address,
            'maxAgeInDays': '90'
        }

        headers = {
            'Accept': 'application/json',
            'Key': config.get("ABUSEIPDB_KEY")
        }

        response = requests.request(method='GET', url=url, headers=headers, params=querystring)

        # Formatted output
        decodedResponse = json.loads(response.text)

        if decodedResponse["data"]['abuseConfidenceScore'] > 0:
            print(json.dumps(decodedResponse, sort_keys=True, indent=2))


