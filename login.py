from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from sympy import root
import psycopg2


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

        self.var_contra = StringVar()
        contraseña =Label(text ="Contraseña:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=320)
        txt_contraseña =Entry(font=("times new roman",15),textvariable=self.var_contra)
        txt_contraseña.place(x=100,y=350)
        txt_contraseña.configure(show="*")
        
        btn_register =Button(self.root, text= '¿Registrar nueva cuenta?',command= self.register_ventana,font=('Times new roman', 10),bd=0,bg="white",fg="black").place(x=100,y=390)
        btn_register =Button(self.root, text= 'Login',command= self.verificar_data,activebackground='green', bg='#2A2A46', cursor="hand2",font=('Times new roman', 12,'bold'),fg="white").place(x=200,y=460,width=110, height=30)

    def register_ventana (self):
        self.root.destroy()
        import register

    def verificar_data(self):
        if self.var_email.get() =="" or self.var_contra.get()=="" :
            messagebox.showerror("Error","Campos vacios",parent=self.root)
        
        else: 
            try:
                datos = [self.var_email.get(),self.var_contra.get()]
                self.tuplas = tuple(datos)
                self.connection = psycopg2.connect(dbname ="proyecto02-BBD", user = "postgres", password ="3369")
                self.cursor = self.connection.cursor()
                self.cursor.execute("SELECT* FROM usuarios WHERE correo=%s and password =%s",self.tuplas)
                
                row =self.cursor.fetchone()
                if row ==None:
                    messagebox.showerror("Error","Correo o contraseña incorrectos",parent=self.root)
                else:
                    messagebox.showinfo("Sucess","Se inicio sesion",parent=self.root)
                    self.connection.commit ()
                    self.connection.close()
            except Exception as es:
                 messagebox.showerror("Error","Error Due to: {str (es)}",parent=self.root)

root=Tk()
obj = Login(root)
root.mainloop()