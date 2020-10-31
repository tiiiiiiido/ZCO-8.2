from datetime import datetime
import webbrowser
import time
import tkinter as tk
import threading 

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def day1 ():  
    with open('data/days/day1.txt', 'r') as day:
        global links
        links = day.readlines()
        
        whileloop()
def day2 ():  
    with open('data/days/day2.txt', 'r') as day:
        global links
        links = day.readlines()
        whileloop()
def day3 ():  
    with open('data/days/day3.txt', 'r') as day:
        global links
        links = day.readlines()
        whileloop()
def day4 ():  
    with open('data/days/day4.txt', 'r') as day:
        global links
        links = day.readlines()
        whileloop()
def day5 ():  
    with open('data/days/day5.txt', 'r') as day:
        global links
        links = day.readlines()
        whileloop()
def day6 ():  
    with open('data/days/day6.txt', 'r') as day:
        global links
        links = day.readlines()
        whileloop()
def day7 ():  
    with open('data/days/day7.txt', 'r') as day:
        global links
        links = day.readlines()
        whileloop()

button1 = tk.Button(text='monday/الأحد',command=day1, bg='black',fg='white')
canvas1.create_window(150, 60, window=button1)

button2 = tk.Button(text='tuesday/الاثنين',command=day2, bg='black',fg='white')
canvas1.create_window(150, 90, window=button2)

button3 = tk.Button(text='wednesday/الثلاثاء',command=day3, bg='black',fg='white')
canvas1.create_window(150, 120, window=button3)

button4 = tk.Button(text='thursday/الاربعاء',command=day4, bg='black',fg='white')
canvas1.create_window(150, 150, window=button4)

button5 = tk.Button(text='friday/الخميس',command=day5, bg='black',fg='white')
canvas1.create_window(150, 180, window=button5)

button6 = tk.Button(text='saturday/الجمعه',command=day6, bg='black',fg='white')
canvas1.create_window(150, 210, window=button6)

button6 = tk.Button(text='sunday/السبت',command=day7, bg='black',fg='white')
canvas1.create_window(150, 210, window=button6)

def whileloop():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        if current_time == "08:15":
            webbrowser.open(links[0])  #link 1
            time.sleep(120)  

        elif current_time == "09:03":
            webbrowser.open(links[1])  #link 2
            time.sleep(120)  

        elif current_time == "09:53":
            webbrowser.open(links[2])  #link 3
            time.sleep(120)  

        elif current_time == "11:08":
            webbrowser.open(links[3])  #link 4
            time.sleep(120)  
        
        elif current_time == "11:58":
            webbrowser.open(links[4])  #link 5
            time.sleep(120)  
        time.sleep(10)
root.mainloop()