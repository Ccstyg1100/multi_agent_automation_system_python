def run(self):
    print("🔥 scheduler启动")

    count = 0

    while not self.queue.is_empty():
        task = self.queue.get_task()
        print(f"👉 处理任务: {task}")

        count += 1

    print(f"✅ 执行完成，总任务数: {count}")
