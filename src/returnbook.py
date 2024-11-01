from tkinter import *
from tkinter import messagebox
from mysql_connector import connect_db

def ret_book():
    con = connect_db()
    if con is None:
        return
    cur = con.cursor()
    issueTable = "books_issued"
    bookTable = "books"
    bid = bookInfo1.get()

    deleteSql = "DELETE FROM " + issueTable + " WHERE bid = %s"
    updateSql = "UPDATE " + bookTable + " SET status = 'Available' WHERE bid = %s"

    try:
        cur.execute("SELECT * FROM books WHERE bid = %s AND status = 'Available'", (bid,))
        if cur.fetchone() is not None:
            messagebox.showinfo('Error', "Book is not issued")
        else:
            cur.execute(deleteSql, (bid,))
            cur.execute(updateSql, (bid,))
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
    except ms.Error as err:
        messagebox.showinfo('Error', f"Error: {err}")
    finally:
        cur.close()
        con.close()
        root.destroy()

def return_book():
    global bookInfo1, root
    root = Tk()
    root.title("Return Book")
    root.geometry("1020x735")

    # Create canvas and layout
    Canvas1 = Canvas(root, bg="silver")
    Canvas1.pack(expand=True, fill="both")

    headingFrame1 = Frame(root, bg="Yellow", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier New', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb1 = Label(labelFrame, text="Book ID:", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5, relwidth=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='black', fg='white', font=('Courier New', 11), command=ret_book)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="QUIT", bg='black', fg='white', font=('Courier New', 11), command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
