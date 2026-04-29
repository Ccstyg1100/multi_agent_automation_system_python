from core.scheduler import Scheduler
from core.queue_manager import TaskQueue

def main():
    queue = TaskQueue()

    for i in range(100):
        queue.add_task({
            "id": i,
            "topic": f"短视频选题 {i}"
        })

    scheduler = Scheduler(queue)
    scheduler.run()

if __name__ == "__main__":
    main()
