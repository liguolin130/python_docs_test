# row = 1
#
# while row <= 5:
#     col = 1
#     while col <= row:
#         print('*',end='')
#         col += 1
#     print('')
#     row = row + 1


row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d*%d=%d" %(col, row, row*col), end="\t")
        col += 1
    print("")
    row += 1
    