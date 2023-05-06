import os

# files path
file = os.path.join(os.getcwd(), 'files', 'add_text.txt')
# print(file)
temp = {}
key = 0

with open(file, 'r') as f:
    # read content line by line
    for l in f:  # skip empty line
        if l != '\n':
            line = l.strip()  # delete newline character
        else:
            continue
        # print(line)
        temp[key] = line
        key += 1
        # print('line:',line)


if '__main__'=='__name__':
    print('dict: {}'.format(temp))
