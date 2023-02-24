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
    def arg_parser(self):
        parser = argparse.ArgumentParser(
            prog="rac",
            description="RESTful API Client.",
        )
        parser.add_argument('-u', '--url', help="(required) url of endpoint")
        parser.add_argument('--https',
                            help='sets your connection to https', action='store_true')
        parser.add_argument('-m', '--method',
                            help='sets your connection method. [GET, POST, OPTIONS]')
        parser.add_argument('-d', '--data',
                            help='data that want to be passed in json format', metavar='JSON')
        parser.add_argument('--data-file',
                            help='data as a json file', metavar='FILE')
        parser.add_argument('-r', '--allow-redirects',
                            help="allows redirects", action="store_true")
        parser.add_argument('--force-show-response',
                            help="shows response anyways", action="store_true")
        parser.add_argument('--version', help="shows the version number",
                            action="version", version='%(prog)s v{version}'.format(version=self.version))
        args = parser.parse_args()
        return args

    def __init__(self, version) -> None:
        self.version = version
        self.args = self.arg_parser()
        self.is_https = 's' if self.args.https is True else ''

        if self.args.url is None:
            print(f'{ui.f}[!] --url is required{ui.e}')
            exit(1)

        match str(self.args.method).lower():
            case 'get':
                self.method = 'get'
            case 'post':
                self.method = 'post'
            case 'options':
                self.method = 'options'
            case default:
                print(
                    f'{ui.w}[!] Setting METHOD to default (GET).{ui.e}'
                )
                self.method = 'get'

        try:
            self.data = json.dumps(self.args.data) if self.args.data is not None else json.loads(
                open(self.args.data_file, 'r').read())
        except:
            self.data = None


class Request:

    def __init__(self, endpoint, argparser) -> None:
        self.endpoint = endpoint
        self.argparser = argparser

    @staticmethod
    def eprint(msg, exit_code=0, end="\n"):
        print(msg, end=end)
        exit(exit_code)

    def request(self):
        print(f'[ {self.argparser.method.upper()} ]', self.endpoint)
        match self.argparser.method:
            case 'get':
                self.res = requests.get(
                    self.endpoint,
                    allow_redirects=self.argparser.args.allow_redirects
                )
            case 'post':
                self.res = requests.post(
                    self.endpoint,
                    data=self.argparser.data,
                    allow_redirects=self.argparser.args.allow_redirects
                )
            case 'options':
                self.res = requests.options(
                    self.endpoint,
                    allow_redirects=self.argparser.args.allow_redirects
                )

    def response_handler(self):
        match self.res.status_code:
            case 200:
                print(ui.ok + '[+] Connected.' + ui.e)
                print(self.res.json())
                self.eprint(f'{ui.ok}[+] JSON Data Found.{ui.e}')
            case 201:
                self.eprint(ui.ok + '[+] Posted!' + ui.e)
            case 204:
                self.eprint(ui.ok + '[+] 204 No Content.' + ui.e)
            case 302:
                self.eprint(
                    ui.w + "[!] 302 Temporarily moved to: " +
                    self.endpoint + self.res.headers['Location'] +
                    f"\n[!] Use {ui.f}-r{ui.e}{ui.w} to allow redirects" + ui.e
                )
            case 304:
                self.eprint(
                    ui.w + '[!] 304 Not modified. No need to retransmit.' + ui.e
                )
            case 400:
                self.eprint(f'{ui.f}[-] 400 Client error.{ui.e}', 1)
            case 403:
                self.eprint(ui.f + '[-] 403 Forbidden.' + ui.e)
            case 404:
                self.eprint(f'{ui.f}[-] 404 Not found.{ui.e}', 1)
            case 405:
                self.eprint(
                    f'{ui.f}[-] 405 Method is not allowed on this endpoint.{ui.e}', 1
                )
            case 413:
                self.eprint(ui.f + '[-] 413 Content Too Large' + ui.e, 1)
            case 415:
                self.eprint(f'{ui.f}[-] 415 Unsupported format.{ui.e}', 1)
            case 418:
                self.eprint(
                    ui.b + '[???] 418 You are connected to a...teapot?!' + ui.e, 1
                )
            case 429:
                self.eprint(ui.f + '[-] 429 Too many requests.' + ui.e, 1)

    def run(self):
        self.request()
        if self.argparser.args.force_show_response:
            print(ui.w + '[!] FORCE SHOW RESPONSE ENABLED' + ui.e)
            print('====RESPONSE====')
            print(self.res.text)
            print('====END-RESP====')
        self.response_handler()
