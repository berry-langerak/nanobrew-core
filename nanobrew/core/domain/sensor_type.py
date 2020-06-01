from .options import Options
from .unit import Unit


class SensorType:
    _name: str
    _options: dict
    _factory: callable
    _unit: Unit

    def __init__(self, name: str, options: Options, factory: callable, unit: Unit):
        self._name = name
        self._options = options
        self._factory = factory
        self._unit = unit

    def get_unit(self) -> Unit:
        return self._unit

    def get_options(self) -> Options:
        return self._options

    def get_name(self):
        return self._name

    def to_dict(self):
        return {
            'name': self._name,
            'options': self._options.to_dict(),
            'unit': self._unit.to_dict()
        }

    async def create_reader(self, parameters: dict):
        return await self._factory(parameters)
