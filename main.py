import pymysql


db = pymysql.connect(host='192.168.124.105',
                     user='root',
                     port=3306, passwd='123456',
                     database='Nigeria')

cursor = db.cursor()
sql = "SELECT * FROM APP WHERE user_id='793560'"
cursor.execute(sql)
data = cursor.fetchall()
print(data)