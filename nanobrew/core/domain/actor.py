class Actor:
    _actor_id: str
    _actor_name: str
    _parameters: dict

    def __init__(self, actor_id, actor_name, output_type, parameters: dict):
        self._actor_id = actor_id
        self._actor_name = actor_name
        self._output_type = output_type
        self._parameters = parameters

    async def turn_on(self):
        await self._output_type.on()

    async def turn_off(self):
        await self._output_type.off()
