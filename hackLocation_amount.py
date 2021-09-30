import pymysql
import string

db = pymysql.connect(host='192.168.124.105',
                     user='root',
                     port=3306, passwd='123456',
                     database='Nigeria')

cursor = db.cursor()

relative_list = ['fake', 'faker', 'Fake', ]
sql = "SELECT * FROM Variables_all"
cursor.execute(sql)
data = cursor.fetchall()

for person in data:
    amount = 0
    for i in relative_list:
        if (i in person[36]) is True:
            amount += 1
    dataList = [amount, person[0]]
    sql1 = """UPDATE Variables_all SET app_hackLocationSort = %s WHERE user_id = %s"""
    print(amount, person[0])
    cursor.execute(sql1, dataList)
    db.commit()
