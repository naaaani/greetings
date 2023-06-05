#!/usr/bin/env python3
import random
import os
import datetime
import json

dirty_words = open('/home/nandi/petProject/greetings/dirty_words.txt', 'r')
content = dirty_words.readlines()
dirty_words.close()

def get_data(filename):
    with open(filename, 'r') as file:
        content = json.load(file)
        return content

def getDate():
    current = datetime.datetime.now()
    return [current.year, current.month, current.day]

def check_date(today):
    date = datetime.datetime.now()
    todays_date = [date.year, date.month, date.day]
    data = get_data('data.json')
    stored_date = data['date']

    if todays_date != stored_date:
        data['date'] = todays_date
        set_new_date(data)


def set_new_date(update):
    with open('data.json', 'w') as data:
        json.dump(update, data)



def getRandomLine(lines):
    line = lines[random.randint(0, 355)].strip()
    return line

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