import uuid

class Actor:
    _actor_id: str
    _actor_name: str
    _parameters: dict
    _state_on: bool = False

    def __init__(self, actor_id, actor_name, output_type, parameters: dict):
        self._actor_id = actor_id
        self._actor_name = actor_name
        self._output_type = output_type
        self._parameters = parameters

    def get_name(self):
        return self._actor_name

    def get_parameters(self):
        return self._parameters

    def get_type_name(self):
        return self._output_type.get_type_name()

    async def is_on(self) -> bool:
        return self._state_on

    async def on(self):
        await self._output_type.on()
        self._state_on = True

    async def off(self):
        await self._output_type.off()
        self._state_on = False

    async def persist(self, repository):
        if self._actor_id is None:
            self._actor_id = str(uuid.uuid4())

        return await repository.persist(self)

    def get_id(self) -> str:
        return self._actor_id
