import json

class ReadData:
    def get_data(self):
        with open("data.json", "r", encoding="utf-8") as f:
            title = json.load(f)["title"]

        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)["data"]

            return title,data
