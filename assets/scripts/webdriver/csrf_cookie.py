from . import driver, sleep

def get_csrf_cookie() -> str:

    """
    Get the CSRF cookie from the login page.

    NOTE: THIS DOESN'T CLOSE THE DRIVER.
    """

    driver.get("https://venus.chub.ai/login")
    sleep(2)
    cookie = driver.get_cookies()[1]['value']

    # unload site
    driver.get('about:blank')

    return str(cookie)
