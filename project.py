import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("Info collector")
#root.configure(bg='#F5DEB3')
root.iconphoto(False, tk.PhotoImage(file="C:\man icon - Copy.png"))
  

connection = sqlite3.connect('account.db')
#assigning strings to variables
TABLE_NAME = "account_table"
EMPLOYEE_ID = "employee_id"
EMPLOYEE_NAME = "employee_name"
EMPLOYEE_DEPARTMENT = "employee_department"
EMPLOYEE_ADDRESS = "employee_address"
EMPLOYEE_PHONE = "employee_phone"


connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + EMPLOYEE_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   EMPLOYEE_NAME + " TEXT, " + EMPLOYEE_DEPARTMENT + " TEXT, " +
                   EMPLOYEE_ADDRESS + " TEXT, " + EMPLOYEE_PHONE + " INTEGER);")

# heading craetion and styling
appLabel = tk.Label(root, text="Employee Management System", bg="#C19A6B",fg="#36454F",width=45)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(5, 0))

#creating objects with class
class Employee:
    employeeName = ""
    departmentName = ""
    phoneNumber = 0
    address = ""

#define the initialization declaration function which puts the attribute in a condition to an opeartiion
    def __init__(self, employeeName, departmentName, phoneNumber, address):
        self.employeeName = employeeName
        self.departmentName = departmentName
        self.phoneNumber = phoneNumber
        self.address = address

        
#define function of multiple commands on-click of a button
def fun1():
   nameEntry.delete(0, tk.END)
def fun2 ():
   tk.messagebox.showinfo("clear message", "Name cleared successfully")

#same   
def delete1():
   departmentEntry.delete(0, tk.END)
def delete11 ():
   tk.messagebox.showinfo("clear message", "Department cleared successfully")

def delete2():
   phoneEntry.delete(0, tk.END)
def delete22 ():
   tk.messagebox.showinfo("clear message", "Phone number cleared successfully")


def delete3():
   addressEntry.delete(0, tk.END)
def delete33 ():
   tk.messagebox.showinfo("clear message", "Address cleared successfully")





  
#create and style entry box label   
nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))
button1 = tk.Button(root, bg = '#C19A6B', text = "CLEAR NAME", command=lambda: [fun1(), fun2()] , width=20,height=1, font=('sylfaen', 12)).place(x=570,y=115)



departmentLabel = tk.Label(root, text="Enter your department", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))
button2 = tk.Button(root, bg = '#C19A6B', text = "CLEAR DEPARTMENT", command=lambda: [delete1(), delete11()], width=20, font=('sylfaen', 12)).place(x=570,y=172)


phoneLabel = tk.Label(root, text="Enter your phone number", width=40, anchor='w',
                      font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))
button3 = tk.Button(root, bg = '#C19A6B', text = "CLEAR PHONE NUMBER", command=lambda: [delete2(), delete22()] , width=20, font=('sylfaen', 12)).place(x=570,y=230)


addressLabel = tk.Label(root, text="Enter your address", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))
button4 = tk.Button(root,  bg = '#C19A6B', text = "CLEAR ADDRESS", command=lambda: [delete3(), delete33()], width=20, font=('sylfaen', 12)).place(x=570,y=290)

#creating and styling entrybox
nameEntry = tk.Entry(root, width = 70 )
departmentEntry = tk.Entry(root, width = 70) 
phoneEntry = tk.Entry(root, width = 70)
addressEntry = tk.Entry(root, width = 70)

#Entry box positioning
nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
departmentEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
phoneEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
addressEntry.grid(row=4, column=1, padx=(0,10), pady = 20)

#defining function "takeNameInput" to receive information from the entrybox and input them into database and removing them for entry box at the same time
def takeNameInput():
    global nameEntry, departmentEntry, phoneEntry, addressEntry
    # global username, departmentName, phone, address
    global list
    global TABLE_NAME, EMPLOYEE_NAME, EMPLOYEE_DEPARTMENT, EMPLOYEE_ADDRESS, EMPLOYEE_PHONE
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    departmentName = departmentEntry.get()
    departmentEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + EMPLOYEE_NAME + ", " +
                       EMPLOYEE_DEPARTMENT + ", " + EMPLOYEE_ADDRESS + ", " +
                       EMPLOYEE_PHONE + " ) VALUES ( '"
                       + username + "', '" + departmentName + "', '" +
                       address + "', " + str(phone) + " ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")

#defining function "destroyRootWindow" to create second window , display database and close the root window 
def destroyRootWindow():
    root.destroy()
    secondWindow = tk.Tk()

    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Employee Management System",
                         bg="#C19A6B",fg="#36454F", width=50)
    appLabel.config(font=("Syl", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")

    tree.heading("one", text="Employee Name")
    tree.heading("two", text="Department Name")
    tree.heading("three", text="Address")
    tree.heading("four", text="Phone Number")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Employee " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()


# def printDetails():
#     for singleItem in list:
#         print("Employee name is: %s\nDepartment name is: %s\nPhone number is: %d\nAddress is: %s" %
#               (singleItem.employee, singleItem.departmentName, singleItem.phoneNumber, singleItem.address))
#         print("****************************************")

button = tk.Button(root, bg = '#C19A6B' ,text="Take input", command=lambda :takeNameInput())
button.grid(row=5, column=0, pady=30)

displayButton = tk.Button(root, bg = '#C19A6B', text="Display result", command=lambda :destroyRootWindow())
displayButton.grid(row=5, column=1)

root.mainloop()
