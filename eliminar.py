from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from sympy import root
import psycopg2



class Eliminar:
    def __init__(self,root):
        self.root = root
        self.root.title ("Eliminar")
        self.root.geometry('400x550+600+70')
	
        titulo =Label(text ="Eliminar pelicula:",font=("times new roman",20,"bold"),fg="Black").place(x=70,y=40)

        self.left=ImageTk.PhotoImage(file = "fotos/basura.png")
        left= Label(self.root,image =self.left).place(x=285,y=10,width=128,height=128)

    
        self.var_idPelilcula = StringVar()
        idPelicula =Label(text ="ID de la pelicula:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=200)
        txt_idPelicula =Entry(font=("times new roman",15),textvariable=self.var_idPelilcula).place(x=100,y=240)

        self.var_nombre = StringVar()
        nombre =Label(text ="Nombre de la pelicula:",font=("times new roman",15,"bold"),fg="gray").place(x=100,y=300)
        txt_nombre =Entry(font=("times new roman",15),textvariable=self.var_nombre).place(x=100,y=340)
        
        
        btn_register =Button(self.root, text= 'ELIMINAR ',command= self.verificar_data,activebackground='green', bg='#2A2A46',font=('Times new roman', 10),bd=0,fg="white").place(x=200,y=440)
        btn_login =Button(self.root, text= 'REGRESAR',command= self.regresar_ventana, activebackground='green', bg='#2A2A46', cursor="hand2",font=('Times new roman', 12,'bold'),fg="white").place(x=220,y=500,width=150, height=30)
    
             

    def regresar_ventana (self):
        self.root.destroy()
        import Bprinci
    
    def usuario (self):
        self.root.destroy()
        import Bprinci

    def verificar_data(self):
        if self.var_idPelilcula.get() =="" or self.var_nombre.get()=="" :
            messagebox.showerror("Error","Campos vacios",parent=self.root)
        else: 
            
                datos = [self.var_idPelilcula.get(),self.var_nombre.get()]
                self.tuplas = tuple(datos)
                self.connection = psycopg2.connect(dbname ="proyecto02-BBD", user = "postgres", password ="3369")
                self.cursor = self.connection.cursor()
                self.cursor.execute("DELETE FROM peliculas WHERE id_pelicula=%s and titulo =%s",self.tuplas)
                row =self.cursor.fetchone()
                print (row)
                if row == None:
                    messagebox.showerror("Error","No es posible eliminar esa pelilcula",parent=self.root)
                else:
                    messagebox.showinfo("Sucess","Se inicio sesion",parent=self.root)
                    self.connection.commit ()
                    self.connection.close()
        
root=Tk()
obj = Eliminar(root)
root.mainloop()