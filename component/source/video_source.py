import cv2
import numpy as np
from typing import Optional
from common import ExitNodeException
from component.component import SourceComponent
from context import Context
from entity.data import BaseData


class VideoSource(SourceComponent):

    def __init__(self, config: dict, context: Context):
        super().__init__(config, context)
        self.url = self.config.get("videoUrl")
        self.cap = cv2.VideoCapture(self.url)

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
