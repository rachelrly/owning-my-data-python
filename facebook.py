import json
import datetime
import ipaddress


def print_facebook_activity():
    #open file
    d = open('data/account_activity.json', )
    #convert to python
    data = json.load(d)

    for i in data['account_activity']:
        ts = datetime.datetime.fromtimestamp(i['timestamp'])
        a = i.get('action')
        c = i.get('city')
        s = i.get('region')
        print(f'{a} {ts} from {c}, {s}')

    d.close()


# print_facebook_activity()


def print_ip_activity():
    d = open('data/used_ip_addresses.json', )
    data = json.load(d)

    for i in data['used_ip_address']:
        ts = datetime.datetime.fromtimestamp(i['timestamp'])
        ip = ipaddress.ip_interface(i.get('ip'))
        print(f'{ts} : {ip}')


#print_ip_activity()