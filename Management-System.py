

import tkinter as tk
from tkinter import Entry
import Management_Class

root = tk.Tk()

root.title("Management System")

appLabel = tk.Label(root, text="Management System")
# appLabel.config(font=(30))
appLabel.pack()

nameLabel = tk.Label(root, text="Enter your name")
nameLabel.pack()

nameEntry = Entry(root)
nameEntry.pack()

addressLabel = tk.Label(root, text="Enter your address")
addressLabel.pack()

addressEntry = Entry(root)
addressEntry.pack()

phoneLabel = tk.Label(root, text="Enter your phone")
phoneLabel.pack()

phoneEntry = Entry(root)
phoneEntry.pack()

def save_details():
    name = nameEntry.get()
    address = addressEntry.get()
    phone = phoneEntry.get()
    obj = Management_Class.Management(name, address, phone)
    obj.display_data()
    obj.save_details()


button = tk.Button(root, text="Save Details", command=lambda : save_details())
button.pack()

root.mainloop()











































