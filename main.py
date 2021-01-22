

from tkinter import *
from tkinter import messagebox,Toplevel
import pyqrcode
import png
import os
import time

#Scan Module list Here

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import winsound

#Tkinter start
root = Tk()
root.geometry('580x460')
root.maxsize(580,460)
root.minsize(580,460)
font = ('times', 12, 'italic bold')
root.title('QR_Generator')
root.configure(bg='grey')
root.wm_iconbitmap('qr1.ico')


# function work
def S_scan():
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_DUPLEX
    with open('record.txt') as f:
        myDataList = f.read().splitlines()

    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime(" %m/%d/%Y, %H:%M:%S ", named_tuple)
    print(time_string)
    while True:
        # time.sleep(1)
        _, frame = cap.read()
        decodeObj = pyzbar.decode(frame)
        for obj in decodeObj:
            print(" ", obj.data)
            myData = obj.data.decode('utf-8')

            if myData in myDataList:
                pts = np.array([obj.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(frame, [pts], True, (255, 0, 255), 3)
                pts2 = obj.rect
                cv2.putText(frame, str('Entry'), (pts2[0], pts2[1]), font, 0.9,
                            (255, 0, 0), 2)
                cv2.putText(frame, str('Welcome Our world'), (150, 350), font, 0.9,
                            (255, 0, 0), 2)
            else:
                pts = np.array([obj.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(frame, [pts], True, (255, 0, 255), 3)
                pts2 = obj.rect
                cv2.putText(frame, str('No entry'), (pts2[0], pts2[1]), font, 0.6,
                            (0, 0, 255), 2)

                cv2.putText(frame, str('Sorry,Unknown Person'), (50, 350), font, 0.9,
                            (0, 0, 255), 2)
                winsound.Beep(500, 400)

        cv2.imshow("security scanner", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

def Make_Qr():
    Qr_Name = Qr_Name_Entry.get()
    Qr_Id = Qr_Id_Entry.get()
    Qr_Message = Qr_Message_Entry.get()
    Data = 'Name: ' + Qr_Name + ' Id: ' + Qr_Id + '  Message: ' + 'Qr_Message'
    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime(" %m/%d/%Y, %H:%M:%S ", named_tuple)

    print(time_string)

    # write our data in txt file also save date and time
    with open('record.txt', 'a') as f:
        f.write(
            f'{Data}'  +  f' Data entry time: {time_string}'+'\n')
    # Empty data Qr code
    if Data==' ':
            res=messagebox.askyesno('Notification','Are you create empty QR?')
            if (res==True):
                    Qr_code = pyqrcode.create(Data)
                    path=r'C:\Users\Lenovo\Desktop\qrfile' #Desktop file must creat it in your deasktop
                    save_path='{}\{}{}.png'.format(path,Qr_Id,Qr_Name)
                    list_dir=os.listdir(path)
                    if('{}{}.png'.format(Qr_Id,Qr_Name) in list_dir):
                            messagebox.showinfo('Notification','Sorry,This Name and Id are repeat!')

                    else:
                        Qr_code.png(save_path, scale=8)  # if you change qr color use color module(rgb)
                        notification_ms = 'Save as: ' + Qr_Id + Qr_Name + '.png'
                        Qr_Notification_Message_label.configure(text=notification_ms)
                        result = messagebox.askyesno('Notification', 'Qr File is generate now click Yes Button')
                        if (result == True):
                            top = Toplevel()
                            top.geometry('400x400')
                            top.configure(bg='white')
                            top.wm_iconbitmap('qr2.ico')
                            img = PhotoImage(file=save_path)
                            lebel = Label(top, image=img, bg='white')
                            lebel.place(x=10, y=10)
                            top.mainloop()
            else:
                pass
    # Qr_data file start
    else:
               Qr_code = pyqrcode.create(Data)
               path = r'C:\Users\Lenovo\Desktop\qrfile'
               save_path = '{}\{}{}.png'.format(path, Qr_Id, Qr_Name)
               list_dir = os.listdir(path)
               if ('{}{}.png'.format(Qr_Id, Qr_Name) in list_dir):
                   messagebox.showinfo('Notification', 'Sorry,This Name and Id are repeat!')

               else:
                  Qr_code.png(save_path, scale=8) #if you change qr color use color module(rgb)
                  notification_ms='Save as: '+Qr_Id+Qr_Name+ '.png'
                  Qr_Notification_Message_label.configure(text=notification_ms)
                  result = messagebox.askyesno('Notification','Qr File is generate now click Yes Button')
                  if(result==True):
                      top = Toplevel()
                      top.geometry('400x400')
                      top.configure(bg='white')
                      top.wm_iconbitmap('qr2.ico')
                      img=PhotoImage(file=save_path)
                      lebel = Label(top, image=img,bg='white')
                      lebel.place(x=10,y=10)
                      top.mainloop()

def Clear():
    cl = messagebox.askokcancel('Notification', 'Are you want to Clear?')
    if (cl == True):
        Qr_Id_Entry.delete(0, 'end')
        Qr_Name_Entry.delete(0, 'end')
        Qr_Message_Entry.delete(0, 'end')
        Qr_Notification_Message_label.config(text='')
    else:
        pass

def Quit_root():
    res = messagebox.askokcancel('Notification', 'Are you want to Exit Qr_Generator?')
    if (res == True):
        root.destroy()
    else:
        pass

# Label area
Qr_Id_label = Label(root, text="Enter Your Id:", bg="powder blue", fg='black', width=15, height=2,
                    font=('times', 12, 'italic bold'))
Qr_Id_label.place(x=10, y=20)

Qr_Name_label = Label(root, text="Enter Your Name:", bg="powder blue", fg='black', width=15, height=2,
                      font=('times', 12, 'italic bold'))
Qr_Name_label.place(x=10, y=80)

Qr_Message_label = Label(root, text="Enter Qr Message:", bg="powder blue", fg='black', width=15, height=2,
                         font=('times', 12, 'italic bold'))
Qr_Message_label.place(x=10, y=140)

Qr_Notification_label = Label(root, text="Notification:", bg="powder blue", fg='black', width=10, height=2,
                              font=('times', 15, 'bold underline'))
Qr_Notification_label.place(x=10, y=400)

Qr_Notification_Message_label = Label(root, text="", bg="powder blue", fg='black', width=30, height=2,
                                      font=('times', 15, 'bold'))
Qr_Notification_Message_label.place(x=200, y=400)

# Entry box area start

Qr_Id_Entry = Entry(root, width=30, bg='Beige',relief=SOLID, bd=1, font=('Arial', 15, 'bold'))
Qr_Id_Entry.place(x=230, y=20)

Qr_Name_Entry = Entry(root, width=30, bg='Beige',relief=SOLID, bd=1, font=('Arial', 15, ' bold'))
Qr_Name_Entry.place(x=230, y=80)

Qr_Message_Entry = Entry(root, width=30, bg='Beige',relief=SOLID, bd=1, font=('Arial', 15, ' bold'))
Qr_Message_Entry.place(x=230, y=140)

# Buttons area
Make_Qr_image = Button(root, text='Generate', width=15, command=Make_Qr, font=('times', 11, 'bold'), bd=10,
                       bg='tan')
Make_Qr_image.place(x=10, y=250)

Clear_Button = Button(root, text='Clear', width=15, command=Clear, font=('times', 11, 'bold'), bd=10,
                      bg='tan')
Clear_Button.place(x=210, y=250)

Quit_Button = Button(root, text='Exit', width=15, command=Quit_root, font=('times', 11, 'bold'), bd=10,
                     bg='tan')
Quit_Button.place(x=410, y=250)


S_Scan_Button = Button(root, text='S_scan', command=S_scan, width=15,font=('times', 11, 'bold'), bd=10,
                     bg='olive')
S_Scan_Button.place(x=210, y=320)




# Buttons hover Effect && Functions but this area  is not  working my project it's optional
def Make_Qr_imageEnter(e):
    Make_Qr_image["bg"] = 'purple2'

def Make_Qr_imageLeave(e):
    Make_Qr_image['bg'] = 'powder blue'

def Clear_ButtonEnter(e):
    Clear_Button['bg'] = 'purple2'

def Clear_ButtonLeave(e):
    Clear_Button['bg'] = 'powder blue'

def Quit_ButtonEnter(e):
    Quit_Button['bg'] = 'purple2'

def Quit_ButtonLeave(e):
    Quit_Button['bg'] = 'powder blue'


Make_Qr_image.bind = ('<Enter>', Make_Qr_imageEnter)
Make_Qr_image.bind = ('<Leave>', Make_Qr_imageLeave)

Clear_Button.bind = ('< Enter >', Clear_ButtonEnter)
Clear_Button.bind = ('< Leave >', Clear_ButtonLeave)

Quit_Button.bind = ('< Enter >', Quit_ButtonEnter)
Quit_Button.bind = ('< Leave >', Quit_ButtonLeave)

root.mainloop()



