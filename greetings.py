#!/usr/bin/env python3
import random
import os

dirty_words = open("/home/nandi/petProject/greetings/dirty_words.txt", "r")
content = dirty_words.readlines()
dirty_words.close()

def getRandomLine(lines):
    line = lines[random.randint(0, 355)].strip()
    return line

def createMessage(title, message):
    return "notify-send" + " " + title + " " +  message

def createAlert():
    line = getRandomLine(content)

    os.system("notify-send 'Üdvözöllek, " + line + "' 'Ideje dolgozni'")
    
createAlert()
