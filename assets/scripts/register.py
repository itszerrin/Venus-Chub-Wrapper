from . import logging, requests, UserAgent, randbelow, MultipartEncoder, Dict, Any

def register(email: str, password: str, username: str, name: str, __csrf_token: str) -> Dict[str, Any]:

    """
    Register to the chub.ai website.

    Return structure:

    {
        "git_id": int
        "samwise": str
        "username": str
    }

    :param email: The email
    :param password: The password
    :param username: The username
    :param name: The name
    :param __csrf_token: The CSRF token

    :return: The JSON response
    """

    logging.info("Registering with email: %s, password: %s, username: %s, name: %s", email, password, username, name)

    url: str = "https://sub.chub.ai/register"

    m = MultipartEncoder(
        fields={
            "csrf_token": __csrf_token,
            "username": username,
            "name": name,
            "email": email,
            "password": password,
            "username": username,
            "redirect_url": "https://chub.ai/register",
            "is_venus": "TRUE",
            "is_mobile": "WHO CARES",
            "state": "",
        },
    )

    headers: dict[str, str] = {
        "Host": "sub.chub.ai",
        "User-Agent": f"{UserAgent().random}",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://venus.chub.ai/",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "True",
        "samwise": "glpat-UZXEBupEVv2vMCdFDkfJ",
        "Content-Type": m.content_type, # type: str
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
