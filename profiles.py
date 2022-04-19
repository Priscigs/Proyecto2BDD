from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from sympy import root
import psycopg2

class Profiles:
    def __init__(self,root):
        self.root = root
        self.root.title ("Profiles")
        self.root.geometry('400x550+600+70') 
	
        self.left=ImageTk.PhotoImage(file = "fotos/images.png")
        left= Label(self.root,image =self.left).place(x=70, y=-160,width=300,height=500)

        self.var_perfiles= StringVar()
        nombre =Label(text ="Perfiles:",font=("times new roman",30,"bold"),fg="gray").place(x=20,y=200)
       
        self.var_agregar = StringVar()
        email =Label(text ="Código Perfil:",font=("times new roman",15,"bold"),fg="gray").place(x=20,y=260)
        txt_agregar =Entry(font=("times new roman",15),textvariable=self.var_agregar).place(x=140,y=260)

        self.var_nom = StringVar()
        email =Label(text ="Nombre Perfil:",font=("times new roman",15,"bold"),fg="gray").place(x=20,y=310)
        txt_nom =Entry(font=("times new roman",15),textvariable=self.var_nom).place(x=140,y=310)

        self.var_tipo = StringVar()
        email =Label(text ="Tipo Perfil:",font=("times new roman",15,"bold"),fg="gray").place(x=20,y=360)
        txt_tipo =Entry(font=("times new roman",15),textvariable=self.var_tipo).place(x=140,y=360)

        self.var_user = StringVar()
        email =Label(text ="Usuario Perfil:",font=("times new roman",15,"bold"),fg="gray").place(x=20,y=410)
        txt_user =Entry(font=("times new roman",15),textvariable=self.var_user).place(x=140,y=410)

        btn_agregar = Button(self.root, 
                              text= 'Agregar',
                              command= self.register_data,
                              activebackground='green', 
                              bg='#2A2A46', cursor="hand2",
                              font=('Times new roman', 12,'bold'),
                              fg="black").place(x=100,y=460,width=65, height=30)

        btn_volver = Button(self.root, 
                              text= 'Regresar',
                              command= self.register_ventana,
                              activebackground='green', 
                              bg='#2A2A46', cursor="hand2",
                              font=('Times new roman', 12,'bold'),
                              fg="black").place(x=220,y=460,width=65, height=30)

        btn_volver = Button(self.root, 
                              text= 'Opciones de Usuario',
                              command= self.superU,
                              activebackground='green', 
                              bg='#2A2A46', cursor="hand2",
                              font=('Times new roman', 12,'bold'),
                              fg="black").place(x=105,y=500,width=180, height=30)

    def register_ventana (self):
        self.root.destroy()
        import login

    def superU (self):
        self.root.destroy()
        import Bprinci
    
    def register_data(self):
        self.datos = [(self.var_agregar.get(),
                    self.var_nom.get(),
                    self.var_tipo.get(),
                    self.var_user.get())]
        self.tuplaa = tuple(self.datos)
        if self.var_agregar.get() =="" or self.var_nom.get()=="" or self.var_tipo.get()=="" or self.var_user.get() =="":
            messagebox.showerror("Error","Campos vacios",parent=self.root)

        elif self.var_agregar.get() !="" or self.var_nom.get() !="" or self.var_tipo.get() !="" or self.var_user.get() !="":
            self.connection = psycopg2.connect(dbname ="BDDP2", user = "postgres", password ="klipxtreme123_")
            self.cursor = self.connection.cursor()
            self.cursor.executemany("insert into perfiles(id_perfil,nombre_perfil,tipo_perfil,usuario) values(%s,	%s,	%s,	%s)",self.tuplaa)
                      
            self.connection.commit ()
            self.connection.close()

            messagebox.showinfo("Sucess","Perfil Añadido Correctamente",parent=self.root)
        else:
            messagebox.showerror("Error","Los perfiles no se pudieron añadir, por favor probar nuevamente",parent=self.root)
                
             
root=Tk()
obj = Profiles(root)
root.mainloop()