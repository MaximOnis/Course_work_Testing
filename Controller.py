import DButil
import asyncio


class Controller:
    def __init__(self):
        self.pollution = None
        self.humidity = None
        self.temperature = None
        self.ventilation = DButil.get_ventilation()
        self.humidifier = DButil.get_humidifier()
        self.airdryer = DButil.get_air_dryer()
        self.conditioner = DButil.get_conditioner()
        self.heating_system = DButil.get_heating()

        self.termometer = DButil.get_termometer()
        self.humidity_sensor = DButil.get_humidity_sensor()
        self.pollution_sensor = DButil.get_pollution_sensor()

        if not all([self.ventilation, self.humidifier, self.conditioner, self.heating_system]):
            raise ValueError("One or more devices are not initialized correctly.")

    def generate_data(self):
        self.termometer.generate()
        self.pollution_sensor.generate()
        self.humidity_sensor.generate()

    def get_stats(self):
        self.temperature = self.termometer.get_temperature()
        self.humidity = self.humidity_sensor.get_humiditylevel()
        self.pollution = self.pollution_sensor.get_pollutionlevel()
        stats = [self.temperature, self.humidity, self.pollution]
        return stats

    async def set_temperature(self, temperature=20):
        if self.temperature > temperature:
            await self.conditioner.set_temperature(self.termometer, temperature)
        elif self.temperature < temperature:
            await self.heating_system.set_temperature(self.termometer, temperature)

    async def set_humidity(self, humidity=40):
        if self.humidity < humidity:
            await self.humidifier.set_humiditylevel(self.humidity_sensor, humidity)
        elif self.humidity > humidity:
            await self.airdryer.set_humiditylevel(self.humidity_sensor, humidity)

    async def set_pollution(self, pollution=25):
        if self.pollution > pollution:
            await self.ventilation.set_pollution(self.pollution_sensor, pollution)

    async def update_all(self, temperature=20, humidity=40, pollution=25):
        # Виконуємо всі три функції паралельно
        await asyncio.gather(
            self.set_temperature(temperature),
            self.set_humidity(humidity),
            self.set_pollution(pollution)
        )
        # Повертаємо оновлені дані
        stats = self.get_stats()
        return stats
