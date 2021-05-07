# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:41:18 2021

@author: Hunter Stiles
"""

import tkinter as tk
from tkinter import ttk
from twilio.rest import Client
import sqlite3
import pandas as pd
import logging
import os


try:
    logLevel = os.environ['MESSAGE_LOG_LEVEL']
except:
    logLevel = logging.DEBUG
  
logging.basicConfig(format='%(asctime)s %(message)s',  datefmt='%I:%M:%S %p')
logging.getLogger().setLevel(logLevel)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
filehandler = logging.FileHandler(r'messagelog.txt')
filehandler.setFormatter(formatter)
logging.getLogger().addHandler(filehandler)


logging.warning('messaging application started.')
con = sqlite3.connect('directory.db')
cur = con.cursor()

try:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
except:
    logging.warning("Unable to get twilio account_sid from environment")
    account_sid = 'a valid twilio sid'

try:
    account_sid = os.environ['TWILIO_ACCOUNT_TOKEN']
except:
    logging.warning("Unable to get twilio auth_token from environment")
    auth_token = 'a valid twilio token'



client = Client(account_sid, auth_token)

# checkNumber checks to see if the number is numeric digits and has
# a length of 10.  If so it returns True, if not it pops up an error box and
# returns False.
def checkNumber(telephoneNumber):
    if telephoneNumber.isnumeric() and len(telephoneNumber) == 10:
        return True
   
    tk.messagebox.showerror("Invalid Phone number", "Number must be 10 digits")
    logging.info("Invalid phone number entered " + telephoneNumber)
    return False
    
# below are the callback functions for the numbered buttons
# each one simply appends the number to the number in the phone display
def button1():
    logging.debug("pressed 1")
    display_number.insert('end', '1')
def button2():
    logging.debug("pressed 2")
    display_number.insert('end', '2')
def button3():
    logging.debug("pressed 3")
    display_number.insert('end', '3')
def button4():
    logging.debug("pressed 4")
    display_number.insert('end', '4')
def button5():
    logging.debug("pressed 5")
    display_number.insert('end', '5')
def button6():
    logging.debug("pressed 6")
    display_number.insert('end', '6')
def button7():
    logging.debug("pressed 7")
    display_number.insert('end', '7')
def button8():
    logging.debug("pressed 8")
    display_number.insert('end', '8')
def button9():
    logging.debug("pressed 9")
    display_number.insert('end', '9')
def button0():
    logging.debug("pressed 0")
    display_number.insert('end', '0')
    
    
def button_dir():
    def button_Submit():
        logging.debug("pressed Submit button in directory window")
        logging.debug("selected " + dirCombBox.get())
        ind=df.index[(df['name'] == dirCombBox.get())].tolist()
        display_number.delete(0, "end")
        display_number.insert(0, df.at[ind[0], 'number'])
        windowDirectory.destroy()
    logging.debug("pressed directoy button")
    windowDirectory = tk.Toplevel(root)
    windowDirectory.geometry("250x250")
    windowDirectory.title("Directory")
    instructionLabel = tk.Label(windowDirectory, text="select entry from directory")
    instructionLabel.pack()
    
    df = pd.read_sql_query("SELECT name, number FROM PhoneNumbers ORDER BY name", con)
    logging.debug(df)
    dirCombBox = ttk.Combobox(windowDirectory, values=df['name'].tolist())
    dirCombBox.pack()
  
 
    frameA = tk.Frame(windowDirectory)
    frameA.pack(side="bottom")
    Button_sendText = tk.Button(frameA, text="Submit", command=button_Submit)
    Button_sendText.grid(row = 1, column = 1)
    Button_cancel = tk.Button(frameA, text="Cancel", command=windowDirectory.destroy)
    Button_cancel.grid(row = 1, column = 3)

def button_ad():
    logging.debug("pressed add/delete")
    def button_Add():
        logging.debug("pressed Add button in add/delete window")
        name=nameEntry.get()
        number=numberEntry.get()
        if len(name)==0:
            tk.messagebox.showerror("Invalid name", "You must enter a name")
            return
        if checkNumber(number):
            cur.execute('INSERT INTO  PhoneNumbers VALUES (?,?)', (name, number))
            con.commit()
            logging.info("added " + name + "to the directory")
            tk.messagebox.showinfo("Added", "Added " + name + " to contacts")
            windowAD.destroy()
            
            
                
    def button_Delete():
        logging.debug("pressed Delete button in add/delete window")
        name = dirCombBox.get();
        tk.messagebox.showinfo("Deleted", "Deleted " + name + " from contacts")
        cur.execute('DELETE FROM PhoneNumbers WHERE name=?', (name,))
        con.commit()
        logging.info("deleted " + name + "from the directory")
        tk.messagebox.showinfo("Deleted", "Deleted " + name + " from contacts")
        windowAD.destroy()
    logging.debug("pressed directoy button")
    windowAD = tk.Toplevel(root)
    windowAD.geometry("250x300")
    windowAD.title("Add/Delete")
    instructionLabel = tk.Label(windowAD, text="select entry to delete")
    instructionLabel.pack()
    
    df = pd.read_sql_query("SELECT name, number FROM PhoneNumbers ORDER BY name", con)
    logging.debug(df)
    dirCombBox = ttk.Combobox(windowAD, values=df['name'].tolist())
    dirCombBox.pack()
  
 
    frameA = tk.Frame(windowAD)
    frameA.pack()
    Button_Delete = tk.Button(frameA, text="Delete", command=button_Delete)
    Button_Delete.grid(row = 1, column = 1)
    Button_cancel = tk.Button(frameA, text="Cancel", command=windowAD.destroy)
    Button_cancel.grid(row = 1, column = 3)
    frameB = tk.Frame(windowAD)
    frameB.pack(side="bottom")
    instructionLabel1 = tk.Label(frameB, text="Enter name and number to add")
    instructionLabel1.pack()
    nameLabel = tk.Label(frameB, text="Name")
    nameLabel.pack()
    nameEntry= tk.Entry(frameB, width = 30)
    nameEntry.pack()
    numberLabel = tk.Label(frameB, text="Number")
    numberLabel.pack()
    numberEntry= tk.Entry(frameB, width = 30)
    numberEntry.pack()
    frameC = tk.Frame(frameB)
    frameC.pack(side="bottom")
    Button_Add = tk.Button(frameC, text="Add", command=button_Add)
    Button_Add.grid(row = 1, column = 1)
    Button_cancel1 = tk.Button(frameC, text="Cancel", command=windowAD.destroy)
    Button_cancel1.grid(row = 1, column = 3)
    
    


def button_send():
    def button_sendText():
        logging.debug("pressed Send Text in send popup window")
        phoneNum = display_number1.get()
        if (checkNumber(phoneNum)):
            logging.debug("sending text to " + phoneNum  )
            message = client.messages \
                .create(
                    body=display_MSG.get("1.0","end"),
                    to=phoneNum,
                    from_='+19082244077'
                    )
            logging.info("sent the following text to " + phoneNum)
            logging.info(display_MSG.get("1.0","end"))
             
    def button_sendVoice():
        logging.debug("pressed Send Voice in send popup window")
        phoneNum = display_number1.get()
        if (checkNumber(phoneNum)):
            logging.debug("sending voice message to " + phoneNum  )
            call = client.calls.create(
                twiml='<Response><Say>' + display_MSG.get("1.0","end") + '</Say></Response>',
                to=phoneNum,
                from_='+19082244077'
            )
        logging.info("sent the following text to " + phoneNum)
        logging.info(display_MSG.get("1.0","end"))

        
    logging.debug("pressed send message")
    logging.debug(display_number.get())
    
    windowSendMsg = tk.Toplevel(root)
    windowSendMsg.geometry("250x250")
    windowSendMsg.title("Send")
    display_number1 = tk.Entry(windowSendMsg, width = 30)
    display_number1.insert("end", display_number.get())
    display_number1.pack()
  
    scrollbar = tk.Scrollbar(windowSendMsg)
    display_MSG = tk.Text(windowSendMsg, width = 30, height = 10, yscrollcommand=scrollbar.set, wrap='word')
    scrollbar.config(command=display_MSG.yview)
    scrollbar.pack(side="right")
    display_MSG.pack(side="top")
    frameA = tk.Frame(windowSendMsg)
    frameA.pack()
    Button_sendText = tk.Button(frameA, text="Send Text", command=button_sendText)
    Button_sendText.grid(row = 1, column = 1)
    Button_cancel = tk.Button(frameA, text="Cancel", command=windowSendMsg.destroy)
    Button_cancel.grid(row = 1, column = 2)
    Button_sendVoice = tk.Button(frameA, text="Send Voice", command=button_sendVoice)
    Button_sendVoice.grid(row = 1, column = 3)


    
 
root = tk.Tk()
root.title("Phone")
root.geometry("250x300")
 
frame1 = tk.Frame(root)
frame1.pack()
display_number = tk.Entry(frame1, width = 30)
display_number.pack()

frame2 = tk.Frame(root)
frame2.pack()
button1 = tk.Button(frame2, text = "1", height = 3, width = 6, command = button1)
button1.grid(row = 1, column = 1)
button2 = tk.Button(frame2, text = "2", height = 3, width = 6,  command = button2)
button2.grid(row = 1, column = 2)
button3 = tk.Button(frame2, text = "3", height = 3, width = 6,  command = button3)
button3.grid(row = 1, column = 3)
button4 = tk.Button(frame2, text = "4", height = 3, width = 6, command = button4)
button4.grid(row = 2, column = 1)
button5 = tk.Button(frame2, text = "5", height = 3, width = 6,  command = button5)
button5.grid(row = 2, column = 2)
button6 = tk.Button(frame2, text = "6", height = 3, width = 6,  command = button6)
button6.grid(row = 2, column = 3)
button7 =tk. Button(frame2, text = "7", height = 3, width = 6, command = button7)
button7.grid(row = 3, column = 1)
button8 = tk.Button(frame2, text = "8", height = 3, width = 6,  command = button8)
button8.grid(row = 3, column = 2)
button9 = tk.Button(frame2, text = "9", height = 3, width = 6,  command = button9)
button9.grid(row = 3, column = 3)
button0 = tk.Button(frame2, text = "0", height = 3, width = 6  , command = button0)
button0.grid(row = 4, column = 2)

frame3 = tk.Frame(root)
frame3.pack()
buttonDir = tk.Button(frame3, text = "Contacts", height = 3, width = 10, command = button_dir)
buttonDir.pack(side="left")
buttonConnect = tk.Button(frame3, text = "Add\nDelete", height = 3, width = 10, command = button_ad)
buttonConnect.pack(side="left")
buttonSend = tk.Button(frame3, text = "Send\nMessage", height = 3, width = 10, command = button_send)
buttonSend.pack(side="right")

root.mainloop()