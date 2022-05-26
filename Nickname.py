#!/usr/bin/python3
from game import Game
from tkinter import *

import Enrengistreur_donner



class MyWindow(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.__name = StringVar()

        label = Label(self, text="Ton pseudo ""!:")
        label2 = Label(self, text="(Le Pseudo changeras au redémarrage du jeu !)")
        label3 = Label(self, text="(si tu ne veut pas le changer ferme directement la fenêtre)")
        label.pack()
        label2.pack()
        label3.pack()

        name = Entry(self, textvariable=self.__name)

        name.focus_set()
        name.pack()

        button = Button(self, text="Enrengistrée !", command=self.doSomething)
        button.pack()

        self.geometry("400x200")
        self.title("Entre ton Pseudo")



    def doSomething(self):
        dict1 = self.__name.get().split('"')
        file1 = open("user_data/namedata.py", "w")
        file1.write("%s = %s\n" % ("dict1 ", dict1))
        self.__name.get()


window = MyWindow()
window.mainloop()
