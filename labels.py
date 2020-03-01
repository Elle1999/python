from tkinter import *

main = Tk()
main.title("Elle tkinter")
main.geometry('300x300')
main.config(bg = '#00ffff')

firstname = Label(main, text="Elle")
lastname = Label(main, text="Jen")
date = Label(main, text="2/29/2020")

firstname.pack(side = LEFT)
lastname.pack(side = RIGHT)
date.pack(side = TOP)

main.mainloop()
