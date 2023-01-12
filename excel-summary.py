import os 
import pandas as pd

os.chdir(r'D:\\office\\德邦物流\\')

file_name_li = os.listdir(r'D:\\office\\德邦物流\\')

all_data_li = []

for file_name in file_name_li:
    all_data = pd.read_excel(file_name)
    all_data_li.append(all_data)

writer = pd.ExcelWriter('./汇总.xlsx')

df = pd.concat(all_data_li)

df.to_excel(writer, sheet_name='往来辅助账2020', index=False)

writer.save()
    