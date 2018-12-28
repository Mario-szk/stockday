
该项目是一个通过py处理股票数据然后写入数据库的示例，已经亲测通过，我用的环境是python3.7

1，选择一个通达信股票软件，登录进去后选择盘后数据下载，参考示例图片1

然后选择时间区段进行下载，开始日期可设置为1990101，结尾日期最好选为前一天，因为当日数据可能没有收盘，收盘时间一般是6点后，参考示例图片2

2，编辑daytoscv.py，设置好下载的日线day文件和要转换的csv文件的目录，然后运行daytoscv.py
  说明：day文件都是二进制数据流，所以需要转换才行，不能直接读取。daytoscv.py的作用就是将day文件转成csv格式数据表，该格式可以通过excel读取。
  
  
3，编辑csvtomysql.py，设置好已经转换的csv文件的目录和数据库用户名地址等信息，然后运行csvtomysql.py，该过程较长，需要耐心等待。
  说明：csvtomysql.py文件作用就是将csv转入mysql数据库中，方便调用。

4，对于股票代码和股票名称问题，可参考此过程处理写入数据库中。

PS一下:
df.to_sql(tablename, con=engine, if_exists='fail',index=False,chunksize=1000)这句的chunksize=1000可以根据实际需要修改，但是不能设置为空。实测如果为空，写入数据表过多时会出现卡死。

如果提示ModuleNotFoundError: No module named 'XXX'，则在cmd下运行pip install XXX,需要你安装有pip，pip就是一个安装管理工具，如何安装自行网上搜索。

