import threading
from abc import ABC, abstractmethod
from threading import Thread
from typing import Optional

from component.component import BaseComponent
from context import Context
from data.data import BaseData


class NodeSubject(object):
    def __init__(self):
        self._next_nodes = []

    def register_node(self, node):
        self._next_nodes.append(node)

    @property
    def next_nodes(self):
        return self._next_nodes

    def notify_all(self, data: BaseData):
        node: NodeObserver
        for node in self._next_nodes:
            node.update(data)


class NodeObserver(ABC):
    @abstractmethod
    def update(self, data: BaseData):
        pass


class BaseNode(Thread):
    def __init__(self, node_info=None, context: Context = None):
        super().__init__()
        self._node_info = node_info
        self._context = context
        self._logger = self._context.logger

        self._id = self._node_info.get("id")
        self._name = self._node_info.get("name")
        self._type = self._node_info.get("type")
        self._config = self._node_info.get("config", [])

        self._lock = threading.Lock()
        self._event = threading.Event()

        self.running = True
        self.component: Optional[BaseComponent] = None
        self.pre_data: Optional[BaseData] = None
        self.current_data: Optional[BaseData] = None

    @property
    def lock(self):
        return self._lock

    @property
    def id(self):
        return self._id

    @property
    def context(self):
        return self._context

    @property
    def logger(self):
        return self._logger

    @property
    def config(self):
        return self._config

    @property
    def event(self):
        return self._event

    def resume(self):
        self._event.set()

    def suspend(self):
        self._event.clear()
        self._event.wait()

    def exit(self):
        self.running = False

    def get_data(self):
        with self.lock:
            self.current_data = self.pre_data

    def release(self):
        self.component.terminate()
