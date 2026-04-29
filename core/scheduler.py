from agents.content_agent import ContentAgent
from agents.analysis_agent import AnalysisAgent
from agents.optimizer_agent import OptimizerAgent
from core.ab_test import ABTest
from data.storage import DataStorage

class Scheduler:
    def __init__(self, queue):
        self.queue = queue
        self.content_agent = ContentAgent()
        self.analysis_agent = AnalysisAgent()
        self.optimizer_agent = OptimizerAgent()
        self.ab_test = ABTest()
        self.storage = DataStorage()

    def run(self):
        while not self.queue.is_empty():
            task = self.queue.get_task()

            prompt = self.ab_test.select_prompt(task["topic"])
            content = self.content_agent.generate(prompt)
            result = self.analysis_agent.analyze(content)
            self.storage.save(result)
            self.optimizer_agent.optimize(result)

            print(f"完成任务: {task['id']}")
