#!/usr/bin/env python3
import requests
import json
import sys
from pprint import pprint
from requests.auth import HTTPBasicAuth

# disable insecure ssl requests warnings
import urllib3
urllib3.disable_warnings()

ovirtusername='changeme'
ovirtpassword='changeme'
ovirthost='changeme01.tld.com'


def listvms(findvm):
    headers={'Accept': 'application/json'}
    r = requests.get('https://%s/ovirt-engine/api/vms' % ovirthost, auth=HTTPBasicAuth(ovirtusername, ovirtpassword), verify=False, headers=headers)
    data = r.json()
    for vm in data['vm']:
        if findvm in vm['fqdn']:
            print("name:%s ; status:%s ; cores:%s ; mem:%s\n" % (vm['fqdn'], vm['status'], vm['cpu']['topology']['cores'], int(vm['memory']) / (1024.0 * 1024.0)))

def main():
    if len(sys.argv) > 1:
        findvm=sys.argv[1]
    else:
        findvm=''
    listvms(findvm)


if '__main__' in __name__:
    main()
