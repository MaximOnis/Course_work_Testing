import pymongo
import Devices
import Sensors

myclient = pymongo.MongoClient("mongodb+srv://maxonis13:maximonis13@mycluster.1bdhv.mongodb.net/")
mydb = myclient["Ventilation"]
devices = mydb["Devices"]
sensors = mydb["Sensors"]

a = devices.find()
b = sensors.find()

conditioner = None
heating = None
humidifier = None
dryer = None
ventilation = None
termometer = None
humidity_sensor = None
pollution_sensor = None

for a in devices.find():
    match a['type']:
        case 'Conditioner':
            conditioner = Devices.Conditioner(a['_id'], a['name'])
        case 'HeatingSystem':
            heating = Devices.Heating(a['_id'], a['name'])
        case 'Humidifier':
            humidifier = Devices.AirHumidifier(a['_id'], a['name'])
        case 'Ventilation':
            ventilation = Devices.Ventilation(a['_id'], a['name'])
        case 'AirDryer':
            dryer = Devices.AirDryer(a['_id'], a['name'])

for a in sensors.find():
    match a['type']:
        case 'Termometer':
            termometer = Sensors.Termometer(a['_id'], a['name'])
        case 'HumiditySensor':
            humidity_sensor = Sensors.HumiditySensor(a['_id'], a['name'])
        case 'PollutionSensor':
            pollution_sensor = Sensors.PollutionSensor(a['_id'], a['name'])


def get_air_dryer():
    return dryer


def get_termometer():
    return termometer


def get_humidity_sensor():
    return humidity_sensor


def get_pollution_sensor():
    return pollution_sensor


def get_conditioner():
    return conditioner


def get_heating():
    return heating


def get_humidifier():
    return humidifier


def get_ventilation():
    return ventilation

def shut():
    myclient.close()
