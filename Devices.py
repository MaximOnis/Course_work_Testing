import Sensors
import asyncio


class Device:
    def __init__(self, devid, name):
        self.id = devid
        self.name = name
        self.status = 0

    def on(self):
        self.status = 0

    def off(self):
        self.status = 1


class Ventilation(Device):
    def __init__(self, devid, name):
        super().__init__(devid, name)
        self.pollution = None

    async def set_pollution(self, sensor, pollution=25):
        self.on()
        self.pollution = pollution
        await sensor.set_pollution(pollution)

    def off(self):
        super().off()
        self.pollution = 0


class Conditioner(Device):
    def __init__(self, devid, name):
        super().__init__(devid, name)
        self.temperature = None

    async def set_temperature(self, termometer, temperature=20):
        self.on()
        self.temperature = temperature
        await termometer.set_temperature(temperature, '-')

    def off(self):
        super().off()
        self.temperature = None


class AirHumidifier(Device):
    def __init__(self, devid, name):
        super().__init__(devid, name)
        self.humidity = None

    async def set_humiditylevel(self, sensor, humidity=40):
        self.on()
        self.humidity = humidity
        await sensor.set_humidity(humidity, '+')

    def off(self):
        super().off()
        self.humidity = 0


class AirDryer(Device):
    def __init__(self, devid, name):
        super().__init__(devid, name)
        self.humidity = None

    async def set_humiditylevel(self, sensor, humidity=40):
        self.on()
        self.humidity = humidity
        await sensor.set_humidity(humidity, '-')

    def off(self):
        super().off()
        self.humidity = 0


class Heating(Device):
    def __init__(self, devid, name):
        super().__init__(devid, name)
        self.temperature = None

    async def set_temperature(self, termometer, temperature=20):
        self.on()
        self.temperature = temperature
        await termometer.set_temperature(temperature, '+')

    def off(self):
        super().off()
        self.temperature = None
