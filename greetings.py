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

def get_date():
    current = datetime.datetime.now()
    return [current.year, current.month, current.day]

def check_date(filename):
    todays_date = get_date()
    data = get_data(filename)
    stored_date = data['date']

    if todays_date != stored_date or data['word'] == '':
        data['date'] = todays_date
        old_word = data['word']
        data['used'].append(old_word)
        data['word'] = get_new_word(data['used'])
        update_data(data)

def get_new_word(used_words):
    is_new = False
    while is_new == False:
        word = get_random_line()
        if word not in used_words:
            is_new = True

    return word

def update_data(update):
    with open('/home/nandi/petProject/greetings/data.json', 'w') as data:
        json.dump(update, data)


def get_random_line():
    line = content[random.randint(0, 355)].strip()
    return line

def todays_word(filename):
    check_date(filename)
    data = get_data(filename)
    word = data['word']
    return word

def create_alert():
    word = todays_word('/home/nandi/petProject/greetings/data.json')
    timeout_ms = 9999999
    os.system(f"notify-send --expire-time {timeout_ms} 'Üdvözöllek, " + word + "' 'Ideje dolgozni'")
    
    
create_alert()
