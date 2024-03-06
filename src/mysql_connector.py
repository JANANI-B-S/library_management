import mysql.connector as ms;

con = ms.connect(
    host="localhost",
    user="root",
    database="lbms",  # name your database here
    passwd="1502"  # enter your mysql passwd here
)


if con.is_connected():
    print("database connected")
else:
    print("connection unsuccessful")
