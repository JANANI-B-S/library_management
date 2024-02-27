import mysql.connector as ms;

con = ms.connect(
    host="localhost",
    user="root",
    database="LBMS",  # name your database here
    passwd="1502"  # enter your mysql passwd here
)
cur = con.cursor()

if con.is_connected():
    print("database connected")
else:
    print("connection unsuccessful")
