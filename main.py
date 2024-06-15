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