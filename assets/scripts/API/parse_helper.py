from json import loads

def parse_for_content(chunk) -> str:

    if chunk:

        try:

            return loads(chunk.removeprefix("data: "))["choices"][0]["delta"]["content"]
        
        except:

            return ''
