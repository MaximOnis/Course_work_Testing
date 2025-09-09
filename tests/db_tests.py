import pytest
from unittest.mock import MagicMock, patch
import Devices
import Sensors
import DButil


@pytest.fixture
def mock_mongo():
    with patch("DButil.pymongo.MongoClient") as mock_client:
        mock_db = MagicMock()
        mock_client.return_value = mock_db
        yield mock_db


@pytest.fixture
def mock_devices(mock_mongo):
    mock_collection = mock_mongo["Ventilation"]["Devices"]
    mock_collection.find.return_value = [
        {'_id': 1, 'name': 'Device1', 'type': 'Conditioner'},
        {'_id': 2, 'name': 'Device2', 'type': 'HeatingSystem'},
        {'_id': 3, 'name': 'Device3', 'type': 'Humidifier'},
        {'_id': 4, 'name': 'Device4', 'type': 'Ventilation'},
        {'_id': 5, 'name': 'Device5', 'type': 'AirDryer'},
    ]
    return mock_collection


@pytest.fixture
def mock_sensors(mock_mongo):
    mock_collection = mock_mongo["Ventilation"]["Sensors"]
    mock_collection.find.return_value = [
        {'_id': 101, 'name': 'Sensor1', 'type': 'Termometer'},
        {'_id': 102, 'name': 'Sensor2', 'type': 'HumiditySensor'},
        {'_id': 103, 'name': 'Sensor3', 'type': 'PollutionSensor'},
    ]
    return mock_collection


def test_initialize_devices(mock_devices):
    DButil.devices = mock_devices
    DButil.conditioner = None
    DButil.heating = None
    DButil.humidifier = None
    DButil.ventilation = None
    DButil.dryer = None

    for a in mock_devices.find():
        match a['type']:
            case 'Conditioner':
                assert a['name'] == 'Device1'
                DButil.conditioner = Devices.Conditioner(a['_id'], a['name'])
            case 'HeatingSystem':
                assert a['name'] == 'Device2'
                DButil.heating = Devices.Heating(a['_id'], a['name'])
            case 'Humidifier':
                assert a['name'] == 'Device3'
                DButil.humidifier = Devices.AirHumidifier(a['_id'], a['name'])
            case 'Ventilation':
                assert a['name'] == 'Device4'
                DButil.ventilation = Devices.Ventilation(a['_id'], a['name'])
            case 'AirDryer':
                assert a['name'] == 'Device5'
                DButil.dryer = Devices.AirDryer(a['_id'], a['name'])

    assert DButil.conditioner is not None
    assert DButil.heating is not None
    assert DButil.humidifier is not None
    assert DButil.ventilation is not None
    assert DButil.dryer is not None


def test_initialize_sensors(mock_sensors):
    DButil.sensors = mock_sensors
    DButil.termometer = None
    DButil.humidity_sensor = None
    DButil.pollution_sensor = None

    for a in mock_sensors.find():
        match a['type']:
            case 'Termometer':
                assert a['name'] == 'Sensor1'
                DButil.termometer = Sensors.Termometer(a['_id'], a['name'])
            case 'HumiditySensor':
                assert a['name'] == 'Sensor2'
                DButil.humidity_sensor = Sensors.HumiditySensor(a['_id'], a['name'])
            case 'PollutionSensor':
                assert a['name'] == 'Sensor3'
                DButil.pollution_sensor = Sensors.PollutionSensor(a['_id'], a['name'])

    assert DButil.termometer is not None
    assert DButil.humidity_sensor is not None
    assert DButil.pollution_sensor is not None


def test_get_devices_and_sensors():
    assert DButil.get_conditioner() is DButil.conditioner
    assert DButil.get_heating() is DButil.heating
    assert DButil.get_humidifier() is DButil.humidifier
    assert DButil.get_ventilation() is DButil.ventilation
    assert DButil.get_air_dryer() is DButil.dryer
    assert DButil.get_termometer() is DButil.termometer
    assert DButil.get_humidity_sensor() is DButil.humidity_sensor
    assert DButil.get_pollution_sensor() is DButil.pollution_sensor
