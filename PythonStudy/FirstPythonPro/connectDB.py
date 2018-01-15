import pymysql

db = pymysql.connect("localhost", "test", "******", "ImageProcessing", charset='utf8')

cursor = db.cursor()

# sql 查询语句
sql = "SELECT * FROM runoob_tbl"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname0 = row[0]
        fname1 = row[1]
        fname2 = row[2]
        fname3 = row[3]
        print("fname=%s, fname1=%s, fname2=%s, fname3=%s" % (fname0, fname1, fname2, fname3))
except:
    print("Error: unable to fetch data")




# cursor.execute("SELECT VERSION()")
#
# data = cursor.fetchone()
#
# print("Database version : %s " % data)

db.close()