
from __future__ import annotations
import logging

from ..base_command import BaseCommand
from ..container import Container
from ...domain.sensor_repository import SensorRepository

class ActivateSensors(BaseCommand):
    def __init__(self):
        pass

    def get_handler(self, container: Container):
        return self.Handler(container.get_service('sensors'))

    class Handler:
        _sensors: SensorRepository
        
        def __init__(self, sensors: SensorRepository):
            self._sensors = sensors

        async def handle(self, command: ActivateSensors):
            sensor_list = await self._sensors.fetch_all()
            for sensor in sensor_list.values():
                await sensor.activate()