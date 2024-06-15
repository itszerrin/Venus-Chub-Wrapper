from . import driver, sleep, By

def get_mars_token(username: str, password: str, chat_id: str | int) -> str:

    """
    Get the MARS token from the chat page.
    
    NOTE: THIS DOESN'T CLOSE THE DRIVER.
    
    :param username: The username.
    :param password: The password.
    :param chat_id: The chat ID.
    
    :return: The MARS token.
    
    :rtype: str
    """

    driver.get(f"https://chub.ai/login")
    sleep(4)

    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element("xpath", "//button[@type='submit']").click()
    sleep(5)

    driver.get(f"https://chub.ai/chats/{chat_id}")
    sleep(4)

    # print localstorage
    try:    return driver.execute_script("return window.localStorage;")["MARS_TOKEN"]
    except KeyError:   print("MARS_TOKEN not found in localstorage. The Chat page hasn't loaded properly. Exiting..."); exit(1)
