import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk
from Musica import Musica

class Gui:
    def __init__(self):
        self.image()
        self.entry()
        self.label(text1)
        self.button()
        self.menu()

    def image(self):
        img = Image.open('image/rikka.jpg')
        img_resize = img.resize((190, 300), Image.ANTIALIAS)
        self.imgTk = ImageTk.PhotoImage(img_resize)
        lab = tk.Label(win, image=self.imgTk)
        lab.place(x=0, y=0)  

    def entry(self):    
        global var1
        global var2
        global var3
        entry1 = tk.Entry(win, textvariable=var1, font=("" , 13))
        entry1.place(x=400, y=120)

        entry21 = tk.Entry(win, textvariable=var2, font=("" , 10))
        entry21.place(x=320, y=160)

        entry22 = tk.Entry(win, textvariable=var4, font=("" , 10))
        entry22.place(x=490, y=160)

        entry3 = tk.Entry(win, textvariable=var3, font=("" , 13))
        entry3.place(x=400, y=200)

    def label(self, text):    
        lab0 = tk.Label(win, text=text1, font=("" , 20))
        lab0.place(x=200, y=0)

        lab1 = tk.Label(win, text='Card number: ', font=("" , 13))
        lab1.place(x=240, y=120)

        lab2 = tk.Label(win, text='Expiry: ', font=("" , 13))
        lab2.place(x=240, y=160)

        lab3 = tk.Label(win, text='Security code: ', font=("" , 13))
        lab3.place(x=240, y=200)

        lab4 = tk.Label(win, text='/', font=("" , 20))
        lab4.place(x=470, y=150)


    def button(self):
        button = tk.Button(win, text='Th-thanks', command=self.action)
        button.place(x=350, y=250)

    def action(self):
            global var1
            global var2
            global var3
            global var4
            global musica
            if str(var1.get()) == "" or str(var2.get()) == "" or str(var3.get()) == "" or str(var4.get()) == "":
                tkinter.messagebox.showerror('ERROR', 'Missing data')

            elif len(str(var1.get())) != 16:
                var1.set('must be 16 digits')
            
            elif len(str(var2.get())) != 2 or len(str(var4.get())) != 2 :
                var2.set('must be Mounth')
                var4.set('must be Year')
            elif len(str(var3.get())) != 3 and len(str(var3.get())) != 4:
                var3.set('must be 3 or 4 digits')
            else:
                fp = open('data.txt', 'w')
                fp.write("Cart number: " + str(var1.get()) + "\n")
                fp.write("expiry: " + str(var2.get()) + "/" + str(var4.get()) + "\n")
                fp.write("Security code: " + str(var3.get()) + "\n")
                fp.close()
                musica.start_song(1)

    def menu(self):
        menu = tk.Menu(win)
        menu.add_command(label='Info', command=self.info)
        win.configure(menu=menu)
    
    def info(self):
        tkinter.messagebox.showinfo('Info get data', 'Author: Antonino Buscarino')

win = tk.Tk()
win.geometry('650x300')
win.title('Rikka-sama')
win.iconbitmap('image/icon_rikka.ico')
win.resizable(False, False)

musica = Musica.Musica('song/arigato.wav')

text1 = '''H-hi there...
    Do you th-think I could have your
    credit card information, p-please?'''

var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()

gui = Gui()

win.mainloop()