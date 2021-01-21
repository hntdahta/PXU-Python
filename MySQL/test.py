import mysql.connector

# Kiểm thử kết nối
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

print(mydb)

# Liệt kê các cơ sở dữ liệu có trong máy chủ csdl
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for item in mycursor:
    print(item)

mydb.close()