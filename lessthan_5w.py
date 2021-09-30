import pymysql
import string

db = pymysql.connect(host='192.168.124.105',
                     user='root',
                     port=3306, passwd='123456',
                     database='Nigeria')

cursor = db.cursor()
sql1 = "SELECT  * FROM min_installs"
cursor.execute(sql1)
data1 = cursor.fetchall()
loan_list = []
for row in data1:
    loan_list.append(row[1])
sql2 = "SELECT * FROM Variables_all"
cursor.execute(sql2)
data2 = cursor.fetchall()

for person in data2:
    amount = 0
    for i in loan_list:
        if (i in person[37]) is True:
            amount +=1
    dataList = [amount, person[0]]
    sql3 = """UPDATE Variables_all SET lessthan_5w = %s WHERE user_id = %s"""
    print(amount, person[0])
    cursor.execute(sql3, [amount, person[0]])
    db.commit()
