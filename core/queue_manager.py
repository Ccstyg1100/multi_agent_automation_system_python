from queue import Queue

class TaskQueue:
    def __init__(self):
        self.queue = Queue()

    def add_task(self, task):
        self.queue.put(task)

    def get_task(self):
        if not self.queue.empty():
            return self.queue.get()
        return None

    def is_empty(self):
        return self.queue.empty()
