# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Шаг 6: Нажимаем на кнопку I want
    submit_button = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    submit_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

        # Шаг 1: Получаем значение переменной x
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    # Шаг 2: Рассчитываем значение функции от x
    y = calc(x)

    # Шаг 3: Вводим ответ в текстовое поле
    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)

    # Шаг 6: Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ждем загрузки страницы
    time.sleep(1)

finally:
    # Ожидание, чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # Закрываем браузер после всех манипуляций
    browser.quit()