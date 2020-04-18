from tkinter import *

root = Tk()

label1 = Label(root, text="Enter Email:").grid(row=0, column=0)
input_field1 = Entry(root, width=50)
input_field1.grid(row=0, column=1)


def click():
    email = input_field1.get()
    if email.find("@") == -1:
        error = Label(root, text="Insert a valid email!").grid(row=2, column=1)
    else:
        username = email.split("@", 1)[0]
        domain_name = email.split("@", 1)[1]
        username_label = Label(root, text="Username: " + username).grid(row=2, column=0)
        domain_name_label = Label(root, text="Domain Name: " + domain_name).grid(row=2, column=1)


button = Button(root, text="Enter", command=click).grid(row=1, column=1)

root.mainloop()
