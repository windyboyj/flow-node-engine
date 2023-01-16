import copy
from common import ExitNodeException
from component.component import ComponentFactory, TransformComponent
from context import Context
from entity.data import BaseData, TransformOutputData
from node.base_node import NodeSubject, BaseNode, NodeObserver


class TransformNode(BaseNode, NodeSubject, NodeObserver):

    def __init__(self, node_info: dict, context: Context):
        super().__init__(node_info, context)
        NodeSubject.__init__(self)
        NodeObserver.__init__(self)
        try:
            self.component: TransformComponent = ComponentFactory.get_component(node_info, context)
            self.component.initialize()
        except Exception as e:
            self.logger.exception(e)
            raise ExitNodeException()

    def update(self, data: BaseData):
        with self.lock:
            self.pre_data = copy.deepcopy(data)
            self.resume()

    def run(self) -> None:
        self.suspend()
        while self.running:
            try:
                self.get_data()
                result_data: TransformOutputData = self.component.execute(self.current_data)
                result_data.frame_id = self.current_data.frame_id
                self.notify_all(result_data)
                self.suspend()
            except ExitNodeException as e:
                self.logger.exception(e)
                self.exit()
            except Exception as e:
                self.logger.exception(e)
        self.release()
