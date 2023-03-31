#!/usr/bin/python3
"""
    # Script that fetches https://alx-intranet.hbtn.io/status
    #status
"""
from urllib.request import urlopen
from sys import argv


def requestId():
    """opening url and performing task"""
    with urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))


if __name__ == '__main__':
    requestId()
