from lib import lib

from requests.exceptions import ConnectionError
from json.decoder import JSONDecodeError

__version__ = '0.2.0'


def main():
    try:
        argparser = lib.ArgumentParser(__version__)
        ui = lib.UI()
        endpoint = f'http{argparser.is_https}://{argparser.args.url}'
        rq = lib.Request(endpoint, argparser)
        rq.run()
    except ConnectionError:
        print(f'{ui.f}[-] There was an error to connect to the endpoint.{ui.e}')
    except JSONDecodeError:
        print(rq.res.text)
        rq.qprint(f'{ui.w}[!] JSON Decode failed, raw response printed.{ui.e}')

if __name__ == '__main__':
    main()
