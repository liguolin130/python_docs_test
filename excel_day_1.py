# import xlrd
# from matplotlib import rcParams
# from matplotlib._cm_listed import data
#
# #
# # def read_excel(row_num=None, col_num=None):
# #     work_book = xlrd.open_workbook("./test1/beng.xls",file_contents= data)
# #     work_book.sheet_names()
# #     sheet = work_book.sheet_by_index(0)
# #     sheet = work_book.sheet_by_name(u"Sheet1")
# #     row = sheet.row
# #     col = sheet.cols # 列
# #     sheet.row_values(row_num) # 查询行数据
# #     sheet.col_values(col_num)
# #     va = sheet.cel(row_num, col_num).values
# #
# #  def work_bing(plot=None, plt=None):
# #      labels = ["国"]
# #      sizes = []
# #      colors = ['red', 'yellow', 'blue', 'green']
# #      explode = (0.05, 0, 0, 0)
# #      patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
# #                                         labeldistance=1.1, autopct='%2.0f%%', shadow=False,
# #                                         startangle=90, pctdistance=0.6)
#
# labels = ["国"]
# #print(rcParams["font.sans-serif"]="labels")
#
#
#
#

import re
user = input(":")
ret = re.sub("色情|落体","**",user)
print(ret)



