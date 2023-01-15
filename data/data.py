from dataclasses import dataclass
from typing import Union

import numpy as np


@dataclass
class BaseData:
    frame_id: int = None


@dataclass
class TransformInputData(BaseData):
    frame: np.ndarray = None
    param: dict = None


@dataclass
class TransformOutputData(BaseData):
    frame: np.ndarray = None
    text: Union[dict, list] = None
    msg: dict = None
