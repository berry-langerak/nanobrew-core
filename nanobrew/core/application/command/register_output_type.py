from __future__ import annotations

from ...domain.options import Options as DomainOptions
from ...domain.output_type import OutputType
from ...domain.output_type_repository import OutputTypeRepository
from ..container import Container


class RegisterOutputType:
    def __init__(self, name, options, output_factory: callable):
        self.name = name
        self.options = options
        self.output_factory = output_factory

    def get_handler(self, container: Container):
        output_types = container.get_service('output_types')

        return self.Handler(output_types)

    class Handler:
        _output_types: OutputTypeRepository

        def __init__(self, output_types: OutputTypeRepository):
            self._output_types = output_types

        async def handle(self, command: RegisterOutputType):
            options = DomainOptions.from_dict(command.options.to_dict())
            output_type = OutputType(command.name, options, command.output_factory)

            await self._output_types.register_output_type(command.name, output_type)
