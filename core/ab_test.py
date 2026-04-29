import random

class ABTest:
    def __init__(self):
        self.prompts = [
            "写一个爆款短视频脚本：{}",
            "生成一个高点击率视频内容：{}"
        ]

    def select_prompt(self, topic):
        template = random.choice(self.prompts)
        return template.format(topic)
