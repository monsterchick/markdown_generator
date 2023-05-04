import json


data = {'t': 'd'}
data_list = []
title = ''


def read_data_json(key):
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)[key]
        print('tttttt',data)
        return data

class Table:
    def __init__(self):
        self.title = read_data_json('title')
        self.data_list = read_data_json('data_list')
        self.new_title = read_data_json('new_title')
        self.new_data_list = read_data_json('new_data_list')

    # make table
    def table(self):
        # head of table
        title = f'| {self.title} |'
        count_data = len(self.data_list)
        dash = f'| {"-"*count_data} |'
        print(title)
        print(dash)
        [print(f'| {i} |') for i in self.data_list]

    def add_head(self):
        title = f'| {self.title} |'
        print(title)

    def add_dash(self):
        count_data = len(self.data_list)
        dash = f'| {"-"*count_data} |'
        print(dash)

    def add_record(self):
        [print(f'| {i} |') for i in self.data_list]

    def add_empty_head(self):
        print(self.new_title)
        # if self.new_title is :
        #     print(True)
        # else:
        #     print(False)
        #     # title = f'| {self.title} |'


def create_table():
    t = Table()
    t.add_head()
    t.add_dash()
    t.add_record()
    t.add_empty_head()

create_table()
