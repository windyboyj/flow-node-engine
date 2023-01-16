import time
import cv2
from typing import Optional
from component.component import SinkComponent
from context import Context
from entity.data import TransformOutputData


class ShowSink(SinkComponent):

    def __init__(self, config: dict, context: Context):
        super().__init__(config, context)
        self.timestamp = str(int(time.time()))

    def initialize(self):
        pass

    def execute(self, data: Optional[TransformOutputData] = None):
        frame = data.frame
        cv2.imshow(self.timestamp, frame)
        cv2.waitKey(1)
        return

    def terminate(self):
        cv2.destroyAllWindows()
