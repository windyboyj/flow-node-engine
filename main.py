import json
import threading
import time
from typing import Optional, List

from context import Context
from node.sink_node import SinkNode
from node.source_node import SourceNode
from node.transform_node import TransformNode


class TaskRunner(object):
    def __init__(self, task_info: dict):
        self.running = True
        self.event = threading.Event()
        self.task_info = task_info
        print(self.task_info)
        self.context = Context(task_info)
        self.source_node: Optional[SourceNode] = None
        self.transform_nodes: Optional[List[TransformNode]] = []
        self.transform_nodes_map: dict = {}
        self.sink_nodes = []

    def start(self):
        try:
            self.init_nodes()
            print(self.source_node, self.transform_nodes, self.sink_nodes)
            self.start_nodes()
            while self.running:
                if self.source_node.is_alive() is False:
                    break
                self.event.wait(timeout=2)

        except Exception as e:
            print(e)
        self.exit_nodes()

    def exit_nodes(self):
        self.source_node.exit()

    def start_nodes(self):
        self.source_node.setDaemon(True)
        self.source_node.start()
        for node in self.transform_nodes:
            node.setDaemon(True)
            node.start()

        for node in self.sink_nodes:
            node.setDaemon(True)
            node.start()

    def init_nodes(self):
        self.init_source_node()
        self.init_transform_nodes()
        self.init_sink_nodes()

    def init_source_node(self):
        source: dict = self.task_info.get("source")
        self.source_node = SourceNode(source, self.context)

    def init_transform_nodes(self):
        transforms = self.task_info.get("transforms")
        for trans in transforms:
            parent = trans.get("parent", None)
            if parent == self.source_node.id:
                trans_node = TransformNode(trans, self.context)
                self.transform_nodes.append(trans_node)
                self.transform_nodes_map[trans_node.id] = trans_node
                self.source_node.register_node(trans_node)

    def init_sink_nodes(self):
        sinks = self.task_info.get("sinks")
        for sink in sinks:
            parent = sink.get("parent", None)
            parent_node: TransformNode = self.transform_nodes_map.get(parent, None)
            if parent_node:
                sink_node = SinkNode(sink, self.context)
                self.sink_nodes.append(sink_node)
                parent_node.register_node(sink_node)


if __name__ == '__main__':
    with open('task.json', 'r') as f:
        task_json = json.loads(f.read())

    task = TaskRunner(task_json)
    task.start()
