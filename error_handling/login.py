import tkinter
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("560x215")
window.title("login")

amount_label = Label(window, text="Enter current amount", width=20, font=10)
amount_entry = Entry(window)
def malaysia():
    amount = int(amount_entry.get())
    try:
        if amount < 3000:
            raise ValueError(messagebox.showinfo("message","insufficient funds. Deposit more money"))
    except ValueError as error:
        print(error)
        amount_entry.delete(0, END)

    else:
        messagebox.showinfo("message", "you are eligible for a trip to Malaysia")
        amount_entry.delete(0, END)
    finally:
        print("successful transaction")


def exit():
    window.destroy()

exitbtn = Button(window, text="Exit", command=exit, bg="white")
checkbutton = Button(window, text="qualification check", command=malaysia, bg="white")



checkbutton.place(x=205, y=100)
exitbtn.place(x=270, y=150)
amount_label.place(x=170, y=10)
amount_entry.place(x=190, y=50)
window.mainloop()