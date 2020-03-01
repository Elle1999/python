from tkinter import *
from tkinter import messagebox

main = Tk()
main.title("Elle tkinter")
main.geometry('300x300')
main.config(bg = '#00ffff')

lblFirst = Label(main, text = 'First Name:')
lblFirst.grid(row = 0, column = 0, padx = 20, pady = 10)

entFirst = Entry(main, width = 20)
entFirst.grid(row = 0, column = 1)

lblLast = Label(main, text='Last Name:')
lblLast.grid(row = 1, column = 0, padx = 20, pady = 10)

entLast = Entry(main, width = 20)
entLast.grid(row = 1, column = 1)

lblAddress = Label(main, text = 'Address:')
lblAddress.grid(row = 2, column = 0, padx = 20, pady = 10)

entAddress = Entry(main, width = 20)
entAddress.grid(row = 2, column = 1)


main.mainloop()
