"""
Модуль selenium_tests содержит три теста с использованием Selenium WebDriver:

- test_register - тест на регистрацию нового аккаунта на странице.
- test_right_click - тест на правый клик и выбор элемента из контекстного меню.
- test_copy_paste - тест на копирование и вставку текста в поле ввода.

"""

# Импортируем библиотеку webdriver из модуля selenium для взаимодействия с браузером
from selenium import webdriver
# Импортируем модуль ActionChains для работы с ActionChains в Selenium WebDriver
from selenium.webdriver import ActionChains
# Импортируем сервис для ChromeDriver
from selenium.webdriver.chrome.service import Service
# Импортируем типы и функции поиска
from selenium.webdriver.common.by import By
# Импортируем клавиши
from selenium.webdriver.common.keys import Keys
# Импортируем модуль WebDriverWait, который предоставляет экземпляр WebDriverWait для ожидания элементов на странице
from selenium.webdriver.support.ui import WebDriverWait
# Импортируем модуль expected_conditions из библиотеки selenium.webdriver.support для работы с ожиданиями
from selenium.webdriver.support import expected_conditions as EC
# Импортируем модуль sleep из стандартной библиотеки time для перерывов между действиями
from time import sleep


def init_webdriver():
    """
    Функция создает и возвращает экземпляр Selenium WebDriver с заданными настройками.

    :return: объект WebDriver.
    """
    # Инициализируем сервис ChromeDriver для браузера Chrome
    driver = Service("Useful_code/chromedriver/")
    # Запускаем браузер Chrome с нашим сервисом
    browser = webdriver.Chrome(service=driver)
    # Ждем 30 секунд пока элементы на странице не будут доступны
    browser.implicitly_wait(30)
    # Устанавливаем максимальное время ожидания, в течение которого страница должна быть загружена
    browser.set_page_load_timeout(50)
    # Возвращаем экземпляр браузера Chrome
    return browser


def test_register():
    """
    Тест на регистрацию нового аккаунта на странице https://qavbox.github.io/demo/signup/.
    Ожидается, что страница загрузится, заголовок содержит слово "Registration", поле имени будет кликабельным.
    В поле ввода записывается значение "YOUR_NAME".
    """
    # Инициализируем веб-драйвер
    browser = init_webdriver()
    # Переход на страницу https://qavbox.github.io/demo/signup/
    browser.get("https://qavbox.github.io/demo/signup/")
    # Получаем элемент поля ввода имени с помощью локатора By.ID и идентификатора 'username'
    username_field = browser.find_element(By.ID, "username")
    # Проверяем, что в заголовке страницы есть слово "Registration"
    assert "Registration" in browser.title
    # Создаем объект ActionChains, на который будем навешивать действия
    action = ActionChains(browser)
    # Нажимаем на поле ввода имени и вводим значение "YOUR_NAME"
    action.click(username_field).send_keys("YOUR_NAME").perform()
    # Задержка выполнения на 2 секунды
    sleep(2)
    # Закрываем браузер
    browser.quit()


def test_right_click():
    """
    Тест на правый клик и выбор элемента из контекстного меню на странице https://swisnl.github.io/jQuery-contextMenu/demo.html.
    Ожидается, что страница загрузится, будет найден элемент с текстом "right click me".
    Выполняется правый клик на элементе, выбирается пункт "Edit", ожидается появление всплывающего окна,
    после закрытия окна браузера происходит завершение теста.
    """
    # Инициализируем веб-драйвер
    browser = init_webdriver()
    # Открываем сайт
    browser.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    # Находим элемент для контекстного меню
    right_click_el = browser.find_element(By.XPATH, "//span[contains(text(), 'right click me')]")
    # Кликаем на элемент правой кнопкой мыши с использованием ActionChains
    ActionChains(browser).context_click(right_click_el).send_keys(Keys.ARROW_DOWN).pause(2).send_keys(
        Keys.ARROW_DOWN).pause(1).send_keys(Keys.ENTER).perform()
    # Ожидаем появления alert
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    # Пауза на 2 секунды
    sleep(2)
    # Нажимаем "OK" на alert
    browser.switch_to.alert.accept()
    # Закрываем браузер
    browser.quit()


def test_copy_paste():
    """
    Тест на копирование и вставку текста в поле ввода на странице https://qavbox.github.io/demo/signup/.
    Ожидается, что страница загрузится, поля ввода будут кликабельные.
    В поле ввода имени вводится значение "YOUR_NAME", затем введенное значение копируется в буфер обмена.
    Значение из буфера обмена вставляется в поле ввода email. Проверяется, что email равен
    введенному значению имени.
    """
    # Инициализируем веб-драйвер
    browser = init_webdriver()
    # Открываем сайт
    browser.get("https://qavbox.github.io/demo/signup/")
    # Находим поле для ввода email
    email_field = browser.find_element(By.ID, "email")
    # Находим поле для ввода имени пользователя
    username_field = browser.find_element(By.ID, "username")
    # Вводим имя пользователя
    username_field.send_keys("YOUR_NAME")
    # Копируем имя пользователя в буфер обмена
    ActionChains(browser).key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
    ActionChains(browser).key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()
    # Пауза на 2 секунды
    sleep(2)
    # Вставляем из буфера обмена имя пользователя в поле email
    ActionChains(browser).click(email_field).key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()
    # Пауза на 2 секунды
    sleep(2)
    # Проверяем, что введенное имя пользователя соответствует значению в поле email
    assert email_field.get_attribute("value") == "YOUR_NAME"
    # Закрываем браузер
    browser.quit()
