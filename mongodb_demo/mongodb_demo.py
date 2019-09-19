import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['runoobdb']

dblist = myclient.list_database_names()
# dblist = myclient.database_names() 
if "runoobdb" not in dblist:
  print("数据库不存在！")