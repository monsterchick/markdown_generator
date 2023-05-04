import pandas as pd
import json

data_list = []
title = ''


def read_data_json():
    with open('data.json', 'r', encoding='utf-8') as f:
        datas = json.load(f)
        data_list = []
        for i in datas:
            # print(datas[i]['title'])
            # print(datas[i]['data_list'])
            data_list.append((datas[i]['title'],datas[i]['data_list']))
        print(data_list)
        return data_list
        # 處理每一列
        # print(datas['0'])
        # print(datas['1'])
        # return title, len(datas)

class Table():
    def __init__(self):
        self.title = read_data_json()[0]
        self.data_list = read_data_json()[1]

    def rm_symbol(self, head):
        if '||' in head:
            head = head.replace('||', '|')
        return head

    # make table
    def add_head(self):
        head = ''
        head += f'| {self.title} |'

        # remove '|'
        head = self.rm_symbol(head)
        print(head)


    def add_dash(self):
        dash = ''
        count_data = len(self.title)
        # print(count_data)
        dash += f'| {"-"*count_data} |'
        dash = self.rm_symbol(dash)
        print(dash)

    def add_record(self):
        for d in self.data_list:
            print(f'| {d} |')



def create_table():
    t = Table()
    t.add_head()
    t.add_dash()
    t.add_record()


# for i in range(read_data_json()[2]):
create_table()