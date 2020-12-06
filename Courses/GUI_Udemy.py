from tkinter import *
from tkinter import messagebox
window = Tk()


# dictionary of users
users = {"User1": "pass1",
         "User2": "pass2",
         "User3": "pass3",
         "User4": "pass4",
         "User5": "pass5"}


def log_in():
    user = UserEntry.get()
    password = PassEntry.get()
    verif = 0
    for k, v in users.items():
        if k == user and v == password:
            verif = 1
            break
    if verif == 1:
        messagebox.showinfo("Access", "Your granted access!")
    else:
        messagebox.showerror("Error", "Wrong username or password, try again")
        UserEntry.delete(0, END)
        PassEntry.delete(0, END)
        # (UserEntry and UserPass).delete()


UserLabel = Label(window, text="Enter username: ")
UserLabel.pack(anchor=W)
UserEntry = Entry(window)
UserEntry.pack(anchor=W)

UserPass = Label(window, text="Enter password: ")
UserPass.pack(anchor=W)
PassEntry = Entry(window)
PassEntry.pack(anchor=W)

button = Button(window, text="Log in", command=log_in)
button.pack()

window.mainloop()