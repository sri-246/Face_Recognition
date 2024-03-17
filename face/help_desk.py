from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Help:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK", font=("rockwell extra bold",35,"underline"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\91875\Pictures\Face Project\helper.jpg")
        img_top=img_top.resize((1530,720),Image.BICUBIC)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_label=Label(f_lbl,text="Email:sriviba2004@gmail.com",font=("rockwell",20,"bold"), bg="white",fg="red")
        dev_label.place(x=550,y=300)



if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()