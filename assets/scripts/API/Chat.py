from . import List, Dict, Generator, Any, randbelow, UserAgent, requests

def chat(
        CH_API_KEY: str, 
        messages: List[Dict[str, str]], 
        model: str, 
        max_tokens: int = 250, 
        temperature: float = 0.8, 
        top_p: float = 0.99, 
        frequency_penalty: float = 1.0, 
        presence_penalty: float = 1.0, 
        stream: bool = True,
        stop: List[str] = ['USER:', '#', '[']
    ) -> Generator[Any, Any, Any] | Dict[str, Any]:

    url: str = "https://inference.chub.ai/prompt"

    headers: Dict = {
        "Host": "inference.chub.ai",
        "User-Agent": f"{UserAgent().random}",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CH_API_KEY}",
        "Content-Length": f"{randbelow(2000)}",
        "Origin": "https://venus.chub.ai",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Priority": "u=4",
        "TE": "trailers"
    }

    data: Dict = {
        "messages": messages,
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "frequency_penalty": frequency_penalty,
        "presence_penalty": presence_penalty,
        "stop": stop
    }

    response = requests.post(url, headers=headers, json=data, stream=stream)
    response.raise_for_status()

    if stream:

        for chunk in response.iter_lines():

            if chunk:
                
                yield chunk.decode("utf-8")

    else:
            
        return response.content
    