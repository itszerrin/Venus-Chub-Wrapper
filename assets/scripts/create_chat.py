from . import UserAgent, randbelow, requests

def create_chat(_samwise: str) -> int:

    """
    Create a chat on the chub.ai website and then send a pageview event.

    Return structure:

    id: int

    :param _samwise: The samwise token

    :return: The chat id

    :rtype: int
    """

    url: str = "https://api.chub.ai/api/venus/chats"

    headers = {
        "Host": "api.chub.ai",
        "User-Agent": f"{UserAgent().random}",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://venus.chub.ai/",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "True",
        "CH-API-KEY": _samwise,
        "Origin": "https://venus.chub.ai",
        "Connection": "keep-alive",
        "Content-Length": f"{randbelow(150)}",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Priority": "u=1",
        "TE": "trailers"
    }

    data = {
        'character_id': 'composed_view_3402/reference-endpoint-4dbc6dbef1b4',
        'is_v2': True,
        'scenario_id': None,
        'stage_id': None,
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    __chat_id: int = response.json()["id"]

    # send another post request for the pageview
    __url: str = "https://odo.chub.ai/api/event"

    headers = {
        "Host": "odo.chub.ai",
        "User-Agent": f"{UserAgent().random}",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "text/plain",
        "Content-Length": f"{randbelow(90)}",
        "Origin": "https://venus.chub.ai",
        "Connection": "keep-alive",
        "Referer": "https://venus.chub.ai/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers"
    }

    data = {
        'd': 'chub.ai',
        'n': 'pageview',
        'r': None,
        'u': f'https://venus.chub.ai/chats/{__chat_id}',
    }

    response = requests.post(__url, headers=headers, json=data)
    response.raise_for_status()

    return __chat_id
