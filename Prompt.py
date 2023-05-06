import json


class Prompt:
    def get_prompt(self):
        with open("prompts.json", "r", encoding="utf-8") as f:
            prompt = json.load(f)
            prompt = prompt['markdown代码生成器']['prompt']
        return prompt

