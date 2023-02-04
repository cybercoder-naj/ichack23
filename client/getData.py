import json, pathlib
HOME = pathlib.Path(__file__).parent.absolute()

all_ranges = {}
services = {'amazon':'aws','google':'gcp','azure':'azure'}
ip_fmt = {'amazon':'ip_prefix','google':'ipv4Prefix','azure':'addressPrefix'}
scope_fmt = {'aws':'region','gcp':'scope','azure':''}

def get_co2(service,scope):
    ...


for name in ['amazon','google']:
    with open(HOME/f'../assets/ip-ranges/{name}-ip-ranges.json', 'r') as file:
        data = json.load(file)
        all_ranges.update({prefix[ip_fmt[name]]: get_co2(services[name],prefix[scope_fmt[name]]) for prefix in data["prefixes"]})
