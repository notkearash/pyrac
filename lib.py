import argparse

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
        parser.add_argument('-p', '--port',
                            help="(optional) port of endpoint", default=80)
        parser.add_argument('--https',
                            help='(optional) sets your connection to https', action='store_true')
        parser.add_argument('-m', '--method',
                            help='(optional) sets your connection method. [GET, POST]')
        # FIXME
        # parser.add_argument('--version', help="shows the version number",
        #                     action="version", version='%(prog)s v{version}'.format(version=version))
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
            print(
                f'{ui.w}[!] Setting METHOD to default (GET).{ui.e}')
            method = 'get'
