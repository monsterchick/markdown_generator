global index2
text = '[![{a}]({b})]({c})'
for i in range(len(list)):
    if index2 % 3 == 1:
        t = text.format(a=list[i], b='', c='')
        print(t)
    if index2 % 3 == 2:
        t = text.format(a='', list[i], '')
        print(t)
    if index2 % 3 == 0:
        t = text.format('', '', list[i])
        print(t)
    else:
        print(False)
    index2 += 1


    global index2
    text = ['[![','a','](','b',')](','c']

    text[1] = list[index2]
    index2 += 1
    text[3] = list[index2]
    index2 += 1
    text[5] = list[index2]
    print(text)
    # for i in range(len(list)):
    #     telist[i]






        for i in range(len(list)-1):
            li.append('[!['+list[index]+'](')
            index += 1
            break
        for i in range(len(list) - 1):
            li.append(list[index]+')](')
            index += 1
            break
        for i in range(len(list) - 1):
            li.append(list[index] + ')')
            index += 1
            break
    print(index)
    print(li)