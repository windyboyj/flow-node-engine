from typing import Optional

import cv2

from component.component import TransformComponent
from context import Context
from data.data import TransformOutputData, TransformInputData


class AlgorithmTwo(TransformComponent):
    def __init__(self, config: dict, context: Context):
        super().__init__(config, context)

    def initialize(self):
        pass

    def execute(self, data: Optional[TransformInputData] = None) -> Optional[TransformOutputData]:
        frame = data.frame
        result = ["AlgorithmTwo"]
        text = "AlgorithmTwo: frame_id:" + str(data.frame_id)
        cv2.putText(frame, text, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        return TransformOutputData(frame=frame, text=result)

    def terminate(self):
        pass
