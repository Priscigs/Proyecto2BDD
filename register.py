import imp
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import tkinter as tk
from sympy import root
import psycopg2
import hashlib

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


        self.var_contra = StringVar()
        contraseña =Label(text ="Contraseña:",font=("times new roman",15,"bold"),fg="gray").place(x=20,y=320)
        txt_contraseña =Entry(font=("times new roman",15),textvariable=self.var_contra)
        txt_contraseña.place(x=20,y=350)
        txt_contraseña.configure(show="*")
        # self.pruebaa = self.var_contra.get().encode()
        # self.hs = hashlib.md5(self.pruebaa)
        # self.var_contra = self.hs.hexdigest()

        #t_hashed = hashlib.sha3_512(self.var_contra).hexdigest()

        self.var_confContra = StringVar()
        conf_contraseña =Label(text ="Confirmar contraseña:",font=("times new roman",15,"bold"),fg="gray").place(x=20,y=380)
        txt_confcontraseña =Entry(font=("times new roman",15),textvariable=self.var_confContra)
        txt_confcontraseña.place(x=20,y=410)
        txt_confcontraseña.configure(show="*")
        # self.pruebaa2 = self.var_confContra.get().encode()
        # self.hs2 = hashlib.md5(self.pruebaa2)
        # self.var_confContra = self.hs2.hexdigest()

        btn_login =Button(self.root, text= 'Select Profile Type',command= self.register_ventana,activebackground='green', bg='#2A2A46', cursor="hand2",font=('Times new roman', 12,'bold'),fg="black").place(x=100,y=500,width=220, height=30)

        self.v = tk.IntVar()
        self.v.set(3)

        Label(text ="Elige un tipo de cuenta:",
              fg="white", 
              justify= tk.LEFT, 
              padx= 20).place(x=200,y=200)

        self.freemium = tk.Radiobutton(root, 
                              text="Cuenta freemium",
                              command=self.mostrarSeleccionado,
                              padx = 20, 
                              variable=self.v, 
                              value=1).place(x=215,y=240)

        self.standar = tk.Radiobutton(root, 
                              text="Cuenta estándar",
                              command=self.mostrarSeleccionado,
                              padx = 20, 
                              variable=self.v, 
                              value=2).place(x=215,y=270)

        self.premium = tk.Radiobutton(root, 
                              text="Cuenta premium",
                              command=self.mostrarSeleccionado,
                              padx = 20, 
                              variable=self.v, 
                              value=3).place(x=215,y=300)

        self.var_userType = StringVar()
        self.label1 = tk.Label(text ="",
                                    fg="white", 
                                    justify= tk.LEFT, 
                                    padx= 20)
        self.label1.place(x=215,y=330)

        btn_register = Button(self.root, 
                              text= 'Crear Cuenta',
                              command= self.register_data,
                              activebackground='green', 
                              bg='#2A2A46', cursor="hand2",
                              font=('Times new roman', 12,'bold'),
                              fg="black").place(x=150,y=460,width=100, height=30)

    def mostrarSeleccionado(self):
        if self.v.get()==1:
            self.label1.configure(text="Freemium")
        if self.v.get()==2:
            self.label1.configure(text="Estándar")
        if self.v.get()==3:
            self.label1.configure(text="Premium")
    
    def register_ventana (self):
        self.root.destroy()
        import login
    
    def register_data(self):
        if self.var_fnames.get() =="" or self.var_email.get()=="" or self.var_contra.get()=="" or self.var_confContra.get() =="":
            messagebox.showerror("Error","Campos vacios",parent=self.root)

        elif self.var_contra.get()==self.var_confContra.get():
            sus= "Null"
            activ = "Null"
            datos = [(self.var_fnames.get(),
                    self.var_contra.get(),
                    self.var_userType.get(),
                    self.var_email.get(),
                    activ)]
            self.tuplaa = tuple(datos)
            self.connection = psycopg2.connect(dbname ="P2BDD", user = "postgres", password ="klipxtreme123_")
            self.cursor = self.connection.cursor()
            self.cursor.executemany("insert into usuarios(usuario,password,tipo_suscripcion,correo,activo_desde) values(%s,	%s,	%s,	%s,	%s)",self.tuplaa)
                    
            self.connection.commit ()
            self.connection.close()

            messagebox.showinfo("Sucess","Cuenta creada",parent=self.root)
        else:
            messagebox.showerror("Error","Las contraseñas no coinciden",parent=self.root)
             


root=Tk()
obj = Register(root)
root.mainloop()