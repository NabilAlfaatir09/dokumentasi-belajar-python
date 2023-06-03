from tkinter import *
root = Tk()
root.geometry("500x300")

# heading
Label(root,  text="Registration Form",
      font="ar 15 bold").grid(row=0, column=3)

# field name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
email = Label(root, text="Email")

# packing fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
email.grid(row=3, column=2)

# variable untuk storing data
namevalue = StringVar
phonevalue = StringVar
emailvalue = StringVar
checkvalue = IntVar

# creating entry field
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
emailentry = Entry(root, textvariable=emailvalue)

# packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
emailentry.grid(row=3, column=3)

# creating checkbox
checkbtn = Checkbutton(text="remember me?", variable=checkvalue)
checkbtn.grid(row=4, column=3)

# submit button
Button(text="submit", command=getvals)
root.mainloop()
