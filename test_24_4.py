import time
from selenium.webdriver.common.by import By


def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """

    # Open google search page:
    selenium.get('https://google.com')

    time.sleep(3)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for search text input:
    search_input = selenium.find_element(By.CLASS_NAME, 'gLFyf')

    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('Hario')

    time.sleep(3)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search:
    search_button = selenium.find_element(By.CLASS_NAME, 'gNO89b')
    search_button.submit()
    # search_button.click() можно и так кликнуть, а не отпрвить форму

    time.sleep(3)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    selenium.save_screenshot('result.png')

# pytest -v --driver Chrome --driver-path /Users/deniszutaev/PycharmProjects/Skillfactory/chromedriver_mac_arm64/chromedriver test_24_4.py

# вот так верно запускть конкретный файд
# pytest -v --driver Chrome --driver-path driver-path/chromedriver.exe test_24_4.py