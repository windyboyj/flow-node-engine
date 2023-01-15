from common import ExitNodeException
from component.component import ComponentFactory, SourceComponent
from context import Context
from data.data import TransformInputData
from node.base_node import BaseNode, NodeSubject


class SourceNode(BaseNode, NodeSubject):
    def __init__(self, node_info: dict, context: Context):
        super().__init__(node_info, context)
        NodeSubject.__init__(self)
        try:
            self.frame_id = 1
            self.component: SourceComponent = ComponentFactory.get_component(node_info, context)
            self.component.initialize()
        except Exception as e:
            self.logger.exception(e)
            raise ExitNodeException()

    def run(self):
        while self.running:
            try:
                frame = self.component.execute()
                if frame is not None:
                    data = TransformInputData(frame_id=self.frame_id, frame=frame, param={})
                    self.notify_all(data)
                    self.frame_id += 1
            except ExitNodeException as e:
                self.logger.exception(e)
                self.exit()
            except Exception as e:
                self.logger.exception(e)
        self.release()
