import asyncio
import logging

import aiohttp
import aiohttp_cors
from aiohttp import web
from aiohttp.web import AppRunner, TCPSite

from ...application.command_bus import CommandBus
from ...application.config import Config
from ...application.event_bus import EventBus
from ...application.query_bus import QueryBus
from .resource.actor_resource import ActorResource
from .resource.sensor_resource import SensorResource
from .resource.sensor_type_resource import SensorTypeResource
from .resource.output_type_resource import OutputTypeResource
from .resource.websocket_resource import WebsocketResource


class Server:
    _web_app: web.Application

    _config: Config
    _commands: CommandBus
    _events: EventBus
    _queries: QueryBus

    def __init__(self, config: Config, commands: CommandBus, events: EventBus, queries: QueryBus):
        self._commands = commands
        self._events = events
        self._queries = queries
        self._config = config

        self._web_app = self._configure(
            web.Application(),
            commands,
            queries,
            events
        )

        self._web_app.add_routes([
            web.get('/', self.handle),
        ])

    async def handle(self, request):
        text = "Hello world from Nanobrew."
        return web.Response(text=text)

    async def run(self):
        runner = AppRunner(self._web_app)
        await runner.setup()

        host = self._config.get('http.host')
        port = self._config.get('http.port')

        site = TCPSite(runner, host, port)
        logging.info("Running nanobrew on %s:%d" % (host, port))
        await site.start()

    def _configure(self, app: web.Application, commands, queries, events):
        resources = [
            ActorResource(commands, queries),
            SensorResource(commands, queries),
            SensorTypeResource(commands, queries),
            OutputTypeResource(commands, queries),
            WebsocketResource(commands, queries, events)
        ]

        for resource in resources:
            resource.attach(app)

        return self._configure_cors(app)

    def _configure_cors(self, app: web.Application):
        cors = aiohttp_cors.setup(app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
        })

        for route in list(app.router.routes()):
            cors.add(route)

        return app
