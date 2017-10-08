from os import system
from msvcrt import getch
from string import whitespace
from tkinter import Tk
from tkinter.messagebox import showinfo

class Editor():
    def __init__(self):
        self.contents = ""
        self.location = 0
        self.keys = {72: "UP", 80: "DO", 75: "LE", 77: "RI", 23: "QU"}
        self.output = ""
    def open(self, file):
        with open(file) as file:
            self.contents = file.read() + " "
    def start(self):
        system("cls")
        while True:
            try:
                print("--- Python Micronano Editor v0.1 ---")
                print(editor.show())
                editor.move(ord(getch()))
                system("cls")
            except Exception as e:
                if e != "QU":
                    break
                showinfo("Python Micronano Editor v0.1", e)
    def show(self):
        self.output = self.contents[:self.location] + "\u2588" + self.contents[self.location+1:]
        return self.output
    def move(self, code):
        if code in self.keys.keys():
            if self.keys[code] == "LE":
                self.location -= 1
                if self.contents[self.location] in whitespace and self.contents[self.location] != " ":
                    self.location -= 1
                if self.location < 0:
                    self.location = 0
            elif self.keys[code] == "RI":
                self.location += 1
                if self.location  + 2 > len(self.contents):
                    self.location = len(self.contents) - 1
                elif self.contents[self.location] in whitespace and self.contents[self.location] != " ":
                    self.location += 1
            elif self.keys[code] == "QU":
                raise Exception("QU")

Tk().wm_withdraw()
showinfo("Python Micronano Editor v0.1", "Creating Editor...")
editor = Editor()
showinfo("Python Micronano Editor v0.1", "Opening Requested File...")
editor.open("file.txt")
showinfo("Python Micronano Editor v0.1", "Starting Editor...")
editor.start()
showinfo("Python Micronano Editor v0.1", "Closing Editor...")
system("cls")
