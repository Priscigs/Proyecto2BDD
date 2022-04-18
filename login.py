from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from sympy import root
import psycopg2
from hashlib import sha256

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title ("Login")
        self.root.geometry('400x550+600+70')
	
        self.left=ImageTk.PhotoImage(file = "fotos/images.png")
        left= Label(self.root,image =self.left).place(x=60, y=-160,width=300,height=500)
        titulo =Label(text ="Inicio de sesion:",font=("times new roman",20,"bold"),fg="Black").place(x=121,y=200)

        self.var_email = StringVar()
        email =Label(text ="Email:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=260)
        txt_email =Entry(font=("times new roman",15),textvariable=self.var_email).place(x=100,y=290)

        

        self.contraHash = StringVar()

        self.var_contra = StringVar(value='')
        contraseña =Label(text ="Contraseña:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=320)
        self.txt_contraseña =Entry(font=("times new roman",15),textvariable=self.var_contra)
        self.txt_contraseña.place(x=100,y=350)
        self.txt_contraseña.configure(show="*")

        # ALMACENAMIENTO DE HASH CON SHA256
        h = sha256()
        h.update(self.txt_contraseña.get().encode())
        self.contraHash.set(h.hexdigest())
        
        btn_register =Button(self.root, text= '¿Registrar nueva cuenta?',command= self.register_ventana,font=('Times new roman', 10),bd=0,bg="white",fg="black").place(x=100,y=390)
        btn_register =Button(self.root, text= 'Login',command= self.verificar_data,activebackground='green', bg='#2A2A46', cursor="hand2",font=('Times new roman', 12,'bold'),fg="white").place(x=145,y=440,width=110, height=30)
        btn_register =Button(self.root, text= 'Super Usuario',command= self.bPrin,activebackground='green', bg='#2A2A46', cursor="hand2",font=('Times new roman', 12,'bold'),fg="white").place(x=145,y=470,width=110, height=30)

        # cont = 1
        # while cont <= 3:
        #     if self.var_email
    def register_ventana (self):
        self.root.destroy()
        import register

    def bPrin (self):
        self.root.destroy()
        import Bprinci

    def verificar_data(self):
        if self.var_email.get() =="" or self.var_contra.get()=="" :
            messagebox.showerror("Error","Campos vacios",parent=self.root)
        
        else: 
            try:
                datos = [self.var_email.get(),self.contraHash.get()]
                self.tuplas = tuple(datos)
                self.connection = psycopg2.connect(dbname ="BDDP2", user = "postgres", password ="klipxtreme123_")
                self.cursor = self.connection.cursor()
                self.cursor.execute("SELECT* FROM usuarios WHERE email=%s and password =%s",self.tuplas)
                
                row =self.cursor.fetchone()
                if row ==None:
                    messagebox.showerror("Error","Correo o contraseña incorrectos",parent=self.root)
                else:
                    messagebox.showinfo("Sucess","Se inicio sesion",parent=self.root)
                    #self.movies
                    self.connection.commit ()
                    self.connection.close()
                    self.root.destroy()
                    import movies
            except Exception as es:
                 messagebox.showerror("Error","Error Due to: {str (es)}",parent=self.root)

root=Tk()
obj = Login(root)
root.mainloop()