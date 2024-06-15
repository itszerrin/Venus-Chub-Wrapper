from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# create a webdriver
__options = webdriver.ChromeOptions()
__options.add_argument("--headless")
__options.add_argument("--disable-gpu")
__options.add_argument("--no-sandbox")
__options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=__options)

def close_driver() -> None:

    """
    Kills the Chrome driver. You need to run this function after you're done with the driver.
    """

    driver.quit()

__all__ = [
    'driver',
    'sleep',
    'By'
]
