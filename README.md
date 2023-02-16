# RESTful API Client
---
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
usage: rac [-h] [-u URL] [-p PORT] [--https] [-m METHOD] [--version]

RESTful API Client.

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     url of endpoint
  -p PORT, --port PORT  (optional) port of endpoint
  --https               (optional) sets your connection to https
  -m METHOD, --method METHOD
                        (optional) sets your connection method. [GET, POST]
  --version             shows the version number
```
## Examples
```
python3 rac.py -u localhost -p 3000
```

## Notes
+ Dirty and quick project
+ But still usable
+ ~~maybe ill work on it~~

## License
Licensed by MIT
