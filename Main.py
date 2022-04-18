from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk



class Main:
    def __init__(self,root):
        self.root = root
        self.root.title ("Main")
        self.root.geometry('400x550+600+70')
        
        
        
        self.left=ImageTk.PhotoImage(file = "fotos/images.png")
        left= Label(self.root,image =self.left).place(x=70, y=-110,width=300,height=500)

        btn_login =Button(self.root, text= 'CREAR CUENTA',command= self.ventanaRe,activebackground='green', bg='#2A2A46', cursor="hand2",font=('Times new roman', 12,'bold'),fg="white").place(x=106,y=280,width=220, height=30)
        btn_login =Button(self.root, text= 'SING IN',command= self.ventanaLo,activebackground='green', bg='#2A2A46', cursor="hand2",font=('Times new roman', 12,'bold'),fg="white").place(x=106,y=330,width=220, height=30)
    
    def ventanaRe (self):
        self.root.destroy()
        import register
    

    def ventanaLo (self):
        self.root.destroy()
        import login
    





root=Tk()
obj = Main(root)
root.mainloop()