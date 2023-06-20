# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем текстовые поля
    input_first_name = browser.find_element(By.NAME, "firstname")
    input_first_name.send_keys("John")

    input_last_name = browser.find_element(By.NAME, "lastname")
    input_last_name.send_keys("Doe")

    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("john.doe@example.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ждем загрузки страницы
    time.sleep(1)

finally:
    # Ожидание, чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # Закрываем браузер после всех манипуляций
    browser.quit()