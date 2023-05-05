list1 = [1, 2, 3, 4, 5]
list2 = ['apple', 'banana', 'orange', 'grape']
list3 = [True, False, True]

index = 0  # 记录当前正在处理的元素索引
while index < len(list1) or index < len(list2) or index < len(list3):
    if index < len(list1):
        print(list1[index], end=' ')
    else:
        print(' ', end=' ')  # 如果列表1没有元素，则打印一个空格占位符

    if index < len(list2):
        print(list2[index], end=' ')
    else:
        print(' ', end=' ')  # 如果列表2没有元素，则打印一个空格占位符

    if index < len(list3):
        print(list3[index])
    else:
        print('')  # 如果列表3没有元素，则打印一个换行符

    index += 1  # 处理下一个元素
