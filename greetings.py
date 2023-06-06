#!/usr/bin/env python3
import random
import os
import datetime
import json
import time

dirty_words = open('/home/nandi/petProject/greetings/dirty_words.txt', 'r')
content = dirty_words.readlines()
dirty_words.close()

def get_data(filename):
    with open(filename, 'r') as file:
        content = json.load(file)
        return content

def get_date():
    current = datetime.datetime.now()
    return [current.year, current.month, current.day]

def check_date(filename):
    todays_date = get_date()
    data = get_data(filename)
    stored_date = data['date']

    if todays_date != stored_date:
        data['date'] = todays_date
        set_new_date(data)
        print(data['date'])

def set_new_date(update):
    with open('/home/nandi/petProject/greetings/data.json', 'w') as data:
        json.dump(update, data)


def getRandomLine(lines):
    line = lines[random.randint(0, 355)].strip()
    return line

def todaysWord(filename):
    check_date(filename)
    data = get_data(filename)
    word = data['word']
    return word

def createAlert():
    time.sleep(5)
    word = todaysWord('/home/nandi/petProject/greetings/data.json')
    # word = 'faszfütyi'

    os.system("notify-send 'Üdvözöllek, " + word + "' 'Ideje dolgozni'")
    
    
createAlert()
