from nanobrew.core.application.command import RegisterOutputType
from nanobrew.core.distributed.options import Options

from .dummy_output import DummyOutput

async def create_output(parameters) -> DummyOutput:
    return DummyOutput(parameters['dummy_id'])

async def activate(commands=None, **kwargs):
    options = Options()
    options.add_numeric_option(True, 'dummy_id', 'Dummy ID', 'An ID for the dummy output')

    await commands.run_command(
        RegisterOutputType("dummy", options, create_output)
    )
