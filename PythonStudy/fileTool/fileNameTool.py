#
# import os
# from openpyxl import Workbook
#
# wb = Workbook()
# dest_filename = '音频列表.xlsx'
# ws1 = wb.active
# ws1.title = "音频列表"
# fileNameList = [];
# # name = ''
# def file_name(file_dir):
#     for root, dirs,files in os.walk(file_dir):
#         print(root)
#         print(dirs)
#         print(files)
#         for name in files:
#             print(name)
#
# def file_name1(file_dir):
#     L=[]
#     for root, dirs, files in os.walk(file_dir):
#         for file in files:
#             if os.path.splitext(file)[1] == '.wav':
#                 L.append(os.path.splitext(file)[0])
#     return L
# def main():
#     fileDir = "/Users/shanfangliang/Desktop/工作文档/跑道检查频率"
#     fileNameList = file_name1(fileDir)
#     print(fileNameList)
#     print(fileNameList.__len__())
#     for file in fileNameList:
#         col_A = 'A%s' % (fileNameList.index(file))
#
#         ws1[col_A] = file
#
#     wb.save(filename=dest_filename)
#
#
#
# if __name__ == '__main__':
#     main()