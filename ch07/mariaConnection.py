import pymysql

db = pymysql.connect(host='localhost', user='root', password='1234',
db='IncheonNational', charset='utf8')

cur=db.cursor()
cur.execute("select * from student")

rows=cur.fetchall()
print(rows)

db.close()