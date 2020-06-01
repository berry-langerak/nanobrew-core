from .sensor_data_mapper import SensorDataMapper


class SensorRepository:
    '''This class is a caching decorator over a concrete data mapper'''
    _sensors: dict = {}
    _repository: SensorDataMapper

    def __init__(self, data_mapper: SensorDataMapper):
        self._data_mapper = data_mapper

    async def fetch_all(self):
        if len(self._sensors) == 0:
            self._sensors = await self._data_mapper.fetch_all()

        return self._sensors

    async def fetch_by_id(self, sensor_id):
        await self.fetch_all()
        if sensor_id not in self._sensors:
            raise KeyError('Sensor with id %s does not exist' % sensor_id)

        return self._sensors[sensor_id]

    async def persist(self, sensor):
        await self._data_mapper.persist(sensor)

        self._sensors[sensor.get_id()] = sensor

    async def delete(self, sensor):
        await self._data_mapper.delete(sensor)

        del self._sensors[sensor.get_id()]