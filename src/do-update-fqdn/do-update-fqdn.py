#!/bin/env python3

import json
import urllib.request
import argparse

parser = argparse.ArgumentParser(description='update DO dns record')
parser.add_argument('--token', metavar='do_api_token', type=str, required=True, help='DO API token')
parser.add_argument('--record', metavar='fqdn', type=str, required=True, help='fqdn that should be updated')

cliargs = parser.parse_args()

hostname, dns_domain = cliargs.record.split('.', maxsplit=1)

headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {cliargs.token}'}
api_request = urllib.request.Request(f'https://api.digitalocean.com/v2/domains/{dns_domain}/records/{hostname}',
                                     headers=headers)
api_response = urllib.request.urlopen(api_request).read()

jsondata = json.loads(api_response.decode('utf-8'))
print(jsondata)

# record_id = [rid for rid in jsondata.]
