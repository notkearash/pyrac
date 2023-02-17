#!/usr/bin/env python3
import lib

from requests import get, post
from requests.exceptions import ConnectionError
from json.decoder import JSONDecodeError

__version__ = '0.1.0'

argparser = lib.ArgumentParser(__version__)
ui = lib.UI()

endpoint = f'http{argparser.is_https}://{argparser.args.url}:{argparser.args.port}'
try:
    print(f'[ {argparser.method.upper()} ]', endpoint)
    res = get(endpoint) if argparser.method == 'get' else post(endpoint)
    if res.status_code == 200:
        print(ui.ok + '[+] Connected.' + ui.e)
        print(res.json())
        print(f'{ui.ok}[+] JSON Data Found.{ui.e}')
    elif res.status_code == 404:
        print(f'{ui.f}[-] 404 Not found.{ui.e}')
except ConnectionError:
    print(f'{ui.f}[-] There was an error to connect to the endpoint.{ui.e}')
except JSONDecodeError:
    print(res.text)
    print(
        f'{ui.w}[!] Unable to decode to JSON, Printed the raw response.{ui.e}')
