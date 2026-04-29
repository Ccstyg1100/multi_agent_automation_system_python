import random

class AnalysisAgent:
    def analyze(self, content):
        return {
            "content": content,
            "engagement": random.randint(1, 100)
        }
