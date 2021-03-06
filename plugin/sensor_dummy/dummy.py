import asyncio

from nanobrew.domain.sensor_type import SensorType
from nanobrew.domain.parameter import Parameter
from nanobrew.domain.option import Option
from nanobrew.domain.option_list import OptionList
from nanobrew.domain.parameter_list import ParameterList

class DummySensorType(SensorType):
    last: float = 0
    step: float = 0.25

    async def read(self, parameters: ParameterList):
        self.last = self.last + self.step
        return self.last

    async def options(self) -> OptionList:
        return OptionList()
