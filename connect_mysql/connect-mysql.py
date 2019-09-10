# -*-coding: utf-8-*-
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='test_mysql'
)
mycursor = mydb.cursor()

# mycursor.execute('CREATE DATABASE test_mysql')
# mycursor.execute('SHOW DATABASES')
#
# for x in mycursor:
#     print(x)

# mycursor.execute('CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))')

# mycursor.execute('SHOW TABLES')
#
# for x in mycursor:
#     print(x)

# mycursor.execute('DROP DATABASE test')

# mycursor.execute(
#     'CREATE TABLE IF NOT EXISTS `runoob_tbl`('
#     '`runoob_id` INT UNSIGNED AUTO_INCREMENT,'
#     ' `runoob_title` VARCHAR(100) NOT NULL,'
#     '`runoob_author` VARCHAR(40) NOT NULL,'
#     '`submission_date` DATE,'
#     'PRIMARY KEY ( `runoob_id` )'
#     ')ENGINE=InnoDB DEFAULT CHARSET=utf8;'
# )

# mycursor.execute(''
#     'ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'
# )

# sql = 'INSERT INTO sites (name, url) VALUES  (%s, %s)'
# val = ('Runoob', 'http://www.baidu.com')
# mycursor.execute(sql, val)
# mydb.commit()
# print('插入成功')

# sql = 'INSERT INTO sites (name, url) VALUES (%s, %s) '
# val = [
#     ('taobao', 'https://www.taobao.com'),
#     ('jd', 'https://www.jd.com'),
#     ('souhu', 'https://www.souhu.com'),
#     ('didi', 'https://www.didi.com'),
#     ('tencent', 'https://www.qq.com')
# ]
#
# mycursor.executemany(sql, val)
# mydb.commit()
# print('批量插入成功')

# sql = 'SELECT name, url from sites ORDER BY name DESC LIMIT 3 OFFSET 1'
# sql = 'DELETE FROM sites WHERE name="taobao"'
# mycursor.execute(sql)
# # myresult = mycursor.fetchall()
# mydb.commit()
#
# # for x in myresult:
# #     print(x)

# sql = 'UPDATE sites SET url="https://www.zenquan.cn", name="sohu" where url=%s'
# url = ('https://www.souhu.com',)
# mycursor.execute(sql, url)
# mydb.commit()

# sql = 'DROP TABLE IF EXISTS runoob_tbl'
# mycursor.execute(sql)

sql1 = '''
    SELECT name, SUM(singin) as singin_count from employee_tbl GROUP BY name
'''
sql2 = '''
    SELECT name, COUNT(*) from employee_tbl GROUP BY name
'''
mycursor.execute(sql1)


myresult = mycursor.fetchall()

print(myresult)
