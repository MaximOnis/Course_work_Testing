import time
import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# Фікстура для створення драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService())
    yield driver
    driver.quit()


# Тест для перевірки завантаження сторінки
def test_page_load(driver):
    driver.get("http://127.0.0.1:5000")  # Замініть на URL вашого додатку
    assert "Система контролю вентиляцією" in driver.title
    header = driver.find_element(By.TAG_NAME, "h1")
    assert header.text == "Система контролю вентиляцією"


# Тест для перевірки генерації даних
def test_info_data(driver):
    driver.get("http://127.0.0.1:5000")

    # Очікуємо оновлення сенсорних даних
    temperature_value = driver.find_element(By.ID, "temperature-value").text
    assert "°C" in temperature_value

    pollution_value = driver.find_element(By.ID, "pollution-value").text
    assert "µg/m³" in pollution_value

    humidity_value = driver.find_element(By.ID, "humidity-value").text
    assert "%" in humidity_value


def test_get_data(driver):
    driver.get("http://127.0.0.1:5000")
    button = driver.find_element(By.XPATH, "//button[contains(text(),'Ввімкнути')]")
    button.click()

    # Очікуємо оновлення сенсорних даних
    wait = WebDriverWait(driver, 1)

    # Перевірка для температури
    temperature_value = wait.until(
        ec.presence_of_element_located((By.CSS_SELECTOR, "#temperature-value .number"))
    ).text
    assert re.match(r"^-?\d+(\.\d+)?$", temperature_value), f"Temperature value is not a number: {temperature_value}"

    # Перевірка для забруднення
    pollution_value = driver.find_element(By.CSS_SELECTOR, "#pollution-value .number").text
    assert re.match(r"^-?\d+(\.\d+)?$", pollution_value), f"Pollution value is not a number: {pollution_value}"

    # Перевірка для вологості
    humidity_value = driver.find_element(By.CSS_SELECTOR, "#humidity-value .number").text
    assert re.match(r"^-?\d+(\.\d+)?$", humidity_value), f"Humidity value is not a number: {humidity_value}"


# Тест для автоматичного оновлення
def test_auto_update(driver):
    driver.get("http://127.0.0.1:5000")

    # Отримуємо початкові значення
    initial_temperature_value = driver.find_element(By.CSS_SELECTOR, "#temperature-value .number").text
    initial_pollution_value = driver.find_element(By.CSS_SELECTOR, "#pollution-value .number").text
    initial_humidity_value = driver.find_element(By.CSS_SELECTOR, "#humidity-value .number").text

    # Чекаємо автоматичного оновлення
    time.sleep(3)

    # Отримуємо нові значення
    updated_temperature_value = driver.find_element(By.CSS_SELECTOR, "#temperature-value .number").text
    updated_pollution_value = driver.find_element(By.CSS_SELECTOR, "#pollution-value .number").text
    updated_humidity_value = driver.find_element(By.CSS_SELECTOR, "#humidity-value .number").text

    # Перевіряємо, чи значення змінилися
    assert initial_temperature_value != updated_temperature_value or initial_pollution_value != updated_pollution_value or initial_humidity_value != updated_humidity_value
