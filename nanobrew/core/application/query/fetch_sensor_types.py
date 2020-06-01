from __future__ import annotations

from ...domain.sensor_type_repository import SensorTypeRepository
from ..base_query import BaseQuery
from ..container import Container
from ..mapper.sensor_type_mapper import SensorTypeMapper


class FetchSensorTypes(BaseQuery):
    def get_handler(self, container):
        return self.Handler(container.get_service('sensor_types'))

    class Handler:
        _sensors: SensorTypeRepository

        def __init__(self, sensor_types: SensorTypeRepository):
            self._sensor_types = sensor_types

        async def handle(self, query: FetchSensorTypes):
            sensor_types = await self._sensor_types.fetch_all()
            mapper = SensorTypeMapper()

            return {key: mapper.sensor_type_to_dict(sensor_type) for key, sensor_type in sensor_types.items()}
