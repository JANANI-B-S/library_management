
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql_connector as sql

def RegisterBook():
    cur = sql.con.cursor()
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = "Available"
    status = status.lower()
    if (bid==""):
        messagebox.showinfo("Error", "Values are empty")
        return "null"

    insert = "INSERT INTO " + bookTable +" (bid,title,author,status) " + " VALUES ('" + str(bid) + "', '" + str(title) + "', '" + str(author) + "', '" + str(status) + "');"

    try:
        cur.execute(insert)
        sql.con.commit();
        messagebox.showinfo("Success","Book added to database successfully")
    except:
        messagebox.showinfo("Error","Can't add the book to database")

    print(bid)
    print(title)
    print(author)
    print(status)
    root.destroy()

def addBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, bookTable,root

    root = Tk()
    root.title("Add Books")
    root.minsize(width=400, height=400)
    root.geometry("1020x735")

    bookTable = "books"

    Canvas1 = Canvas(root)
    Canvas1.config(bg="Green")
    Canvas1.pack(fill="both",expand=True)

    headingFrame1 = Frame(root,bg="Yellow",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font = ('Courier New',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    lb1=Label(labelFrame,text='Book ID:', bg='black',fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='black', fg='white',font = ('Courier New',11),command=RegisterBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="QUIT", bg='black', fg='white',font = ('Courier New',11), command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()





