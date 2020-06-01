import logging

from nanobrew.core.distributed.output import Output

class DummyOutput(Output):
    def __init__(self, dummy_id):
        self._output_on = True
        self._dummy_id = dummy_id

    async def on(self):
        logging.info('DummyOutput.on(%d)' % self._dummy_id)
        self._output_on = True

    async def off(self):
        logging.info('DummyOutput.on(%d)' % self._dummy_id)
        self._output_on = False
