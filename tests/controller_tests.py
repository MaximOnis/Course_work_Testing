import pytest
import asyncio
from unittest.mock import MagicMock
import Controller


# Моки для DButil
@pytest.fixture
def mock_dbutil():
    mock_dbutil = MagicMock()
    mock_dbutil.get_ventilation.return_value = MagicMock()
    mock_dbutil.get_humidifier.return_value = MagicMock()
    mock_dbutil.get_air_dryer.return_value = MagicMock()
    mock_dbutil.get_conditioner.return_value = MagicMock()
    mock_dbutil.get_heating.return_value = MagicMock()
    mock_dbutil.get_termometer.return_value = MagicMock()
    mock_dbutil.get_humidity_sensor.return_value = MagicMock()
    mock_dbutil.get_pollution_sensor.return_value = MagicMock()
    return mock_dbutil


# Тест 1: Ініціалізація класу Controller
def test_controller_initialization(mock_dbutil):
    controller = Controller.Controller()

    assert controller.ventilation is not None
    assert controller.humidifier is not None
    assert controller.conditioner is not None
    assert controller.heating_system is not None
    assert controller.termometer is not None
    assert controller.humidity_sensor is not None
    assert controller.pollution_sensor is not None


# Тест 2: Перевірка методу generate_data
def test_generate_data(mock_dbutil):
    controller = Controller.Controller()

    # Створення моків для функцій, які викликаються в generate_data
    controller.termometer.generate = MagicMock()
    controller.pollution_sensor.generate = MagicMock()
    controller.humidity_sensor.generate = MagicMock()

    controller.generate_data()

    # Перевірка, що метод generate був викликаний для кожного сенсора
    controller.termometer.generate.assert_called_once()
    controller.pollution_sensor.generate.assert_called_once()
    controller.humidity_sensor.generate.assert_called_once()


# Тест 3: Перевірка методу get_stats
def test_get_stats(mock_dbutil):
    controller = Controller.Controller()

    # Моки для методів сенсорів
    controller.termometer.get_temperature = MagicMock(return_value=25)
    controller.humidity_sensor.get_humiditylevel = MagicMock(return_value=50)
    controller.pollution_sensor.get_pollutionlevel = MagicMock(return_value=10)

    stats = controller.get_stats()

    assert stats == [25, 50, 10]
