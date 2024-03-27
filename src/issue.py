from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql_connector as ms

def issueBook():
    cur = ms.con.cursor()
    issueTable = "books_issued"
    bookTable = "books"  # Book Table
    bid = bookInfo1.get()
    sid = bookInfo2.get()
    issueSql = "insert into " + issueTable + " (bid,issuedto) values ('" + bid + "','" + sid + "')"
    update="update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
    print(issueSql)
    cur.execute("select * from books where bid = '" + bid + "' and status = 'issued'")
    if(cur.fetchone() is not None):
        messagebox.showinfo('Error', "Book is already issued")
        root.destroy()
    else:
        try:
            cur.execute(issueSql)
            cur.execute(update)
            ms.con.commit()
            messagebox.showinfo('Success', "Book Issued Successfully")
        except:
            messagebox.showinfo('Error', "Can't issue the book")
        print(bid)
        print(sid)
        root.destroy()

def issue():
    global bookInfo1, bookInfo2, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Issue Books")
    root.minsize(width=400, height=400)
    root.geometry("1020x735")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="magenta")
    Canvas1.pack(expand=True, fill="both")

    headingFrame1 = Frame(root,bg="Yellow",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Issue Books", bg='black', fg='white', font = ('Courier New',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    lb1=Label(labelFrame,text='Book ID:', bg='black',fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    lb2=Label(labelFrame,text='Student ID:', bg='black',fg='white')
    lb2.place(relx=0.05, rely=0.5, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)

    #Submit Button
    SubmitBtn = Button(root, text="ISSUE", bg='black', fg='white', font=('Courier New', 11), command=issueBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="QUIT", bg='black', fg='white', font=('Courier New', 11), command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
