from tkinter import *
from tkinter import messagebox
from mysql_connector import connect_db

def issue_book():
    con = connect_db()
    if con is None:
        return
    cur = con.cursor()
    issueTable = "books_issued"
    bookTable = "books"
    bid = bookInfo1.get()
    sid = bookInfo2.get()

    issueSql = "INSERT INTO " + issueTable + " (bid, issuedto) VALUES (%s, %s)"
    updateSql = "UPDATE " + bookTable + " SET status = 'issued' WHERE bid = %s"

    try:
        cur.execute("SELECT * FROM books WHERE bid = %s AND status = 'issued'", (bid,))
        if cur.fetchone() is not None:
            messagebox.showinfo('Error', "Book is already issued")
        else:
            cur.execute(issueSql, (bid, sid))
            cur.execute(updateSql, (bid,))
            con.commit()
            messagebox.showinfo('Success', "Book Issued Successfully")
    except ms.Error as err:
        messagebox.showinfo('Error', f"Error: {err}")
    finally:
        cur.close()
        con.close()
        root.destroy()

def issue():
    global bookInfo1, bookInfo2, root
    root = Tk()
    root.title("Issue Book")
    root.geometry("1020x735")

    # Create canvas and layout
    Canvas1 = Canvas(root, bg="magenta")
    Canvas1.pack(expand=True, fill="both")

    headingFrame1 = Frame(root, bg="Yellow", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Issue Books", bg='black', fg='white', font=('Courier New', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    lb1 = Label(labelFrame, text='Book ID:', bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame, text='Student ID:', bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="ISSUE", bg='black', fg='white', font=('Courier New', 11), command=issue_book)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="QUIT", bg='black', fg='white', font=('Courier New', 11), command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
