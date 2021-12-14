#substituesanta

import time as t
import random
import turtle
import tkinter
import sys as s

f = open("önskelista.txt","r")


print("I detta program får du skapa eller läsa av en önskelista.")
t.sleep(0)
while True:
    svar=int(input("1. Vill du skapa önskelista? \n2. Vill du läsa av en önskelista?"))
    if svar== 1:
        input_string = input("Skriv in din önskelista")
        list  = input_string.split("\n")
        
        t.sleep(1)

        def print_slow(str):
            for letter in str:
                s.stdout.write(letter)
                s.stdout.flush()
                t.sleep(0.1)

        print_slow("\nGenererar din önskelista...")
        t.sleep(0)
        for wish in list:
            print(wish)
            break
        a_list = [wish]
        textfile = open("önskelista.txt", "w")
        for element in a_list:
            textfile.write(element + "\n")
        textfile.close()
        if svar== 2:
            print(f.readlines())
            print()
            f.close()