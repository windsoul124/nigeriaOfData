import pymysql
import string

db = pymysql.connect(host='192.168.124.105',
                     user='root',
                     port=3306, passwd='123456',
                     database='Nigeria')

cursor = db.cursor()
sql1 = "SELECT  * FROM APP_Data"
cursor.execute(sql1)
data1 = cursor.fetchall()
gplay_list = []
for row in data1:
    gplay_list.append(row[1])


sql2 = "SELECT * FROM Variables_all"
cursor.execute(sql2)
data2 = cursor.fetchall()

for person in data2:
    amount = 0
    for i in gplay_list:
        if (i in person[37]) is True:
            amount +=1
    percent = round((amount / person[40]), 2)
    dataList = [percent, person[0]]
    sql3 = """UPDATE Variables_all SET app_fromGplay = %s WHERE user_id = %s"""
    print(percent, person[0])
    cursor.execute(sql3, dataList)
    db.commit()
