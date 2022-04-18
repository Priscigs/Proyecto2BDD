
from tkinter import*
from PIL import Image,ImageTk
from sympy import root
import pywhatkit as kit
import webbrowser
import searchQueries as sQ

class Movies:

    def buscar(self, item):
        lista = []
        actor = sQ.searchByActor(item)
        genero = sQ.searchByGenre(item)
        director = sQ.searchByDirector(item)
        movie = sQ.searchByMovie(item)
        lista.append(actor)
        lista.append(genero)
        lista.append(director)
        lista.append(movie)

    def __init__(self,root):
        self.root = root
        self.root.title ("Movies")
        self.root.geometry('790x500+300+100')
	
        self.left=ImageTk.PhotoImage(file = "fotos/images.png")
        left= Label(self.root,image =self.left).place(x=70, y=-160,width=650,height=500)

        self.search= StringVar()
        nombre =Label(text ="Buscar:",font=("times new roman",15,"bold"),fg="gray").place(x=20,y=200)
        txt_search =Entry(font=("times new roman",15),textvariable=self.search).place(x=80,y=200)

        btn_buscar = Button(self.root, 
                              text= 'Buscar',
                              command= self.buscar(self.search.get()),
                              activebackground='green', 
                              bg='#2A2A46', cursor="hand2",
                              font=('Times new roman', 12,'bold'),
                              fg="black").place(x=250,y=200,width=100, height=30)
        
        self.info = StringVar()
        infoM =Label(text =self.search.get(),font=("times new roman",15,"bold"),fg="white").place(x=600,y=50)

        self.movie1 = Image.open("fotos/batman.png")
        self.movie1 = self.movie1.resize((100,150), Image.ANTIALIAS)
        self.movie11 = ImageTk.PhotoImage(self.movie1)
        btn_movie1 = Button(self.root, 
                            image= self.movie11,
                            command= lambda: kit.playonyt("BATMAN Tráiler Español"),
                            fg="black") 
        btn_movie1.place(
            x=20.0,
            y=250.0,
            width=100.0,
            height=150.0
        )

        self.movie2 = Image.open("fotos/vemon.png")
        self.movie2 = self.movie2.resize((100,150), Image.ANTIALIAS)
        self.movie22 = ImageTk.PhotoImage(self.movie2)
        btn_movie2 = Button(self.root, 
                            image= self.movie22,
                            command= lambda: kit.playonyt("VENOM 2 Tráiler Español"),
                            fg="black") 
        btn_movie2.place(
            x=150.0,
            y=250.0,
            width=100.0,
            height=150.0
        )

        self.movie3 = Image.open("fotos/spiderman.png")
        self.movie3 = self.movie3.resize((100,150), Image.ANTIALIAS)
        self.movie33 = ImageTk.PhotoImage(self.movie3)
        btn_movie3 = Button(self.root, 
                            image= self.movie33,
                            command= lambda: kit.playonyt("SPIDER-MAN: NO WAY HOME"),
                            fg="black") 
        btn_movie3.place(
            x=280.0,
            y=250.0,
            width=100.0,
            height=150.0
        )

        self.movie4 = Image.open("fotos/loverosie.jpeg")
        self.movie4 = self.movie4.resize((100,150), Image.ANTIALIAS)
        self.movie44 = ImageTk.PhotoImage(self.movie4)
        btn_movie4 = Button(self.root, 
                            image= self.movie44,
                            command= lambda: kit.playonyt("Love, Rosie"),
                            fg="black") 
        btn_movie4.place(
            x=410.0,
            y=250.0,
            width=100.0,
            height=150.0
        )

        self.movie5 = Image.open("fotos/shrek.jpeg")
        self.movie5 = self.movie5.resize((100,150), Image.ANTIALIAS)
        self.movie55 = ImageTk.PhotoImage(self.movie5)
        btn_movie5 = Button(self.root, 
                            image= self.movie55,
                            command= lambda: kit.playonyt("Shrek (2001) Trailer #1"),
                            fg="black") 
        btn_movie5.place(
            x=540.0,
            y=250.0,
            width=100.0,
            height=150.0
        )
 
        self.movie6 = Image.open("fotos/encanto.jpeg")
        self.movie6 = self.movie6.resize((100,150), Image.ANTIALIAS)
        self.movie66 = ImageTk.PhotoImage(self.movie6)
        btn_movie6 = Button(self.root, 
                            image= self.movie66,
                            command= lambda: kit.playonyt("Encanto"),
                            fg="black") 
        btn_movie6.place(
            x=670.0,
            y=250.0,
            width=100.0,
            height=150.0
        )
             
root=Tk()
obj = Movies(root)
root.mainloop()