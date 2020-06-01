class OutputType:
    def __init__(self, name, options, factory: callable):
        self._name = name
        self._options = options
        self._factory = factory

    async def create_output(self, parameters: dict):
        return await self._factory(parameters)

    def to_dict(self):
        return {
            'name': self._name,
            'options': self._options.to_dict(),
        }
