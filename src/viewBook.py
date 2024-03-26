from tkinter import *

import mysql
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql_connector as sql



def View():
    cur = sql.con.cursor(buffered=True)
    table = "books"

    root = Tk()
    root.title("View Books")
    root.minsize(width=400, height=400)
    root.geometry("1020x735")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="aqua")
    Canvas1.pack(expand=True, fill="both")

    headingFrame1 = Frame(root,bg="Yellow",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier New', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-30s%-20s%-10s" % ('BID', 'Title', 'Author', 'Status'),bg='black', fg='white',font=('Courier New', 11)).place(relx=0.07, rely=0.1)
    Label(labelFrame, text = "---------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = "SELECT * FROM "+table+ ";"
    try:
        cur.execute(getBooks)
        sql.con.commit()
        result = cur.fetchall()
        for i in result:
            Label(labelFrame, text="%-10s%-30s%-20s%-10s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white',font=('Courier New', 11)).place(
                relx=0.07, rely=y)
            y += 0.1
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        messagebox.showinfo("Error", "Failed to fetch files from the database")

    quitBtn =quitBtn = Button(root, text="QUIT", bg='black', fg='white',font = ('Courier New',11), command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    root.mainloop()
