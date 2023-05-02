import pandas as pd
import json


data = {'t': 'd'}
data_list = []
title = ''


def read_data_json(key):
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)[key]
        # print(data)
        return data
    f.close()


data_list = read_data_json('data')
title = read_data_json('title')
def create_table(title, data_list):
    data.pop('t')
    data[title] = data_list


    # 使用pandas库将字典转换为DataFrame
    df = pd.DataFrame(data)

    # 使用pandas的to_markdown()方法生成Markdown格式的表格
    markdown_table = df.to_markdown(index=False)

    # 打印Markdown表格
    print(markdown_table)

create_table(title, data_list)
