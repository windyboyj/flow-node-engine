from typing import Optional
from component.component import SinkComponent
from context import Context
from entity.data import TransformOutputData


class LogSink(SinkComponent):

    def __init__(self, config: dict, context: Context):
        super().__init__(config, context)

    def initialize(self):
        pass

    def execute(self, data: Optional[TransformOutputData] = None):
        self.logger.info("result %s %s", data.frame_id, data.text)
        return

    def terminate(self):
        pass
