import pytest
import asyncio
from unittest.mock import AsyncMock
from Devices import Ventilation, Conditioner, AirHumidifier, AirDryer, Heating, Device  # замініть на правильний шлях
from Sensors import PollutionSensor, Termometer, HumiditySensor  # також замінити на правильний шлях


@pytest.mark.asyncio
async def test_ventilation_set_pollution():
    ventilation = Ventilation(devid=1, name="Ventilation")
    pollution_sensor = AsyncMock(spec=PollutionSensor)  # Використовуємо AsyncMock

    # Викликаємо асинхронний метод set_pollution
    await ventilation.set_pollution(pollution_sensor, pollution=30)

    # Перевірка, чи був викликаний метод set_pollution в сенсорі
    pollution_sensor.set_pollution.assert_called_once_with(30)

    # Перевірка, чи змінилося значення pollution в вентиляції
    assert ventilation.pollution == 30


@pytest.mark.asyncio
async def test_conditioner_set_temperature():
    conditioner = Conditioner(devid=1, name="Conditioner")
    termometer = AsyncMock(spec=Termometer)  # Використовуємо AsyncMock

    # Викликаємо асинхронний метод set_temperature
    await conditioner.set_temperature(termometer, temperature=22)

    # Перевірка, чи був викликаний метод set_temperature в термометрі
    termometer.set_temperature.assert_called_once_with(22, '-')

    # Перевірка, чи змінилося значення temperature в кондиціонері
    assert conditioner.temperature == 22


@pytest.mark.asyncio
async def test_air_humidifier_set_humiditylevel():
    humidifier = AirHumidifier(devid=1, name="Air Humidifier")
    humidity_sensor = AsyncMock(spec=HumiditySensor)  # Використовуємо AsyncMock

    # Викликаємо асинхронний метод set_humiditylevel
    await humidifier.set_humiditylevel(humidity_sensor, humidity=50)

    # Перевірка, чи був викликаний метод set_humidity в сенсорі
    humidity_sensor.set_humidity.assert_called_once_with(50, '+')

    # Перевірка, чи змінилося значення humidity в зволожувачі
    assert humidifier.humidity == 50


@pytest.mark.asyncio
async def test_air_dryer_set_humiditylevel():
    air_dryer = AirDryer(devid=1, name="Air Dryer")
    humidity_sensor = AsyncMock(spec=HumiditySensor)  # Використовуємо AsyncMock

    # Викликаємо асинхронний метод set_humiditylevel
    await air_dryer.set_humiditylevel(humidity_sensor, humidity=30)

    # Перевірка, чи був викликаний метод set_humidity в сенсорі
    humidity_sensor.set_humidity.assert_called_once_with(30, '-')

    # Перевірка, чи змінилося значення humidity в осушувачі
    assert air_dryer.humidity == 30


@pytest.mark.asyncio
async def test_heating_set_temperature():
    heating = Heating(devid=1, name="Heating")
    termometer = AsyncMock(spec=Termometer)  # Використовуємо AsyncMock

    # Викликаємо асинхронний метод set_temperature
    await heating.set_temperature(termometer, temperature=25)

    # Перевірка, чи був викликаний метод set_temperature в термометрі
    termometer.set_temperature.assert_called_once_with(25, '+')

    # Перевірка, чи змінилося значення temperature в опаленні
    assert heating.temperature == 25


@pytest.mark.asyncio
async def test_device_on_off():
    device = Device(devid=1, name="Device")

    # Перевірка, чи правильний статус при включенні
    device.on()
    assert device.status == 0

    # Перевірка, чи правильний статус при вимкненні
    device.off()
    assert device.status == 1


@pytest.mark.asyncio
async def test_ventilation_off():
    ventilation = Ventilation(devid=1, name="Ventilation")

    # Включення вентиляції
    await ventilation.set_pollution(AsyncMock(), pollution=50)

    # Перевірка, що вентиляція включена
    assert ventilation.status == 0

    # Виклик методу off
    ventilation.off()

    # Перевірка, чи статус вентиляції змінився на вимкнений
    assert ventilation.status == 1
    assert ventilation.pollution == 0


@pytest.mark.asyncio
async def test_conditioner_off():
    conditioner = Conditioner(devid=1, name="Conditioner")

    # Включення кондиціонера
    await conditioner.set_temperature(AsyncMock(), temperature=20)

    # Перевірка, що кондиціонер включений
    assert conditioner.status == 0

    # Виклик методу off
    conditioner.off()

    # Перевірка, чи статус кондиціонера змінився на вимкнений
    assert conditioner.status == 1
    assert conditioner.temperature is None


@pytest.mark.asyncio
async def test_air_humidifier_off():
    humidifier = AirHumidifier(devid=1, name="Air Humidifier")

    # Включення зволожувача
    await humidifier.set_humiditylevel(AsyncMock(), humidity=50)

    # Перевірка, що зволожувач включений
    assert humidifier.status == 0

    # Виклик методу off
    humidifier.off()

    # Перевірка, чи статус зволожувача змінився на вимкнений
    assert humidifier.status == 1
    assert humidifier.humidity == 0


@pytest.mark.asyncio
async def test_air_dryer_off():
    air_dryer = AirDryer(devid=1, name="Air Dryer")

    # Включення осушувача
    await air_dryer.set_humiditylevel(AsyncMock(), humidity=30)

    # Перевірка, що осушувач включений
    assert air_dryer.status == 0

    # Виклик методу off
    air_dryer.off()

    # Перевірка, чи статус осушувача змінився на вимкнений
    assert air_dryer.status == 1
    assert air_dryer.humidity == 0


@pytest.mark.asyncio
async def test_heating_off():
    heating = Heating(devid=1, name="Heating")

    # Включення обігрівача
    await heating.set_temperature(AsyncMock(), temperature=22)

    # Перевірка, що обігрівач включений
    assert heating.status == 0

    # Виклик методу off
    heating.off()

    # Перевірка, чи статус обігрівача змінився на вимкнений
    assert heating.status == 1
    assert heating.temperature is None

