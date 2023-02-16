#!/usr/bin/env python3
import argparse

from requests import get, post
from requests.exceptions import ConnectionError
from json.decoder import JSONDecodeError

__version__ = '0.1.0'


class UI:
    b = '\033[1m'
    ok = '\033[92m' + b
    w = '\033[93m' + b
    f = '\033[91m' + b
    e = '\033[0m'


ui = UI


def arg_parser():
    parser = argparse.ArgumentParser(
        prog="rac",
        description="RESTful API Client.",
    )
    parser.add_argument('-u', '--url', help="url of endpoint")
    parser.add_argument('-p', '--port',
                        help="(optional) port of endpoint", default=80)
    parser.add_argument('--https',
                        help='(optional) sets your connection to https', action='store_true')
    parser.add_argument('-m', '--method',
                        help='(optional) sets your connection method. [GET, POST]')
    parser.add_argument('--version', help="shows the version number",
                        action="version", version='%(prog)s v{version}'.format(version=__version__))
    args = parser.parse_args()
    return args


args = arg_parser()
is_https = 's' if args.https is True else ''
match str(args.method).lower():
    case 'get':
        method = 'get'
    case 'post':
        method = 'post'
    case default:
        print(f'{ui.w}[!] Setting METHOD to default (GET).{ui.e}')
        method = 'get'


endpoint = f'http{is_https}://{args.url}:{args.port}'
try:
    print(f'[ {method.upper()} ]', endpoint)
    res = get(endpoint) if method == 'get' else post(endpoint)
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
