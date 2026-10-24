from tkinter import *

wn=Tk()
wn.title("My profile card")
wn.geometry("400x380")

title=Label(wn, text="Adithya's Profile card", fg="white", bg="purple", width="52")
title.grid(column=0, row=0, padx=10, pady=10)

name=Label(wn, text="Name: ", fg="black", bg="white")
name.grid(column=0, row=1, padx=10, pady=5)

name_entry=Entry(wn, fg="black", bg="lightyellow", width=25)
name_entry.grid(column=1, row=1, columnspan=3, padx=10, pady=5)


hobby=Label(wn, text="Hobby: ", fg="black", bg="white")
hobby.grid(column=0, row=2, padx=10, pady=5)

hobby_entry=Entry(wn, fg="black", bg="lightyellow", width=25)
hobby_entry.grid(column=1, row=2, columnspan=3, padx=10, pady=5)

wn.mainloop()


