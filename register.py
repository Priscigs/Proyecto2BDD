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
	
        self.left=ImageTk.PhotoImage(file = "fotos/images.png")
        left= Label(self.root,image =self.left).place(x=70, y=-160,width=300,height=500)

        self.var_fnames= StringVar()
        nombre =Label(text ="Nombre:",font=("times new roman",15,"bold"),fg="gray").place(x=20,y=200)
        txt_fname =Entry(font=("times new roman",15),textvariable=self.var_fnames).place(x=20,y=230)
       
        self.var_email = StringVar()
        email =Label(text ="Email:",font=("times new roman",15,"bold"),fg="gray").place(x=20,y=260)
        txt_email =Entry(font=("times new roman",15),textvariable=self.var_email).place(x=20,y=290)

        self.contraHash = StringVar()

        self.var_contra = StringVar(value='')
        contraseña =Label(text ="Contraseña:",font=("times new roman",15,"bold"),fg="gray").place(x=20,y=320)
        self.txt_contraseña =Entry(font=("times new roman",15),textvariable=self.var_contra)
        self.txt_contraseña.place(x=20,y=350)
        self.txt_contraseña.configure(show="*")

        # ALMACENAMIENTO DE HASH CON SHA256
        h = sha256()
        h.update(self.txt_contraseña.get().encode())
        self.contraHash.set(h.hexdigest())

        self.var_confContra = StringVar()
        conf_contraseña =Label(text ="Confirmar contraseña:",font=("times new roman",15,"bold"),fg="gray").place(x=20,y=380)
        txt_confcontraseña =Entry(font=("times new roman",15),textvariable=self.var_confContra)
        txt_confcontraseña.place(x=20,y=410)
        txt_confcontraseña.configure(show="*")

        btn_login =Button(self.root, text= 'Select Profile Type',command= self.register_ventana,activebackground='green', bg='#2A2A46', cursor="hand2",font=('Times new roman', 12,'bold'),fg="black").place(x=100,y=500,width=220, height=30)

        self.v = tk.IntVar()
        self.v.set(3)

        Label(text ="Elige un tipo de cuenta:",
              fg="white", 
              justify= tk.LEFT, 
              padx= 20).place(x=200,y=200)

        self.freemium = tk.Label(root, 
                              text="Freemium",
                              ).place(x=215,y=240)

        self.standar = tk.Label(root, 
                              text="Estándar",
                             ).place(x=215,y=270)

        self.premium = tk.Label(root, 
                              text="Premium").place(x=215,y=300)
                            #   command=self.mostrarSeleccionado,
                            #   padx = 20, 
                            #   variable=self.v, 
                            #   value=3

        self.var_type = StringVar()
        txt_type =Entry(font=("times new roman",15),textvariable=self.var_type).place(x=215,y=340)

        # self.var_userType = StringVar()
        # self.label1 = tk.Label(text ="",
        #                             fg="white", 
        #                             justify= tk.LEFT, 
        #                             padx= 20)
        # self.label1.place(x=215,y=330)

        btn_register = Button(self.root, 
                              text= 'Crear Cuenta',
                              command= self.register_data,
                              activebackground='green', 
                              bg='#2A2A46', cursor="hand2",
                              font=('Times new roman', 12,'bold'),
                              fg="black").place(x=150,y=460,width=100, height=30)

    # def mostrarSeleccionado(self):
    #     if self.v.get()==1:
    #         self.label1.configure(text="Freemium")
    #     if self.v.get()==2:
    #         self.label1.configure(text="Estándar")
    #     if self.v.get()==3:
    #         self.label1.configure(text="Premium")
    # var_userType = mostrarSeleccionado
    def register_ventana (self):
        self.root.destroy()
        import login
    
    def register_data(self):
        activ = datetime.date.today()
        self.datos = [(self.var_fnames.get(),
                    self.var_contra.get(),
                    self.var_email.get(),
                    self.var_type.get(),
                    activ)]
        self.tuplaa = tuple(self.datos)
        if self.var_fnames.get() =="" or self.var_email.get()=="" or self.var_contra.get()=="" or self.var_confContra.get() =="" or self.var_type.get() =="":
            messagebox.showerror("Error","Campos vacios",parent=self.root)

        elif self.var_contra.get()==self.var_confContra.get():
                
            self.connection = psycopg2.connect(dbname ="BDDP2", user = "postgres", password ="klipxtreme123_")
            self.cursor = self.connection.cursor()
            self.cursor.executemany("insert into usuarios(usuario,password,email,tipo_suscripcion,activo_desde) values(%s,	%s,	%s,	%s,	%s)",self.tuplaa)
                        
            self.connection.commit ()
            self.connection.close()

            messagebox.showinfo("Sucess","Cuenta creada",parent=self.root)
        else:
            messagebox.showerror("Error","Las contraseñas no coinciden",parent=self.root)
             
root=Tk()
obj = Register(root)
root.mainloop()