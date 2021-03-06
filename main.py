from sys import argv
from blessings import Terminal
from curses import initscr, endwin
#from readchar import readkey
from time import sleep

if(len(argv) < 2):
    print("No input file")
    exit()

text = open(argv[1]).read().splitlines()
cursor = [0, 23]
char = ""
p = ""
terminal = Terminal()

curse = initscr()
curse.keypad(1)

with terminal.fullscreen():
    while True:
        for i in range(len(text)):
            with terminal.location(0, i):
                p = terminal.white+terminal.on_black
                if cursor[0] is i:
                    if len(text[i]) > 0:
                        p += text[i][:cursor[1]]
                        p += terminal.black+terminal.on_white
                        p += text[i][cursor[1]]
                        p += terminal.white+terminal.on_black
                        p += text[i][cursor[1]+1:]
                    else:
                        p += " "
                        p += terminal.white+terminal.on_black
                else:
                    if len(text[i]) > 0: p += text[i]
                    else: p += " "
                print(p)
        char = curse.getkey()
        if char is "q":
            endwin()
            exit()
        elif char == "KEY_UP" and cursor[0] > 0:
            cursor[0] -= 1
            cursor[1] = min(cursor[1], len(text[cursor[0]])-1)
        elif char == "KEY_DOWN" and cursor[0] < len(text)-1:
            cursor[0] += 1
            cursor[1] = min(cursor[1], len(text[cursor[0]])-1)
        elif char == "KEY_LEFT" and cursor[1] > 0: cursor[1] -= 1
        elif char == "KEY_RIGHT" and cursor[1] < len(text[cursor[0]])-1: cursor[1] += 1
