list = [1,2,3,4,5,6,7,8,9]

count = 0
for i, l in enumerate(list):
    # print(count)
    if count == 3:
        print()  # 打印出新的一行
        count = 0
    count += 1
    print(l, end="")