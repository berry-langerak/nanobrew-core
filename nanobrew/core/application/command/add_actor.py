from __future__ import annotations

import logging

from ...domain.actor import Actor
from ...domain.event_listener import EventListener
from ..base_command import BaseCommand
from ..container import Container
from ..error.validation_failed import ValidationFailed


class AddActor(BaseCommand):
    def __init__(self, actor_name, output_type_name, parameters: dict):
        self.actor_name = actor_name
        self.output_type_name = output_type_name
        self.parameters = parameters

    def get_handler(self, container: Container):
        return self.Handler(
            container.get_service('actors'),
            container.get_service('output_types')
        )

    class Handler:
        def __init__(self, actors, output_types):
            self._actors = actors
            self._output_types = output_types

        async def handle(self, command: AddActor):
            output_type = await self._output_types.get_by_type_name(command.output_type_name)

            options = output_type.get_options()

            (success, errors) = options.validate(command.parameters)

            if success != True:
                raise ValidationFailed(errors)

            actor = Actor(None, command.actor_name, output_type, options.filter(command.parameters))

            await actor.persist(self._actors)

            return actor.get_id()
