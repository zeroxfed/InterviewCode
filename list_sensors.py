# File: list_sensors.py
# By: 0xFED
#
# This script was written for a simple job interview coding challenge
# The request was to authenticate against the LimaCharlie API (https://limacharlie.io/) with the supplied OID and secret to enumerate the sensor hostnames using Python.
# The requests library was chosen to satisfy the expressed constraint of not using the LimaCharlie Python library. (Cause that would be too easy.)
# 
# Tested on:
# Fedora Linux 40 (Workstation)
# Kernel: 6.10.6-200.fc40.x86_64
# Arch: x86-64
# Python: 3.12.5
# Requests: 2.31.0

import requests
import json

# Credentials (normally shouldnt be hardcoded)
oid = "OID GOES HERE"
secret = "SECRET GOES HERE"

# Endpoints
authurl = "https://jwt.limacharlie.io"
apiurl = "https://api.limacharlie.io/v1/sensors/" +oid

# Authentication routine
def authenticate(authurl):
    try:
        print("[+] Attempting to connect")
        creds = {
            "oid": oid,
            "secret": secret
        }

        response = requests.post(authurl, data=creds)
    except:
        print("[-] Connnection failed")
        exit()

    # To check the response
    print("Received " +str(response.status_code)+"\n")
    jwt = json.loads(response.text)
    retrieve(bearertoken = (jwt["jwt"]))

# Retrieval routine
def retrieve(bearertoken):
    headers = {
        "Authorization": "Bearer " + (bearertoken),  # Replace with your actual bearer token
        "accept": ""  # Adjust as needed if you require a specific accept header
    }
    try:
        print("[+] Attempting to Retrive sensors list")
        response2 = requests.get(apiurl, headers=headers)
        # To check the response
        print("Received " +str(response2.status_code)) # Debugging
        print("\n")
    except:
        print("[-] Connection failed")
        exit()
    print ("[+] Retrieved sensors")
    parse(response2)

# Make things pretty
def parse(response2):
    output = json.loads(response2.text)
    print("\n[+] List of sensors:")
    for sensors in output['sensors']:
        print(sensors['hostname'])

# Let the fun begin    
authenticate(authurl)

