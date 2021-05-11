import os, sys
import logging
import tkinter
import psutil
import subprocess
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style



def pressed():
    messagebox.showinfo("Welcome", "Welcome to DarkVenom")

def donothing():
        button = tk.Button(window, text="Do nothing button")
        button.pack()









try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

#displays do nothing



class DarkVen0m(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("DarkVenom")
        self.style = Style()
        self.style.theme_use("default")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text = "Welcome to DarkVenom")
        label.config(font=("Courier", 40) , width= 50, anchor=CENTER)
        label.pack(side="top", fill="x", padx=10, pady=10)

        button1 = tk.Button(self, text="Planning and Preparation", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Reconnaissance", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Discovery", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: controller.show_frame("PageThree"))
        button4 = tk.Button(self, text="Analysing Information & Risks", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: controller.show_frame("PageFour"))
        button5 = tk.Button(self, text="Active Intrusion Attempts", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: controller.show_frame("PageFive"))
        button6 = tk.Button(self, text="Final Analysis", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: controller.show_frame("PageSix"))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label2 = tk.Label(self, text="LoT Security Recommendation basic vulnerabilty", font=controller.title_font)

        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        btn2 = tk.Button(self, text="Calculator", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: subprocess.run([sys.executable, 'calc.py'], check=True))
        
        label.pack(side="top", fill="x", pady=10)
        label2.pack(side="top", fill="x", pady=10)


        button.pack()
        btn2.pack(side=LEFT, padx=5, pady=10)




 #Button Widget



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label2 = tk.Label(self, text="Information Gathering", font=controller.title_font)
        
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        Bnmap = tk.Button(self, text="Nmap", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda:os.system('python3 nmap3.py'))
        Brecon = tk.Button(self, text="Recon", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda:os.popen('bash Reconnaince.sh'))
        
        label.pack(side="top", fill="x", pady=5)
        label2.pack(side="top", fill="x", pady=0)

        button.pack(side="top", pady=10)
        Bnmap.pack(side="top", padx=5)
        Brecon.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 3", font=controller.title_font)
        label2 = tk.Label(self, text="Password Attack", font=controller.title_font)

        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, text="Password Guesses", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda:os.system('python3 password_guesses.py'))

 
        label.pack(side="top", fill="x", pady=10)
        label2.pack()
        button.pack()
        button1.pack()


        

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 4", font=controller.title_font)
        label2 = tk.Label(self, text="Wireless Testing", font=controller.title_font)

        
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        
        label.pack(side="top", fill="x", pady=10)
        label2.pack()
        button.pack()

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 5", font=controller.title_font)
        label2 = tk.Label(self, text="Web Hacking", font=controller.title_font)
               
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        
        label.pack(side="top", fill="x", pady=10)
        label2.pack()
        button.pack()

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 6", font=controller.title_font)
        label2 = tk.Label(self, text="Reporting Results", font=controller.title_font)

        
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        
        label.pack(side="top", fill="x", pady=10)
        label2.pack()
        button.pack()




 

if __name__ == "__main__":
    app= DarkVen0m()
    app.mainloop()

