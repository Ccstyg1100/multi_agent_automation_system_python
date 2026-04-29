def main():
    print(" 系统启动中...")  

    queue = TaskQueue()

    for i in range(10):
        queue.add_task({
            "id": i,
            "topic": f"短视频选题 {i}"
        })

    scheduler = Scheduler(queue)
    scheduler.run()

if __name__ == "__main__":
    main()
