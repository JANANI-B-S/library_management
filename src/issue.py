import mysql_connector as ms
from PIL import ImageTk,Image
from tkinter import messagebox


issueTable = "books_issued"
bookTable="books"
allBid = []

def issue():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status
    cur = ms.con.cursor(buffered=True)
    bid = inf1.get()
    issueto = inf2.get()

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