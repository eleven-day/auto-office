from docx2pdf import convert
import os

# 文件位置
path = ''
# 定义空list,存放文件列表
files = []
for file in os.listdir(path):
    if file.endswith(".docx"):
        files.append(path+file)
files
for file in files:
   convert(file,file.split('.')[0]+'.pdf')
   print(file+'转换成功')