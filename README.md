# Venus-Chub-Wrapper
A Wrapper for https://venus.chub.ai to create accounts and access premium LLMs using local Python scripts.

# Table of Contents
1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Using the Script](#using-the-script)
4. [Registering an Account](#registering-an-account)
5. [Logging In](#logging-in)
6. [Creating a Dummy Chat](#creating-a-dummy-chat)
7. [Getting Your API Key Automatically](#getting-your-api-key-automatically)
8. [Closing the Webdriver](#closing-the-webdriver)
9. [Example 1 - Getting Your API Key](#example-1-getting-your-api-key)
10. [Chatting with Chub's LLMs](#chatting-with-chubs-llms)
11. [Example 2 - Full Code to Chat](#example-2-full-code-to-chat)

## Introduction

1. **Purpose**

The purpose of this script is to demonstrate the capabilities of reverse-engineering with Python. This project is purely for educational purposes and falls under the [GPL-3 License](LICENSE.MD). For more information, you may always contact me under zerrin@zerrin.online

This README is beginner-friendly and step-by-step. It takes the process slowly.

2. **Execution**

This simple project utilizes modules such as ``selenium``, ``requests`` and a bit of exploiting the site's security vulnerabilities and inconsistencies. Adding Cloudflare also won't help - I'll only have to use nodriver instead of selenium

## Set up

1. **Installing needed dependencies**

Run ``git clone https://github.com/Recentaly/Venus-Chub-Wrapper.git``

Install the dependencies by opening a console in the **Venus-Chub-Wrapper** directory and running ``pip install -r requirements.txt``

## Using the script

For context, an **example script** is **NOT** provided. This project only ships individual code snippets to **register** an account, **fetch your Mars Token**, **log in**, and so on. You'll need to make your own **main.py** but this script will guide you in the process.

To start off, create a **main.py** in the root of the project.

## Section 1: Registering an account

Registering requires only 2 imports. View below and copy these into your main.py. The first one is needed to get a Cloudflare Cross-Site request forgery token and the second one is the registering function itself.

```py
from assets.scripts.webdriver.csrf_cookie import get_csrf_cookie
from assets.scripts.register import register
```

(Optional)

```py
from assets.scripts import make_fake_mail, make_fake_password, make_fake_username
```

`make_fake_mail`: Returns a UUIDv4 + "@gmail.com" at the end. <br>
`make_fake_password`: Returns a capital I + a UUIDv4 + "!" (to meet password criteria) <br>
`make_fake_username`: Simply returns a UUIDv4 string.

This is the first security flaw: Unverified email adresses, even ones completely made up (for example: ihatechildren@trollmailjamaica.com) are permitted and get free API credits.

Here's an example way to run the code:

```py
from assets.scripts.webdriver.csrf_cookie import get_csrf_cookie
from assets.scripts.register import register

# get csrf token
__csrf_token: str = get_csrf_cookie()

# register
register_response = register(fake_email, fake_password, fake_username, fake_username, __csrf_token)
```

This registers a burner account and copies the response from the Chub API. Here's an example format of `register_response`:

```json
{
    "git_id": 73017801,
    "samwise": "2949skqo-901d-4f87-b22b-7c9b03221baf",
    "username": "ihatechildren"
}
```

The only real important object we need is the `samwise` token. It is used for authentication.

## Section 2: Logging in

Logging in is relatively easy but not needed mostly. Import following modules:

```py
from assets.scripts.webdriver.csrf_cookie import get_csrf_cookie
from assets.scripts.login import login
```

To log in, you need following parameters ready:

- Your csrf cookie. Get it by calling ``get_csrf_cookie()``
- The email you registered with
- Your password

Then, call the login function

```py
login_response = login(csrf_cookie, email, password)
```

This is the resulting output format as an example:

```json
{
  "git_id": 73017801,
  "samwise": "2949skqo-901d-4f87-b22b-7c9b03221baf",
  "subscription": 0,
  "username": "guatemalafan45"
}
```

Use this to get the important `samwise` token if you have an existing account.

## Section 3: Creating a dummy chat.

Now we need to set up a dummy chat. I have already created a bot for this which will be used to start a chat with. We need to start a chat because the API key isn't initialized until the user starts a chat. The code won't work if my dummy bot under the endpoint `composed_view_3402/reference-endpoint-4dbc6dbef1b4` is deleted. However, you can put any public bot's route here. I recommend a light bot so there webdriver doesn't need to handle a lot of token-traffic. A webdriver will then log in, visit the chat and fetch the API key before swiftly closing.

Imports:

```py
from assets.scripts.create_chat import create_chat
```

Run the function. Preferably after registering. Here's an example snippet:

```py
from assets.scripts.register import register
from assets.scripts.webdriver.csrf_cookie import get_csrf_cookie
from assets.scripts.create_chat import create_chat

__csrf_cookie = get_csrf_cookie()

# register
register_response = register(fake_email, fake_password, fake_username, fake_username, __csrf_cookie)

# make new chat
chat_id: int = create_chat(register_response["samwise"])
```

The `create_chat` method requires a `samwise` token you get from registering or logging in. The `create_chat` function sends two requests - One to create the chat resource and one for the pageview.

## Section 4: Getting your API key automatically

To chat with the Mars or Mercury LLMs with a burner account or existing account, we still need to fetch our API key. Luckily, the `get_mars_token` function does this for us. It's called "get_mars_token" but the token is usable for all models.

First, import the needed module

```py
from assets.scripts.webdriver.mars_token import get_mars_token
```

Then, get your token by calling the function like this:

```py
# get mars token for chat
MARS_TOKEN: str = get_mars_token(fake_email, fake_password, chat_id)
```

## Section 5: Closing the webdriver

The webdriver process will live on if you don't shut it down! There's a function for that too.

Import it via:

```py
from assets.scripts.webdriver import close_driver
```

And then call the function `close_driver`. Do this **AFTER** having fetched your API key.

## Section 6: Example 1 - Getting your API key.

Here's a full-code example to get your API key:

```py
from assets.scripts.webdriver.mars_token import get_mars_token
from assets.scripts.webdriver.csrf_cookie import get_csrf_cookie
from assets.scripts.webdriver import close_driver

from assets.scripts.register import register
from assets.scripts.login import login

from assets.scripts.API.Chat import chat
from assets.scripts.API.parse_helper import parse_for_content

from assets.scripts.create_chat import create_chat

from assets.scripts import make_fake_mail, make_fake_password, make_fake_username


fake_username: str = make_fake_username()
fake_email: str = make_fake_mail()
fake_password: str = make_fake_password()

# get csrf token
__csrf_token: str = get_csrf_cookie()

# register
register_response = register(fake_email, fake_password, fake_username, fake_username, __csrf_token)


# make new chat
chat_id: int = create_chat(register_response["samwise"])

# get mars token for chat
MARS_TOKEN: str = get_mars_token(fake_email, fake_password, chat_id)

# close the webdriver
close_driver()

print(MARS_TOKEN)
```

Output (Note: The selenium logging has been intentionally left out for flooding. Parts of the sensitive information have been redacted using "x"s.)

```bash
[...]
2024-06-15 23:16:07,554 - root - INFO - Registering with email: d4d1869b-424a-xxxx-xxxx-xxxxxxxxxxxx@gmail.com, password: I5ba08d2cc5exxxxxxxxxxxxxxxxxxxxx!, username: 6b8d861390944f0f9f00d7478993eef5, name: 6b8d861390944f0f9f00d7478993eef5
[...]
CHK-2STMC397I00589C0Q5X6Uxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Section 7: Chatting with Chub's LLMs.

Now that we have our (burner) API key with 60 free requests, we can chat with the hosted LLMs.

The imports are:

```py
from assets.scripts.API.Chat import chat
```

(Optional - Recommended for streaming)

```py
from assets.scripts.API.parse_helper import parse_for_content
```

The optional module is able to extract the token from an event-stream chunk. This is good to always parse words out of an incoming stream instead of having to manually do it.

Here's an example chat call:

```py
for chunk in chat(
    MARS_TOKEN, # you need to get your API key first as well.
    [
        {
            "role": "system",
            "content": "You're a helpful assistant."
        },
        {
            "role": "user",
            "content": "Yo."
        }
    ],
    model="mixtral", # model choices: mixtral, mistral, mobile, asha, mythomax
    max_tokens=100, # goes from 1 to 2048.
):

    print(parse_for_content(chunk), end='', flush=True)
```

Output:

```
I'm a web developer from the UK. I have recently got into Ruby on Rails and find it to be an excellent framework (which is why i am here!).

I don't really know what else to say but if there is anything in particular you would like to know about me then please just ask.

I look forward to getting to know some of you!
```

Yeah.. it's talking a bunch of bullshit. Well, these models are RP-tuned anyways so experiment with your prompting. I personally can't help but you just need to slip the model into the persona of a ChatGPT-like assistant and that'll hopefully do the job.

### Parameters:

The `chat` function takes following parameters:

```ruby
CH_API_KEY: str, # your API key
messages: List[Dict[str, str]], # A list of messages in OpenAI format.
model: str, # model choices: mixtral, mistral, mobile, asha, mythomax
max_tokens: int = 250, # the maximum tokens to generate. Goes up to 2048 (Unconfirmed)
temperature: float = 0.8, # the randomness of the generation. 0-2
top_p: float = 0.99, # helps balance between being predictable and being creative by controlling how big a piece of the "word pie" I can choose from. (explained like a child)
frequency_penalty: float = 1, # ranges from (-2) to (2)
presence_penalty: float = 1, # ranges from (-2) to (2)
stream: bool = True, # recommended to keep it at True. False seems to be buggy mostly.
stop: List[str] = ['USER:', '#', '['] # stopping sequences. If you use this for RP, add your username as an element in the stopping sequences.
```

### Output formats:

Here's the chunk format if you don't parse it using the supplemented function:

`data: {"id": "459e62e9-bb18-423f-9403-079cdd9c597a", "object": "chat.completion", "created": "26", "model": "mixtral", "choices": [{"delta": {"content": "<a token will appear here>"}`

The last chunk:

`data: [DONE]`

## Section 8: Example 2 - Full code to chat.

```py
from assets.scripts.webdriver.mars_token import get_mars_token
from assets.scripts.webdriver.csrf_cookie import get_csrf_cookie
from assets.scripts.webdriver import close_driver

from assets.scripts.register import register

from assets.scripts.API.Chat import chat
from assets.scripts.API.parse_helper import parse_for_content

from assets.scripts.create_chat import create_chat

from assets.scripts import make_fake_mail, make_fake_password, make_fake_username


fake_username: str = make_fake_username()
fake_email: str = make_fake_mail()
fake_password: str = make_fake_password()

# get csrf token
__csrf_token: str = get_csrf_cookie()

# register
register_response = register(fake_email, fake_password, fake_username, fake_username, __csrf_token)

# make new chat
chat_id: int = create_chat(register_response["samwise"])

# get mars token for chat
MARS_TOKEN: str = get_mars_token(fake_email, fake_password, chat_id)

# close the webdriver
close_driver()


# chat with mars
for chunk in chat(
    MARS_TOKEN,
    [
        {
            "role": "system",
            "content": "You're a helpful assistant."
        },
        {
            "role": "user",
            "content": "Yo. Say hi please."
        }
    ],
    model="mixtral",
    max_tokens=100,
):

    print(parse_for_content(chunk), end='', flush=True)
```



