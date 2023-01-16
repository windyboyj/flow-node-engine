import abc
import numpy as np
from typing import Optional, Union
from context import Context
from entity.data import BaseData, TransformOutputData


class ComponentFactory(object):
    @staticmethod
    def get_component(node_info, context):
        try:
            import component
            component_type = node_info.get("type")
            component_config = node_info.get("config")
            component_cls = getattr(component, component_type)
            component_ins = component_cls(component_config, context)
            return component_ins
        except Exception as e:
            print(e)
            return None


class BaseComponent(abc.ABC):
    def __init__(self, config: dict, context: Context):
        self._config = config
        self._context = context
        self._logger = context.logger

    @abc.abstractmethod
    def initialize(self):
        pass

    @abc.abstractmethod
    def execute(self, data: Optional[BaseData] = None) -> Union[BaseData, TransformOutputData, np.ndarray, None]:
        pass

    @abc.abstractmethod
    def terminate(self):
        pass

    @property
    def logger(self):
        return self._logger

    @property
    def config(self):
        return self._config

    @property
    def context(self):
        return self._context


class SourceComponent(BaseComponent, abc.ABC):
    @abc.abstractmethod
    def execute(self, data: Optional[BaseData] = None) -> Optional[np.ndarray]:
        pass


class TransformComponent(BaseComponent, abc.ABC):
    @abc.abstractmethod
    def execute(self, data: Optional[BaseData] = None) -> Optional[TransformOutputData]:
        pass


class SinkComponent(BaseComponent, abc.ABC):
    @abc.abstractmethod
    def execute(self, data: Optional[BaseData] = None):
        pass
