class Output:
    async def on(self):
        raise NotImplementedError

    async def off(self):
        raise NotImplementedError