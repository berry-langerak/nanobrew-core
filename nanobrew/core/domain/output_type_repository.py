from .output_type import OutputType

class OutputTypeRepository:
    _output_types: dict

    def __init__(self):
        self._output_types = {}

    async def register_output_type(self, type_name: str, output_type: OutputType):
        self._output_types[type_name] = output_type

    async def fetch_all(self):
        return self._output_types

    async def create(self, type_name: str, parameters: dict):
        if type_name not in self._output_types:
            raise KeyError('Undefined output type "%s"' % type_name)

        return self._output_types[type_name].create_output(parameters)

    async def get_by_type_name(self, type_name) -> OutputType:
        if type_name not in self._output_types:
            raise KeyError('Undefined output type "%s"' % type_name)

        return self._output_types[type_name]
