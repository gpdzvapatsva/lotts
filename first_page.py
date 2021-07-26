# Abdullah isaacs class 2
# import modules section
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta, date
from PIL import ImageTk,Image
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#create window

root = tk.Tk()
root.title("Weather")
root.geometry("800x400")
root.configure(bg="black")

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# create object for log in page
class Logging:
    def __init__(self, master):
        #image
        self.pic = Canvas(master, width=800, height=400, bg="black")
        self.pic.place(x=0, y=0)
        self.img = ImageTk.PhotoImage(Image.open('pngegg.png'))
        self.pic.create_image(0, 20, anchor=NW, image=self.img)
        #create labels and entries
        self.first_name = Label(master, text="First Name", bg="black", fg="gold", font="Times 20 bold italic")
        self.first_name.place(x=50, y=20)
        self.address=Label(master,text="Physical address", bg="black", fg="gold", font="Times 20 bold italic")
        self.address.place(x=450,y=20)
        self.ad_ent=Entry(master,textvariable="add",bg="red",width=35)
        self.ad_ent.place(x=450,y=80)
        self.first_entry = Entry(master, textvariable="fname", bg="red", width=15)
        self.first_entry.place(x=230, y=20)
        self.email = Label(master, text="Email address", bg="black", fg="gold", font="Times 20 bold italic")
        self.email.place(x=50, y=80)
        self.email_ent = Entry(master, textvariable="age", bg="red", width=37)
        self.email_ent.place(x=50, y=120)
        self.id_no = Label(master, text="ID number", bg="black", fg="gold", font="Times 20 bold italic")
        self.id_no.place(x=50, y=160)
        self.id_ent = Entry(master, textvariable="id", bg="red", width=13)
        self.id_ent.place(x=230, y=170)
        def qualify():
            # function to convert first 6 digits of ID number to a birthdate to establish wheether or not the player is old enough to play
            year = int(self.id_ent.get()[0:2])
            month = int(self.id_ent.get()[2:4])
            day = int(self.id_ent.get()[4:6])
            dob = date(int(year), int(month), int(day))
            age= str((date.today() - dob) // timedelta(days=365.2425))[2:4]
            def calc():
                if int(age) < 18:
                    messagebox.showerror("Error","You must be over 18 to play")
                elif len(self.id_ent.get()) < 13:
                    messagebox.showerror("Error","please enter a valid ID number")
                elif len(self.id_ent.get()) > 13:
                    messagebox.showerror("Error","Please enter a valid ID  number")
                else:
                    return 100
            def email_checker():
                # using regex to validate the email address, checking if the correct symbol was included
                if (re.search(regex, self.email_ent.get())):
                    return 100
                else:
                    messagebox.showerror("Error","Invalid Email")
            if calc() == 100 and email_checker() == 100:
                messagebox.showinfo("CONGRATULATIONS","LETS PLAY!!!")
                text_file = open("PlayerID.txt",'+a')
                text_file.write("User: " + self.first_entry.get() + "\nmail: " + self.email_ent.get() + "\nID: " + self.id_ent.get() + "\nAdress: "
                                + self.ad_ent.get())
                text_file.close()
                root.destroy()
                import main

# def clear():
        #
        #  self.first_entry.delete(0, END)
        #  self.email_ent.delete(0, END)
        #  self.id_ent.delete((0, END)

        self.qual = Button(master, text="Check if i qualify", command=qualify, bg="gold",pady=5,padx=5, width=35,height=2)
        self.qual.place(x=450,y=150)


l = Logging(root)

root.mainloop()