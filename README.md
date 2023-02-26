# Python RESTful API Client
## Installation
First make sure you have python 3.10 installed on your system.

```
$ python --version
Python 3.10.x
```

Then install the required packages
```
pip install requests
```
That's it!

## Help message
```
$ ./pyrac -h
usage: pyrac [-h] [-u URL] [--https] [-m METHOD] [-d JSON] [--data-file FILE] [-r]
             [--force-show-response] [--version]

Python RESTful API Client.

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     (required) url of endpoint
  --https               sets your connection to https
  -m METHOD, --method METHOD
                        sets your connection method. [GET, POST, OPTIONS]
  -d JSON, --data JSON  data that want to be passed in json format
  --data-file FILE      data as a json file
  -r, --allow-redirects
                        allows redirects
  --force-show-response
                        shows response anyways
  --version             shows the version number
```
## Examples
```
./pyrac -u jsonplaceholder.typicode.com/posts -m get --https
```
## License
Licensed by MIT
