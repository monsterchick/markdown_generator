from save_to_dict import temp
import os
from pointer import work

temp_list = []
index = 0
index2 = 0

output_file = os.path.join(os.getcwd(), 'files', 'add_text{}.txt'.format('_output'))


def clean_file():
    with open(output_file, 'w') as f:
        f.truncate(0)
    f.close()

def save_to_list(single_line):
    temp_list.append(single_line)
def output_image_with_link(list):
    text = ''
    curly = '{}'
    # print(list)
    for i in list:
        text = text + curly + i
    text += curly
    # print(text.format('[![', '](', ')](', ')\n'))    # can only handle first 3 lines
    with open(output_file, 'w') as f:
        content = text.format('[![', '](', ')](', ')\n')
        f.write(content)
    f.close()


# handle bullet_point
def output_bullet_point(single_line):
    with open(output_file, 'a') as f:
        content = '{w}{s}\n'.format(s=single_line,w=work)
        f.write(content)
    f.close()

# handle backtick
def output_backtick(single_line):
    # print('work:',work)
    with open(output_file, 'a') as f:
        content = '{w}\n{s}\n{w}\n'.format(s=single_line,w=work)
        f.write(content)
    f.close()

# handle hash
def output_hash(single_line):
    with open(output_file, 'a') as f:
        content = '{w}{s}\n'.format(s=single_line,w=work)
        f.write(content)
    f.close()


def get_line():
    # print(temp)
    clean_file()  # clean the file
    for i in range(0, list(temp.keys())[-1] + 1):
        # print(temp[i].strip())
        single_line = temp[i].strip()
        # print(single_line)
        if '#' in work:
            output_hash(single_line)
        elif '`' in work:
            output_backtick(single_line)
        elif '*' in work:
            output_bullet_point(single_line)
        elif '!' in work:
            save_to_list(single_line)
            output_image_with_link(temp_list)
        else:
            pass
    # return temp_list

get_line()
print('generated successfully!')
# print(get_line())