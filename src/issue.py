import mysql_connector as ms
from PIL import ImageTk,Image
from tkinter import messagebox, Tk, Canvas, Label, Frame, Entry, Button

issueTable = "books_issued"
bookTable="books"
allBid = []

def issue():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status
    root = Tk()
    root.title("Issue Books")
    root.minsize(width=400, height=400)
    root.geometry("1020x735")
    cur = ms.con.cursor()

    Canvas1 = Canvas(root)
    Canvas1.config(bg="aqua")
    Canvas1.pack(expand=True, fill="both")

    headingFrame1 = Frame(root,bg="Yellow",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Issue Books", bg='black', fg='white', font=('Courier New', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    # Book ID
    lb1=Label(labelFrame,text='Book ID:', bg='black',fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1=Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student
    lb2=Label(labelFrame,text='Issued To:', bg='black',fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2=Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Issue Button
    issueBtn = Button(root, text="Issue", bg='black', fg='white', font=('Courier New', 15), command=issueBook)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="QUIT", bg='black', fg='white', font=('Courier New', 15), command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def issueBook():
    bid = inf1.get()
    issueto = inf2.get()

    issueTable = "books_issued"
    bookTable = "books"
    cur = ms.con.cursor()


    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    extractBid = "select bid from " + bookTable
    try:
        cur.execute(extractBid)
        ms.con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from " + bookTable + " where bid = '" + bid + "'"
            cur.execute(checkAvail)
            ms.con.commit()
            for i in cur:
                check = i[0]

            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "insert into " + issueTable + " values ('" + bid + "','" + issueto + "')"
    show = "select * from " + issueTable

    updateStatus = "update " + bookTable + " set status = 'issued' where bid = '" + bid + "'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            ms.con.commit()
            cur.execute(updateStatus)
            ms.con.commit()
            messagebox.showinfo('Success', "Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    print(bid)
    print(issueto)

    allBid.clear()