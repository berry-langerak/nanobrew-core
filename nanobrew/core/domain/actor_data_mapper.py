class ActorDataMapper:
    async def fetch_all(self):
        raise NotImplementedError

    async def persist(self, actor):
        raise NotImplementedError

    async def delete(self, actor):
        raise NotImplementedError
