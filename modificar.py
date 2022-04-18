from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from sympy import root
import psycopg2



class Modificar:
    def __init__(self,root):
        self.root = root
        self.root.title ("Modificar")
        self.root.geometry('400x550+600+70')
	
        titulo =Label(text ="Modificar una pelicula:",font=("times new roman",20,"bold"),fg="Black").place(x=90,y=5)

        self.var_fedit= StringVar()
        edit =Label(text ="ID de la pelicula a modificar:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=50)
        txt_fedit=Entry(font=("times new roman",15),textvariable=self.var_fedit).place(x=100,y=80)

        self.var_fduracion= StringVar()
        duracion =Label(text ="Duracion:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=120)
        txt_fduracion =Entry(font=("times new roman",15),textvariable=self.var_fduracion).place(x=100,y=150)


        self.var_idpelicula = StringVar()
        pelicula =Label(text ="nombre de la pelicula:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=180)
        txt_pelicula =Entry(font=("times new roman",15),textvariable=self.var_idpelicula).place(x=100,y=220)

        self.var_fechaL= StringVar()
        fechaL =Label(text ="Fecha de lanzamiento:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=250)
        txt_fechaL =Entry(font=("times new roman",15),textvariable=self.var_fechaL).place(x=100,y=280)

        self.var_genero= StringVar()
        fechaL =Label(text ="Clasificacion:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=320)
        txt_clasi =Entry(font=("times new roman",15),textvariable=self.var_genero).place(x=100,y=350)

        self.var_premios= StringVar()
        premios =Label(text ="Director de la pelicula:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=380)
        txt_premios =Entry(font=("times new roman",15),textvariable=self.var_premios).place(x=100,y=410)

        btn_register =Button(self.root, text= 'AGREGAR PELICULA',command= self.register_data,activebackground='green',bg='#2A2A46',font=('Times new roman', 10),bd=0,fg="white").place(x=200,y=460)
        btn_login =Button(self.root, text= 'Regresar',command= self.regresar_ventana,activebackground='green',bg='#2A2A46',font=('Times new roman', 10),bd=0,fg="White").place(x=100,y=500,width=220, height=30)
    
    def regresar_ventana (self):
        import Bprinci
    
    def register_data(self):
        if self.var_fedit.get() =="" or self.var_fduracion.get() =="" or self.var_idpelicula.get()=="" or self.var_fechaL.get()=="" or self.var_fechaL.get() =="" or self.var_genero.get() =="" or self.var_premios.get() =="" :
            messagebox.showerror("Error","Campos vacios",parent=self.root)

        elif self.var_fedit.get() !="" or self.var_fduracion.get() !="" or self.var_idpelicula.get() !="" or self.var_fechaL.get() !="" or self.var_fechaL.get() !="" or self.var_genero.get() !="" or self.var_premios.get() !="":
            datos = [(self.var_fduracion.get(),
                    self.var_idpelicula.get(),
                    self.var_fedit.get(), self.var_premios.get(),  self.var_fechaL.get(),self.var_genero.get())]
            self.tuplaa = tuple(datos)
            self.connection = psycopg2.connect(dbname ="Proyecto2", user = "postgres", password ="3369")
            self.cursor = self.connection.cursor()
            self.cursor.executemany("UPDATE peliculas SET duracion= %s, titulo = %s, director =%s, fecha_lanzamiento =%s ,clasificacion =%s WHERE id_pelicula = %s", self.tuplaa)
                    
            self.connection.commit ()
            self.connection.close()

            messagebox.showinfo("Sucess","Se ha modificado  esta pelicula con exito",parent=self.root)
        else:
          messagebox.showerror("Error","No se ha podido modificar  su pelicula",parent=self.root)
             


root=Tk()
obj = Modificar(root)
root.mainloop()