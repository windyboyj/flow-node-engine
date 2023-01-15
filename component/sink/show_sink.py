from typing import Optional

import cv2

from component.component import SinkComponent
from context import Context
from data.data import TransformOutputData


class ShowSink(SinkComponent):

    def __init__(self, config: dict, context: Context):
        super().__init__(config, context)

    def initialize(self):
        pass

    def execute(self, data: Optional[TransformOutputData] = None):
        frame = data.frame
        cv2.imshow("show", frame)
        cv2.waitKey(1)
        return

    def terminate(self):
        cv2.destroyAllWindows()
