import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from secrets import randbelow

from fake_useragent import UserAgent

def login(__csrf_token: str, email: str, password: str):

    """
    Login to the chub.ai website.

    Return structure:

    git_id: int
    samwise: str
    subscription: int (range: 0-2)
    username: str

    {
        "git_id": xxxxxxxx,
        "samwise": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "subscription": x,
        "username": "xxxxxxxx"

    }


    :param __csrf_token: The CSRF token
    :param email: The email
    :param password: The password

    :return: The response

    :rtype: requests.models.Response
    """

    url: str = "https://sub.chub.ai/login"
    
    m = MultipartEncoder(
        fields={
            "csrf_token": __csrf_token,
            "email_or_username": email,
            "password": password,
            "oauth": "",
            "state": "",
            "redirect_url": "https://chub.ai/register",
            "is_mobile": "false",
        },
    )

    headers: dict = {
        "Host": "sub.chub.ai",
        "User-Agent": f"{UserAgent().random}",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://venus.chub.ai/",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "True",
        "samwise": "glpat-UZXEBupEVv2vMCdFDkfJ",
        "Content-Type": m.content_type,
        "Content-Length": f"{randbelow(1200)}",
        "Origin": "https://venus.chub.ai",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Priority": "u=4",
        "TE": "trailers"
    }

    response = requests.post(url, headers=headers, data=m)
    response.raise_for_status()

    return response.json()