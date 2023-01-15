from typing import Optional
from component.component import TransformComponent
from context import Context
from data.data import TransformOutputData, TransformInputData


class AlgorithmOne(TransformComponent):
    def __init__(self, config: dict, context: Context):
        super().__init__(config, context)

    def initialize(self):
        pass

    def execute(self, data: Optional[TransformInputData] = None) -> Optional[TransformOutputData]:
        frame = data.frame
        result = ["AlgorithmOne"]
        # print(1)
        return TransformOutputData(frame=frame, text=result)

    def terminate(self):
        pass
