from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("560x560")
window.title("error handling")


def authentication():
    user_pass = {"cam": "123", "eth": "456", "sam": "789", "vic": "135", "zoe": "246"}
    username = entry2.get()
    password = entry3.get()
    if (username, password) in user_pass.items():
        messagebox.showinfo("processing", "successful")
        window.withdraw()
        import login
        login.status

    else:
        messagebox.showinfo("processing", "invalid")

label_1 = Label(window, text="Enter login details", width=20, font=10)

label_2 = Label(window, text="username", width=20, font=10)
entry2 = Entry(window, width=20, textvariable="username")

label_3 = Label(window, text="password", width=20, font=10)
entry3 = Entry(window, width=20, show="$")

btn = Button(window, text="Login", width=20, fg="black", bg="white", command=authentication)

label_1.place(x=170, y=10)
label_2.place(x=170, y=100)
label_3.place(x=170, y=200)
entry2.place(x=180, y=130)
entry3.place(x=180, y=230)
btn.place(x=170, y=330)
window.mainloop()