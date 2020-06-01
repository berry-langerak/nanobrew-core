from aiohttp import web

from ....application import CommandBus, QueryBus
from ....application.error.validation_failed import ValidationFailed
# from ....application.query.fetch_actors import FetchActors
from ....application.command.add_actor import AddActor

class ActorResource:
    _commands: CommandBus
    _queries: QueryBus

    def __init__(self, commands: CommandBus, queries: QueryBus):
        self._commands = commands
        self._queries = queries

    # async def handle_get(self, request):
    #     actors = await self._queries.run_query(FetchActors())

    #     return web.json_response(actors)

    async def handle_post(self, request):
        body = await request.json()

        try:
            actor_id = await self._commands.run_command(AddActor(body['name'], body['output_type'], body['parameters']))

            headers = {
                'Location': '/actors/' + actor_id
            }

            return web.json_response(status=201, headers=headers, data={
                'name': body['name'],
                'output_type': body['output_type'],
                'parameters': body['parameters']
            })

        except ValidationFailed as error:
            return web.json_response(status=422, data={
                'reason': error.get_errors()
            })

    # async def handle_put(self, request):
    #     body = await request.json()
    #     actor_id = request.match_info['actor_id']

    #     try:
    #         cmd = EditActor(actor_id, body['name'], body['output_type'], body['parameters'])
    #         await self._commands.run_command(cmd)

    #         return web.json_response(status=200, data={
    #             'name': body['name'],
    #             'output_type': body['output_type'],
    #             'parameters': body['parameters']
    #         })

    #     except ValidationFailed as error:
    #         return web.json_response(status=422, data={
    #             'reason': error.get_errors()
    #         })

    # async def handle_delete(self, request):
    #     actor_id = request.match_info['actor_id']

    #     try:
    #         await self._commands.run_command(DeleteActor(actor_id))
    #         return web.Response(status=204)

    #     except KeyError:
    #         return web.Response(status=404)


    def attach(self, app: web.Application):
        app.add_routes([
            # web.get('/actors', self.handle_get),
            web.post('/actors', self.handle_post),
            # web.put('/actors/{actor_id}', self.handle_put),
            # web.delete('/actors/{actor_id}', self.handle_delete)
        ])

        return app