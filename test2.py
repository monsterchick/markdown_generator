import json


data = {'t': 'd'}
data_list = []
title = ''


def read_data_json():
    titles = []
    datas = []
    with open('data.json', 'r', encoding='utf-8') as f:

        data = json.load(f)
        column_num = len(data.keys())
        # titles = data.values()
        columns = list(data.values())
        # print(columns)
        for col in columns:
            titles.append(col['title'])
            datas.append(col['data_list'])
    # print(titles)
    # print(datas)
    return titles, datas
    # print(datas)
    # [print(i['columns']) for i in columns]


class Table:
    def __init__(self):
        self.data = read_data_json()
        self.titles = read_data_json()[0]
        self.datas = read_data_json()[1]


    def rm_symbol(self,head):
        if '||' in head:
            head = head.replace('||', '|')
        return(head)
    # make table
    def add_head(self):
        head = ''
        for title in self.titles:
            head += f'| {title} |'

        # remove '|'
        head = self.rm_symbol(head)
        print(head)


    def add_dash(self):
        dash = ''
        count_data = len(self.datas)
        # print(count_data)
        dash += f'| {"-"*count_data} |'
        dash *= count_data
        dash = self.rm_symbol(dash)
        print(dash)

    # def add_record(self):
    #     [print(f'| {i} |') for i in self.datas]
    #     # print(self.datas)
    #     for data in self.datas:
    #         # print(data)
    #         # print(max(length))

def create_table():
    t = Table()
    t.add_head()
    t.add_dash()
    # t.add_record()
    # t.add_empty_head()

create_table()
