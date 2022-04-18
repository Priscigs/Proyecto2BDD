from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from sympy import root
import psycopg2



class Agregar:
    def __init__(self,root):
        self.root = root
        self.root.title ("Agregar")
        self.root.geometry('400x550+600+70')
	
        titulo =Label(text ="Agregar una pelicula:",font=("times new roman",20,"bold"),fg="Black").place(x=90,y=30)

        self.var_fduracion= StringVar()
        duracion =Label(text ="Duracion:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=80)
        txt_fduracion =Entry(font=("times new roman",15),textvariable=self.var_fduracion).place(x=100,y=110)


        self.var_idpelicula = StringVar()
        pelicula =Label(text ="ID de la pelicula:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=140)
        txt_pelicula =Entry(font=("times new roman",15),textvariable=self.var_idpelicula).place(x=100,y=170)


        self.var_tituloPeli = StringVar()
        tituloPeli =Label(text ="Titulo de la pelicula:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=200)
        txt_tituloPeli =Entry(font=("times new roman",15),textvariable=self.var_tituloPeli).place(x=100,y=230)

        self.var_fechaL= StringVar()
        fechaL =Label(text ="Fecha de lanzamiento:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=260)
        txt_fechaL =Entry(font=("times new roman",15),textvariable=self.var_fechaL).place(x=100,y=290)

        self.var_genero= StringVar()
        fechaL =Label(text ="Genero de la pelicula:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=320)
        txt_fechaL =Entry(font=("times new roman",15),textvariable=self.var_genero).place(x=100,y=350)

        self.var_premios= StringVar()
        premios =Label(text ="Premios que gano la pelicula:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=380)
        txt_premios =Entry(font=("times new roman",15),textvariable=self.var_premios).place(x=100,y=410)

        btn_register =Button(self.root, text= 'AGREGAR PELICULA',command= self.register_data,activebackground='green',bg='#2A2A46',font=('Times new roman', 10),bd=0,fg="white").place(x=200,y=460)
        btn_login =Button(self.root, text= 'Regresar',command= self.regresar_ventana,activebackground='green',bg='#2A2A46',font=('Times new roman', 10),bd=0,fg="White").place(x=100,y=500,width=220, height=30)
    
    def regresar_ventana (self):
        import Bprinci
    
    def register_data(self):
        if self.var_fduracion.get() =="" or self.var_idpelicula.get()=="" or self.var_fechaL.get()=="" or self.var_fechaL.get() =="" or self.var_genero.get() =="" or self.var_premios.get() =="" :
            messagebox.showerror("Error","Campos vacios",parent=self.root)

        elif self.var_fduracion.get() !="" or self.var_idpelicula.get() !="" or self.var_fechaL.get() !="" or self.var_fechaL.get() !="" or self.var_genero.get() !="" or self.var_premios.get() !="":
            datos = [(self.var_fduracion.get(),
                    self.var_idpelicula.get(),
                    self.var_tituloPeli.get(),self.var_genero.get(), self.var_premios.get(),  self.var_fechaL.get())]
            self.tuplaa = tuple(datos)
            self.connection = psycopg2.connect(dbname ="proyecto02-BBD", user = "postgres", password ="3369")
            self.cursor = self.connection.cursor()
            self.cursor.executemany("insert into peliculas(duracion,id_pelicula,titulo,genero,premios_ganados,fecha_lanzamiento) values(%s,	%s,	%s,	%s,	%s,	%s)",self.tuplaa)
                    
            self.connection.commit ()
            self.connection.close()

            messagebox.showinfo("Sucess","Se ha agredado esta pelicula con exito",parent=self.root)
        else:
          messagebox.showerror("Error","No se ha podido agregar su pelicula",parent=self.root)
             


root=Tk()
obj = Agregar(root)
root.mainloop()