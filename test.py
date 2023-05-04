

row_count = 2
col_count = 3


# 遍历每个单元格，对其进行设置
# for row in range(row_count):
#     table_row = {
#         'tableCells': []
#     }
#     for col in range(col_count):
#         table_cell = {
#             'content': f'Row {row}, Column {col}'
#         }
#         table_row['tableCells'].append(table_cell)
#     print(table_row)

for row in range(row_count):
    # table_row = {
    #     'table_cells': []
    # }
    # print(table_row['table_cells'])
    for col in range(col_count):
        table_cell = f'{row,col}'

        # print(table_cell['content'])
        print(table_cell)
    break