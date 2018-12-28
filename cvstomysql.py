# 导入必要模块
import os
import pandas as pd
import datetime
from sqlalchemy import create_engine


#获取开始时间
starttime = datetime.datetime.now()

#初始化数据库连接，使用pymysql模块,依次为用户名，密码，端口,数据库名
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/cms')

#定义函数
def csvtomysql(sourcedir,stockfile):
    
#获取文件完整路径
    filepath = os.path.join(sourcedir, stockfile)  

#原始数据读取
    df = pd.read_csv(filepath, sep=',')

#生成对应的数据库表名
    tablename = stockfile[0:8]

#写入数据库    
    df.to_sql(tablename, con=engine, if_exists='fail',index=False,chunksize=1000)
    print('写入数据表',tablename,'成功！')

#通达信上证日线csv目录
shpathdir='E:/sys/py37/test/sh/'

#通达信深证日线csv目录
szpathdir='E:/sys/py37/test/sz/'

#列出文件名
shlistfile=os.listdir(shpathdir)

#循环调用函数
for stockfile in shlistfile:
    print('准备入库的文件是:',stockfile)
    csvtomysql(shpathdir,stockfile)

#列出文件名
szlistfile = os.listdir(szpathdir)

#循环调用函数
for stockfile in szlistfile:
    print('准备入库的文件是:',stockfile)
    csvtomysql(szpathdir,stockfile)

#获取结束时间
endtime = datetime.datetime.now()

#计算并打印耗时
extime=(endtime - starttime).seconds
print('所有csv文件入库成功！！'+'耗时合计'+str(extime)+'秒')

