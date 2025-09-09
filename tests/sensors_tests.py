import pytest
import asyncio
from unittest.mock import MagicMock
from random import randint

from Sensors import PollutionSensor, HumiditySensor, Termometer  # замініть на правильний шлях


@pytest.mark.asyncio
async def test_pollution_sensor_generate():
    sensor = PollutionSensor(devid=1, name="Pollution Sensor")

    # Перевірка, чи було правильно згенеровано значення забруднення
    assert 20 <= sensor.pollution <= 200


@pytest.mark.asyncio
async def test_pollution_sensor_get_pollutionlevel():
    sensor = PollutionSensor(devid=1, name="Pollution Sensor")

    # Виклик методу get_pollutionlevel
    pollution_level = sensor.get_pollutionlevel()

    # Перевірка, що значення забруднення було правильно повернуто
    assert pollution_level == sensor.pollution


@pytest.mark.asyncio
async def test_set_pollution():
    sensor = PollutionSensor(devid=1, name="Pollution Sensor")

    initial_pollution = sensor.pollution
    target_pollution = initial_pollution - 10  # Зниження рівня забруднення

    # Виклик асинхронного методу для зниження рівня забруднення
    await sensor.set_pollution(target_pollution)

    # Перевірка, що рівень забруднення зменшився
    assert sensor.pollution <= target_pollution


@pytest.mark.asyncio
async def test_humidity_sensor_generate():
    sensor = HumiditySensor(devid=1, name="Humidity Sensor")

    # Перевірка, чи було правильно згенеровано значення вологості
    assert 15 <= sensor.humidity <= 80


@pytest.mark.asyncio
async def test_humidity_sensor_get_humiditylevel():
    sensor = HumiditySensor(devid=1, name="Humidity Sensor")

    # Виклик методу get_humiditylevel
    humidity_level = sensor.get_humiditylevel()

    # Перевірка, що значення вологості було правильно повернуто
    assert humidity_level == sensor.humidity


@pytest.mark.asyncio
async def test_set_humidity():
    sensor = HumiditySensor(devid=1, name="Humidity Sensor")

    initial_humidity = sensor.humidity
    target_humidity = initial_humidity + 10  # Збільшення вологості

    # Виклик асинхронного методу для збільшення рівня вологості
    await sensor.set_humidity(target_humidity, '+')

    # Перевірка, що рівень вологості збільшився
    assert sensor.humidity >= target_humidity


@pytest.mark.asyncio
async def test_set_humidity_decrease():
    sensor = HumiditySensor(devid=1, name="Humidity Sensor")

    initial_humidity = sensor.humidity
    target_humidity = initial_humidity - 10  # Зменшення вологості

    # Виклик асинхронного методу для зменшення рівня вологості
    await sensor.set_humidity(target_humidity, '-')

    # Перевірка, що рівень вологості зменшився
    assert sensor.humidity <= target_humidity


@pytest.mark.asyncio
async def test_termometer_generate():
    sensor = Termometer(devid=1, name="Termometer")

    # Перевірка, чи було правильно згенеровано значення температури
    assert 5 <= sensor.temperature <= 50


@pytest.mark.asyncio
async def test_termometer_get_temperature():
    sensor = Termometer(devid=1, name="Termometer")

    # Виклик методу get_temperature
    temperature = sensor.get_temperature()

    # Перевірка, що значення температури було правильно повернуто
    assert temperature == sensor.temperature


@pytest.mark.asyncio
async def test_set_temperature():
    sensor = Termometer(devid=1, name="Termometer")

    initial_temperature = sensor.temperature
    target_temperature = initial_temperature + 5  # Підвищення температури

    # Виклик асинхронного методу для підвищення температури
    await sensor.set_temperature(target_temperature, '+')

    # Перевірка, що температура збільшилась
    assert sensor.temperature >= target_temperature


@pytest.mark.asyncio
async def test_set_temperature_decrease():
    sensor = Termometer(devid=1, name="Termometer")

    initial_temperature = sensor.temperature
    target_temperature = initial_temperature - 5  # Зниження температури

    # Виклик асинхронного методу для зниження температури
    await sensor.set_temperature(target_temperature, '-')

    # Перевірка, що температура зменшилась
    assert sensor.temperature <= target_temperature


@pytest.mark.asyncio
async def test_turn_on_and_off_sensor():
    sensor = Termometer(devid=1, name="Termometer")

    # Перевірка стану при включенні
    sensor.on()
    assert sensor.status == 0

    # Перевірка стану при вимиканні
    sensor.off()
    assert sensor.status == 1
