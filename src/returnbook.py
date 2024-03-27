from tkinter import messagebox
from PIL import ImageTk, Image
import mysql_connector as ms
from tkinter import *


def ret():
    cur = ms.con.cursor()
    issueTable = "books_issued"
    bookTable = "books"
    bid = bookInfo1.get()
    delete = "delete from "+issueTable+" where bid='"+bid+"'"
    update = "update books set status='Available' where bid='"+bid+"'"
    cur.execute("select * from books where bid='"+bid+"' and status='Available'")
    if(cur.fetchone() is not None):
        messagebox.showinfo('Error', "Book is not issued")
        root.destroy()
    else:
        try:
            cur.execute(delete)
            cur.execute(update)
            ms.con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        except Exception as e:
            print(e)
            messagebox.showinfo('Error', "Can't return the book")
        print(bid)
        root.destroy()


def returnBook():
    global bookInfo1, Canvas1, root

    root = Tk()

    root.title("Return Book")
    root.minsize(width=400, height=400)
    root.geometry("1020x735")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="silver")
    Canvas1.pack(expand=True, fill="both")

    headingFrame1 = Frame(root, bg="Yellow", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier New', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb1 = Label(labelFrame, text="Book ID:", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5,relwidth=0.2 ,relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(root, text="SUBMIT", bg='black', fg='white', font=('Courier New', 11), command=ret)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="QUIT", bg='black', fg='white', font=('Courier New', 11), command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()