from ...domain.actor import Actor
from ...domain.actor_data_mapper import ActorDataMapper
from ...domain.output_type_repository import OutputTypeRepository
from .connection import Connection


class SqliteActorDataMapper(ActorDataMapper):
    _output_types: OutputTypeRepository
    _connection: Connection

    def __init__(self, connection: Connection, output_types: OutputTypeRepository):
        self._output_types = output_types
        self._connection = connection

    async def fetch_all(self):
        connection = await self._connection.get_connection()
        cursor = await connection.execute_fetchall(
            "SELECT actor_id, output_type, name FROM actor"
        )

        actors = {}
        for row in cursor:
            output_type = await self._output_types.get_by_type_name(row['output_type'])

            actors[row['actor_id']] = Actor(
                row['actor_id'],
                row['name'],
                output_type,
                await self._get_parameters(row['actor_id'])
            )

        return actors

    async def persist(self, actor: Actor):
        connection = await self._connection.get_connection()

        await connection.execute(
            'REPLACE INTO actor (actor_id, output_type, name) VALUES (?, ?, ?)',
            (actor.get_id(), actor.get_type_name(), actor.get_name())
        )

        await self._persist_parameters( actor.get_id(), actor.get_parameters())

        await connection.commit()

    async def delete(self, actor: Actor):
        connection = await self._connection.get_connection()

        await connection.execute('DELETE FROM actor_parameter WHERE actor_id = ?', (actor.get_id(),))
        await connection.execute('DELETE FROM actor WHERE actor_id = ?', (actor.get_id(),))

        await connection.commit()

    async def _persist_parameters(self, actor_id, parameters):
        connection = await self._connection.get_connection()

        await connection.execute('DELETE FROM actor_parameter WHERE actor_id = ?', (actor_id,))

        for (name, value) in parameters.items():
            await connection.execute(
                'INSERT INTO actor_parameter (actor_id, name, value) VALUES (?, ?, ?)',
                (actor_id, name, value)
            )

    async def _get_parameters(self, actor_id: str) -> dict:
        connection = await self._connection.get_connection()
        cursor = await connection.execute_fetchall(
            "SELECT name, value FROM actor_parameter WHERE actor_id = ?",
            [actor_id]
        )

        parameters = {}
        for row in cursor:
            parameters[row['name']] = row['value']

        return parameters
