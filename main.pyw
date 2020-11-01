import datetime
day = datetime.datetime.now()
print(day.strftime("%A"))
from datetime import datetime
import webbrowser
import time

if day.strftime("%A") == "Sunday":
    with open('data/days/day1.txt', 'r') as day:
        print("today is sunday")
        links = day.readlines()      
elif day.strftime("%A") == "Monday":
    with open('data/days/day2.txt', 'r') as day:
        print("today is Monday")            
        links = day.readlines()      
elif day.strftime("%A") == "Tuesday":
    with open('data/days/day3.txt', 'r') as day:
        print("today is Tuesday")            
        links = day.readlines()  
elif day.strftime("%A") == "Wednesday":
    with open('data/days/day4.txt', 'r') as day:
        print("today is Wednesday")            
        links = day.readlines()     
elif day.strftime("%A") == "Thursday":
    with open('data/days/day5.txt', 'r') as day:
        print("today is Thursday")           
        links = day.readlines()    
elif day.strftime("%A") == "Friday": 
    with open('data/days/day6.txt', 'r') as day:
        print("today is Friday") 
        links = day.readlines()      
elif day.strftime("%A") == "Saturday":
    with open('data/days/day7.txt', 'r') as day:
        print("today is Saturday")
        links = day.readlines()

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M") #cals the time

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