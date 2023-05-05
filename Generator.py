import json

# data_list = []
# title = ''


def read_data_json():
    with open('data.json', 'r', encoding='utf-8') as f:
        datas = json.load(f)
        data_list = []
        for i in datas:
            # print(datas[i]['title'])
            # print(datas[i]['data_list'])
            data_list.append((datas[i]['title'],datas[i]['data_list']))
        # print(data_list)
        return data_list
        # 處理每一列
        # print(datas['0'])
        # print(datas['1'])
        # return title, len(datas)

class Table():
    def __init__(self):
        self.title = read_data_json()[0][0]
        self.data_list = read_data_json()[0][1]

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
        # print(head)
        return head


    def add_dash(self):
        dash = ''
        count_data = len(self.title)
        # print(count_data)
        dash += f'| {"-"*count_data} |'
        dash = self.rm_symbol(dash)
        # print(dash)
        return dash

    def add_record(self):
        list = []
        for d in self.data_list:
            list.append(f'| {d} |')
        return list
def create_table():
    # final colomn, can add extra column
    list = []

    t = Table()
    list.append(t.add_head())
    list.append(t.add_dash())
    [list.append(i) for i in t.add_record()]
    # [print(i) for i in list]
    return list

def add_col(col_num):
    t = Table()
    list = create_table()
    for i in list:
        i += '  |' * col_num
        if ('--' in i):

            print(t.rm_symbol(t.add_dash() * (col_num+1)))
            continue
        else:
            print(i)

        # if (count == 0):
        #     print(t.add_dash() * col_num)
        #     pass



# for i in range(read_data_json()[2]):
create_table()
add_col(2)