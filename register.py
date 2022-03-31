from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from sympy import root
import psycopg2


class Register:
    def __init__(self,root):
        self.root = root
        self.root.title ("Register")
        self.root.geometry('400x550+600+70')
	
        self.left=ImageTk.PhotoImage(file = "fotos/images.png")
        left= Label(self.root,image =self.left).place(x=70, y=-160,width=300,height=500)

        self.var_fnames= StringVar()
        nombre =Label(text ="Nombre:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=200)
        txt_fname =Entry(font=("times new roman",15),textvariable=self.var_fnames).place(x=100,y=230)
       
        self.var_email = StringVar()
        email =Label(text ="Email:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=260)
        txt_email =Entry(font=("times new roman",15),textvariable=self.var_email).place(x=100,y=290)


        self.var_contra = StringVar()
        contraseña =Label(text ="Contraseña:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=320)
        txt_contraseña =Entry(font=("times new roman",15),textvariable=self.var_contra).place(x=100,y=350)

        self.var_confContra = StringVar()
        conf_contraseña =Label(text ="Confirmar contraseña:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=380)
        txt_confcontraseña =Entry(font=("times new roman",15),textvariable=self.var_confContra).place(x=100,y=410)

        btn_register =Button(self.root, text= 'Crear cuenta',command= self.register_data,font=('Times new roman', 10),bd=0,bg="white",fg="black").place(x=200,y=460)
        btn_login =Button(self.root, text= 'SING IN',command= self.register_data,activebackground='green', bg='#2A2A46', cursor="hand2",font=('Times new roman', 12,'bold'),fg="white").place(x=100,y=500,width=220, height=30)
    
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
                    sus,
                    self.var_email.get(),
                    activ)]
            self.tuplaa = tuple(datos)
            self.connection = psycopg2.connect(dbname ="proyecto02-BBD", user = "postgres", password ="3369")
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