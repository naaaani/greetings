#!/usr/bin/env python3
import random
import os

dirty_words = open('/home/nandi/petProject/greetings/dirty_words.txt', 'r')
content = dirty_words.readlines()
dirty_words.close()

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
