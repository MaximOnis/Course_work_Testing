import random
import asyncio


class Sensor:
    def __init__(self, devid, name):
        self.id = devid
        self.name = name
        self.status = 0

    def on(self):
        self.status = 0

    def off(self):
        self.status = 1


class PollutionSensor(Sensor):
    def __init__(self, devid, name):
        super().__init__(devid, name)
        self.pollution = 0
        self.generate()

    def generate(self):
        self.pollution = random.randrange(20, 200)

    def get_pollutionlevel(self):
        self.on()
        return self.pollution

    async def set_pollution(self, pollution):
        if self.pollution > pollution:
            while self.pollution > pollution:
                self.pollution -= 5
                await asyncio.sleep(1)

    def off(self):
        super().off()


class HumiditySensor(Sensor):
    def __init__(self, devid, name):
        super().__init__(devid, name)
        self.humidity = 0
        self.generate()

    def generate(self):
        self.humidity = random.randrange(15, 20)

    def get_humiditylevel(self):
        self.on()
        return self.humidity

    async def set_humidity(self, humidity, sign):
        if sign == '+':
            while self.humidity < humidity:
                self.humidity += 1
                await asyncio.sleep(1)
        elif sign == '-':
            while self.humidity > humidity:
                self.humidity -= 1
                await asyncio.sleep(1)

    def off(self):
        super().off()


class Termometer(Sensor):
    def __init__(self, devid, name):
        super().__init__(devid, name)
        self.temperature = 0
        self.generate()

    def generate(self):
        self.temperature = random.randrange(5, 50)

    def get_temperature(self,):
        self.on()
        return self.temperature

    async def set_temperature(self, temperature, sign):
        if sign == '-':
            while self.temperature > temperature:
                self.temperature -= 1
                await asyncio.sleep(1)
        elif sign == '+':
            while self.temperature < temperature:
                self.temperature += 1
                await asyncio.sleep(1)

    def off(self):
        super().off()
