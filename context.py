from common import get_logger


class Context:
    def __init__(self, task_info: dict):
        self._task_info = task_info
        self._task_id = task_info.get('taskId', '')
        self._property_dict = {}
        self._logger = get_logger(self._task_id)

    @property
    def logger(self):
        return self._logger

    @property
    def task_info(self):
        return self._task_info

    def set_property(self, key, value):
        self._property_dict[key] = value

    def get_property(self, key):
        return self._property_dict.get(key, None)
