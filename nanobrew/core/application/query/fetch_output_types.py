from __future__ import annotations

from ...domain.output_type_repository import OutputTypeRepository
from ..base_query import BaseQuery
from ..container import Container
from ..mapper.output_type_mapper import OutputTypeMapper


class FetchOutputTypes(BaseQuery):
    def get_handler(self, container):
        return self.Handler(container.get_service('output_types'))

    class Handler:
        _outputs_types: OutputTypeRepository

        def __init__(self, output_types: OutputTypeRepository):
            self._output_types = output_types

        async def handle(self, query: FetchOutputTypes):
            output_types = await self._output_types.fetch_all()
            mapper = OutputTypeMapper()

            return {key: mapper.output_type_to_dict(output_type) for key, output_type in output_types.items()}
