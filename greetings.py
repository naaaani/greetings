#!/usr/bin/env python3
import random
import os
import datetime

dirty_words = open('/home/nandi/petProject/greetings/dirty_words.txt', 'r')
content = dirty_words.readlines()
dirty_words.close()

def getDate():
    current = datetime.datetime.now()
    return [current.year, current.month, current.day]

today = {
    'date': [],
    'word': 'fasz',
    'used': [],
}

def check_date(today):
    date = datetime.datetime.now()
    todays_date = [date.year, date.month, date.day]

    if todays_date != today['date']:
        today['date'] = todays_date
        print(today)
    
def getRandomLine(lines):
    line = lines[random.randint(0, 355)].strip()
    return line

#TODO implement json solution
def todaysWord():
    
    if os.stat('/home/nandi/petProject/greetings/today.txt').st_size == 0:
        today = open('/home/nandi/petProject/greetings/today.txt', 'r+')
        today.write(getRandomLine(content))
        today.close()

    today = open('/home/nandi/petProject/greetings/today.txt', 'r')
    word = today.readline()
    today.close()
    return word

def createAlert():
    word = todaysWord()

    os.system("notify-send 'Üdvözöllek, " + word + "' 'Ideje dolgozni'")
    
    
createAlert()
check_date(today)