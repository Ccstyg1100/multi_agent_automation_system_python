class OptimizerAgent:
    def __init__(self):
        self.best_score = 0
        self.best_prompt = None

    def optimize(self, result):
        if result["engagement"] > self.best_score:
            self.best_score = result["engagement"]
            self.best_prompt = result["content"]
            print(f"🔥 新爆款策略！score={self.best_score}")
