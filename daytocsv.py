# %% 导入包 
from struct import * 
import os 
import pandas as pd 
def daytocsv(sourcedir,targetdir,stockfile):
    #原始数据读取存储入缓存
    srcfile = open(sourcedir + os.sep + stockfile, 'rb')
    buffer = srcfile.read()
    srcfile.close()
    #读取的数据长度
    buflengh = len(buffer) #32的整数倍
    #除32获利文件中存储了多少天的信息
    datenum = int(buflengh / 32)
    #解析每一天的数据的内容,每一天列表的起始位置和终止位置
    list_begin = 0
    list_end = 32
    #创建pandas股票数据表
    seriesdata = pd.Series() #创建列表
    stockdata = pd.DataFrame(index =range(0,datenum),columns =['date','open','high','low','close','amount','volum'])
    print(stockdata.index)
    #将个股数据转换为pandas的dataFrame格式数据
    for i in range(datenum):
        #解析32个字节一天数据
        unitdata = unpack('IIIIIfII', buffer[list_begin:list_end])
        date  = unitdata[0]
        opens = unitdata[1] / 100.0
        high  = unitdata[2] / 100.0
        low   = unitdata[3] / 100.0
        close = unitdata[4] / 100.0
        amount = unitdata[5] / 10.0
        vol = unitdata[6]
        unused = unitdata[7]
         #加32指向下一天的数据列表
        list_begin = list_begin + 32
        list_end = list_end + 32

        seriesdata = [ date, opens, high, low, close, amount, vol]
       # print(unitdata)
        stockdata.at[stockdata.index[i],'date'] = seriesdata[0]
        stockdata.at[stockdata.index[i],'open'] = seriesdata[1]
        stockdata.at[stockdata.index[i],'high'] = seriesdata[2]
        stockdata.at[stockdata.index[i],'low']  = seriesdata[3]
        stockdata.at[stockdata.index[i],'close'] = seriesdata[4]
        stockdata.at[stockdata.index[i],'amount'] = seriesdata[5]
        stockdata.at[stockdata.index[i],'volum']  = seriesdata[6]
    #生成对应的文件
    savefilename = stockfile[0:8]
    print(savefilename)
    stockdata.to_csv(targetdir + os.sep + savefilename +' .csv', encoding='gbk')
    
#通达信上证日线数据目录
shpathdir='E:/client/yhzq/vipdoc/sh/lday'
#通达信深证日线数据目录
szpathdir='E:/client/yhzq/vipdoc/sz/lday'
#通达信数据转换后存储目录
shtargetDir='E:/sys/py37/test/sh'
sztargetDir='E:/sys/py37/test/sz'

#将上证目录下的所有文件列表出来
shlistfile = os.listdir(shpathdir)
for stockfile in shlistfile:
    print(stockfile)
    daytocsv(shpathdir,shtargetDir,stockfile)
#将深证目录下的所有文件列表出来
szlistfile = os.listdir(szpathdir)
for stockfile in szlistfile:
    print(stockfile)
    daytocsv(szpathdir,sztargetDir,stockfile)
