from .actor_data_mapper import ActorDataMapper


class ActorRepository:
    _actors: dict = {}
    _repository: ActorDataMapper

    def __init__(self, data_mapper: ActorDataMapper):
        self._data_mapper = data_mapper

    async def fetch_all(self):
        if len(self._actors) == 0:
            self._sensors = await self._data_mapper.fetch_all()

        return self._sensors

    async def fetch_by_id(self, actor_id):
        await self.fetch_all()
        if actor_id not in self._actors:
            raise KeyError('Actor with id %s does not exist' % actor_id)

        return self._sensors[actor_id]

    async def persist(self, actor):
        await self._data_mapper.persist(actor)

        self._actors[actor.get_id()] = actor

    async def delete(self, actor):
        await self._data_mapper.delete(actor)

        del self._actors[actor.get_id()]
