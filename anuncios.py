import imp
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import tkinter as tk
from sympy import root
import psycopg2
from hashlib import sha256
from collections import Counter
import datetime
 
class Register:
    def __init__(self,root):
        self.root = root
        self.root.title ("Register")
        self.root.geometry('400x550+600+70')
	
        self.left=ImageTk.PhotoImage(file = "fotos/anuncio.jpeg")
        left= Label(self.root,image =self.left).pack()

        btn_login =Button(self.root, text= 'Skip',command= self.register_ventana,activebackground='green', bg='#2A2A46', cursor="hand2",font=('Times new roman', 12,'bold'),fg="black").place(x=100,y=500,width=220, height=30)

    def register_ventana (self):
        self.root.destroy()
        import profiles
             
root=Tk()
obj = Register(root)
root.mainloop()