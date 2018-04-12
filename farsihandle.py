# -*- coding: utf-8 -*-

import xlrd
import sys
data = xlrd.open_workbook('MeChat001.xls')
table = data.sheet_by_name(u'iOS')
fstRow = table.row_values(0)
alert = u'选择提取的语言：\n'
langDic = {}
idList = []
for col in range(len(fstRow)):
    tag = fstRow[col]
    if tag == 'id':
        idList = table.col_values(col)
        continue
    langDic[col] = tag
    alert = alert+'\t\t'+str(col)+'------>'+tag +'\n'
sys.stdout.write(alert)
sys.stdout.write(u'选择对应的数字:')
selectIdx = sys.stdin.readline()
langV = langDic[int(selectIdx)]
sys.stdout.write(u'选择的语言为--->'+langV+'\n')

selectCols = table.col_values(int(selectIdx))

if len(selectCols) != len(idList):
    sys.stdout.write('数据文件异常：语言对应错误')
else:
    f = open(r'./'+langV+r'.strings', "w+")
    for i in range(len(idList)):
        if i == 0:
            continue
        id = idList[i].rstrip(',')
        exlang = selectCols[i].rstrip(',')
        r =r'"'+id+r'"'+r'='+r'"'+exlang+r'"'+r';'
        result = u''.join((r,'\n')).encode('utf-8')
        f.write(result)
    f.close()
    sys.stdout.write(u'文件已写入当前目录下:'+langV+r'.strings'+u'中\n')
