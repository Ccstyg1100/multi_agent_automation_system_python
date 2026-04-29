from core.scheduler import Scheduler
from core.queue_manager import TaskQueue

def main():
    print("🚀 main启动成功")   # 👈 必须看到这个

    queue = TaskQueue()

    for i in range(5):
        queue.add_task({
            "id": i,
            "topic": f"测试任务 {i}"
        })

    scheduler = Scheduler(queue)
    scheduler.run()

if __name__ == "__main__":
    main()
