import copy

from common import ExitNodeException
from component.component import SinkComponent, ComponentFactory
from context import Context
from entity.data import BaseData
from node.base_node import BaseNode, NodeObserver


class SinkNode(BaseNode, NodeObserver):

    def __init__(self, node_info: dict, context: Context):
        super().__init__(node_info, context)

        self.component: SinkComponent = ComponentFactory.get_component(node_info, context)
        self.component.initialize()

    def update(self, data: BaseData):
        with self.lock:
            self.pre_data = copy.deepcopy(data)
            self.resume()

    def run(self) -> None:
        self.suspend()
        while self.running:
            try:
                self.get_data()
                self.component.execute(self.current_data)
                self.suspend()
            except ExitNodeException as e:
                self.logger.exception(e)
                self.exit()
            except Exception as e:
                self.logger.exception(e)
        self.release()
