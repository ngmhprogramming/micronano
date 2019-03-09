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
terminal = Terminal()

curse = initscr()
curse.keypad(1)

with terminal.fullscreen():
    while True:
        for i in range(len(text)):
            with terminal.location(0, i):
                if cursor[0] is i  and len(text[i]) > 0:
                    print(text[i][:cursor[1]]+
                          terminal.black+terminal.on_white+text[i][cursor[1]]+
                          terminal.white+terminal.on_black+text[i][cursor[1]+1:])
                else: print(text[i])
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
