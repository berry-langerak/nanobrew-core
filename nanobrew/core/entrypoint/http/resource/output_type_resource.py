from aiohttp import web

from ....application import CommandBus, QueryBus
from ....application.query.fetch_output_types import FetchOutputTypes

class OutputTypeResource:
    _commands: CommandBus
    _queries: QueryBus

    def __init__(self, commands: CommandBus, queries: QueryBus):
        self._commands = commands
        self._queries = queries

    async def handle_get(self, request):
        output_types = await self._queries.run_query(FetchOutputTypes())

        return web.json_response(output_types)

    def attach(self, app: web.Application):
        app.add_routes([
            web.get('/output_types', self.handle_get)
        ])

        return app