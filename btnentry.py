from tkinter import *
from tkinter import messagebox

def btnClick() :
    msg = entry2.get()
    messagebox.showinfo('Error', msg)
    entry.insert(0, msg)

main = Tk()
main.title("Elle tkinter")
main.geometry('300x300')
main.config(bg = '#00ffff')

firstname = Label(main, text="Elle")
lastname = Label(main, text="Jen")
date = Label(main, text="2/29/2020")

firstname.config(fg = 'blue', font = 'Helvetica 10 bold italic')
lastname.config(fg = 'green', font = 'Times 24 bold italic')
date.config(fg = 'pink', font = 'Roboto 10 bold italic')

firstname.pack(side = LEFT)
lastname.pack(side = RIGHT)
date.pack(side = TOP)

entry = Entry(main, width = 20)
entry2 = Entry(main, width = 20)
entry2.pack(side = TOP)
entry.pack(side = TOP)

btn = Button(main, text='Click Me', command = btnClick)
btn.pack(side = BOTTOM)

main.mainloop()
