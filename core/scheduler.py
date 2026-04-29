def run(self):
    print("开始执行任务...")

    while not self.queue.is_empty():
        task = self.queue.get_task()
        print(f"👉 正在处理任务: {task['id']}")

        prompt = self.ab_test.select_prompt(task["topic"])
        content = self.content_agent.generate(prompt)
        result = self.analysis_agent.analyze(content)

        print(f"📊 分析结果: {result}")

        self.storage.save(result)
        self.optimizer_agent.optimize(result)

    print("所有任务完成")
