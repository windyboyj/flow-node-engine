from typing import Optional

import cv2
import numpy as np

from common import ExitNodeException
from component.component import SourceComponent
from context import Context
from data.data import BaseData, TransformInputData


class VideoSource(SourceComponent):

    def __init__(self, config: dict, context: Context):
        super().__init__(config, context)
        url = self.config.get("videoUrl")
        self.cap = cv2.VideoCapture(url)

    def initialize(self):
        pass

    def execute(self, data: Optional[BaseData] = None) -> Optional[np.ndarray]:
        ret, frame = self.cap.read()
        if not ret:
            raise ExitNodeException()

        return frame

    def terminate(self):
        if self.cap:
            self.cap.release()
