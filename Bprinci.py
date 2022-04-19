from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk

class Bprinci:
    def __init__(self,root):
        self.root = root
        self.root.title ("Bprinci")
        self.root.geometry('400x550+600+70')
        
        self.left=ImageTk.PhotoImage(file = "fotos/usuario.png")
        left= Label(self.root,image =self.left).place(x=110,y=30,width=200,height=200)
        
        titulo =Label(text ="SUPER USUARIO",font=("times new roman",20,"bold"),fg="Black").place(x=110,y=180)
        btn_login =Button(self.root, text= 'AGREGAR',command= self.ventanaAgre,activebackground='green', bg='#2A2A46', cursor="hand2",font=('Times new roman', 12,'bold'),fg="white").place(x=65,y=250,width=300, height=60)
        btn_login =Button(self.root, text= 'ELIMINAR ',command= self.ventanaElimi,activebackground='green', bg='#2A2A46', cursor="hand2",font=('Times new roman', 12,'bold'),fg="white").place(x=65,y=310,width=300, height=60)
        btn_login =Button(self.root, text= 'MODIFICAR',command= self.ventanaModifi,activebackground='green', bg='#2A2A46', cursor="hand2",font=('Times new roman', 12,'bold'),fg="white").place(x=65,y=370,width=300, height=60)
        btn_register =Button(self.root, text= 'REGRESAR',command= self.ventadaPrinci,activebackground='green',bg='#2A2A46',font=('Times new roman', 10),bd=0,fg="white").place(x=300,y=460)
    
    def ventanaElimi (self):
        self.root.destroy()
        import eliminar 
    
    def ventanaAgre (self):
        self.root.destroy()
        import agregar

    def ventanaModifi (self):
        self.root.destroy()
        import modificar

    def ventadaPrinci (self):
        self.root.destroy()
        import Main

root=Tk()
obj = Bprinci(root)
root.mainloop()