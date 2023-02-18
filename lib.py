import json
import argparse
import requests


class UI:
    b = '\033[1m'
    ok = '\033[92m' + b
    w = '\033[93m' + b
    f = '\033[91m' + b
    e = '\033[0m'


ui = UI


class ArgumentParser:
    def __init__(self, version) -> None:
        self.version = version

    def arg_parser():
        parser = argparse.ArgumentParser(
            prog="rac",
            description="RESTful API Client.",
        )
        parser.add_argument('-u', '--url', help="url of endpoint")
        parser.add_argument('--https',
                            help='(optional) sets your connection to https', action='store_true')
        parser.add_argument('-m', '--method',
                            help='(optional) sets your connection method. [GET, POST]')
        parser.add_argument('-d', '--data',
                            help='(optional) data that want to be passed in json format', metavar='JSON')
        parser.add_argument('--data-file',
                            help='(optional) data as a json file', metavar='FILE')
        # FIXME
        # parser.add_argument('--version', help="shows the version number",
        #                     action="version", version='%(prog)s v{version}'.format(version=version))
        args = parser.parse_args()
        return args

    args = arg_parser()
    if args.url is None:
        print(f'{ui.f}[!] --url is required{ui.e}')
        exit(1)
    is_https = 's' if args.https is True else ''
    match str(args.method).lower():
        case 'get':
            method = 'get'
        case 'post':
            method = 'post'
        case default:
            print(
                f'{ui.w}[!] Setting METHOD to default (GET).{ui.e}')
            method = 'get'
    try:
        data = json.dumps(args.data) if args.data is not None else json.loads(
            open(args.data_file, 'r').read())
    except:
        data = None


class Request:

    def __init__(self, endpoint, argparser) -> None:
        self.endpoint = endpoint
        self.argparser = argparser

    def request(self):
        print(f'[ {self.argparser.method.upper()} ]', self.endpoint)
        self.res = requests.get(self.endpoint) if self.argparser.method == 'get' else requests.post(
            self.endpoint, data=self.argparser.data
        )
        if self.res.status_code == 200:
            print(ui.ok + '[+] Connected.' + ui.e)
            print(self.res.json())
            print(f'{ui.ok}[+] JSON Data Found.{ui.e}')
        elif self.res.status_code == 201:
            print(ui.ok + '[+] Posted!' + ui.e)
        elif self.res.status_code == 400:
            print(f'{ui.f}[-] 400 Client error.{ui.e}')
        elif self.res.status_code == 404:
            print(f'{ui.f}[-] 404 Not found.{ui.e}')
        elif self.res.status_code == 405:
            print(
                f'{ui.f}[-] 405 Method is not allowed on this endpoint.{ui.e}')
        elif self.res.status_code == 415:
            print(f'{ui.f}[-] 415 Unsupported format.{ui.e}')
