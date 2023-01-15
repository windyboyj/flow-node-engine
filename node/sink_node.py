from common import ExitNodeException
from component.component import SinkComponent, ComponentFactory
from context import Context
from data.data import BaseData
from node.base_node import BaseNode, NodeObserver


class SinkNode(BaseNode, NodeObserver):

    def __init__(self, node_info: dict, context: Context):
        super().__init__(node_info, context)

        self.component: SinkComponent = ComponentFactory.get_component(node_info, context)
        self.component.initialize()

    def update(self, data: BaseData):
        with self._lock:
            self.pre_data = data
            self.resume()

    def run(self) -> None:
        while self.running:
            try:
                self.suspend()
                self.get_data()
                self.component.execute(self.current_data)
            except ExitNodeException as e:
                self.logger.exception(e)
                self.exit()
            except Exception as e:
                self.logger.exception(e)
        self.release()
