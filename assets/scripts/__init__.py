from fake_useragent import UserAgent
from secrets import randbelow, token_hex
from requests_toolbelt.multipart.encoder import MultipartEncoder

from typing import Dict, Any
import logging
import requests
import uuid

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# helper functions
def make_fake_mail() -> str:

    """
    Generate a fake email.
    """

    return f"{uuid.uuid4()}@gmail.com"

def make_fake_username() -> str:

    """
    Generate a fake username.
    """

    return f"{uuid.uuid4().hex}"

def make_fake_password() -> str:

    """
    Generate a fake password.
    """

    return "I" + f"{uuid.uuid4().hex}" + "!"

__all__ = [
    "requests",
    "uuid",
    "logging",
    "token_hex",

    "UserAgent",
    "MultipartEncoder",
    "randbelow",
    "make_fake_mail",
    "make_fake_username",
    "make_fake_password",

    "Dict",
    "Any",
]