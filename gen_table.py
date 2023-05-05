import json
import sys


class Json():
    def __init__(self):
        pass

    def read_json(self):
        with open('input.json', 'r', encoding='utf-8') as f:
            datas = json.load(f)
            header = datas['header']
            data = datas['data']
            return header, data


class Handle():
    def __init__(self):
        pass

    def remove_pipe(self, head):
        if '||' in head:
            head = head.replace('||', '|')
        return head


class Table():
    def __init__(self):
        self.handle = Handle()
        # print(handle.remove_pipe('asdf--asdf--asf-||asdf||sdf||'))
        self.header = Json.read_json(self)[0]
        self.data = Json.read_json(self)[1]

    def test_var(self):
        var1 = self.header
        var2 = self.data
        return var1, var2

    def check_data(self):
        num_header = len(Json.read_json(self)[0])
        num_data = len(Json.read_json(self)[1])
        if num_header != num_data:
            print("The length of the header and data list do not match. Please check input.json and restart the program.")
            sys.exit()
    def add_header(self):
        header = ''
        for head in self.header:
            header += f'| {head} |'

        # remove "|"
        header = self.handle.remove_pipe(header)
        print(header)

    def add_dash(self):
        seperator = ''
        for head in self.header:
            seperator += f'| {"-" * len(head)} |'

        seperator = self.handle.remove_pipe(seperator)
        print(seperator)

    def add_record(self):
        data = ''
        len_sublist = len(self.data[0])

        main_list = self.data
        for i in range(len_sublist):
            # print(i)
            for sublist in main_list:
                # print(sublist[i],end="")
                data += f'| {sublist[i]} |'
                # print(f'| {sublist[i]} |', end = "")
            data += '\n'  # print a new line
            # print()
        data = self.handle.remove_pipe(data)
        print(data)


def create_table():
    t = Table()
    t.check_data()   # check if the input file valid
    t.add_header()  # print header
    t.add_dash()  # print seperator
    t.add_record()  # print data

    # print('test',t.test_var()[0])   # test variables
    # print('test',t.test_var()[1])   # test variables


create_table()
