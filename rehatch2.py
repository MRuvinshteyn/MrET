#Michael Ruvinshteyn & Euguene Thomas
#SoftDev1 pd 7
#HW 03 -- StI/O: Divine your Destiny!
#2017 - 09 - 14

import random

d = {}

def special_split(s): #splits string by commas taking double quotes into account
    x = 1
    l = []
    if s[0] == '"':
        while s[x] != '"':
            x += 1
        l.append(s[0:x+1])
        l.append(s[x+2:])
    else:
        l = s.split(',')
    return l

def create_dict():
    try:
        o = open('occupations.csv', 'rU')
        r = o.read()
        o.close()
    except:
        print "The file 'occupations.csv' does not exist in this directory"
        print "Place the file into this directory and then rerun the program using the command 'create_dict()'"
    
    s = r.split('\n')
    s.remove(s[0]) #removes legend at first position
    s.remove(s[-1]) #removes empty line at the end of the split list
    s.remove(s[-1]) #removes 'total' value
    new_s = []
    for c in s:
        new_s.append(special_split(c))
    
    occupations = []
    for c in range(0,len(new_s)):
        occupations.append(new_s[c][0])
    d['occupation'] = occupations

    chances = []
    for c in range(0,len(new_s)):
        chances.append(float(new_s[c][1]))
    d['chance'] = chances
    
    print d
    
def choose_occupation():
    choice = (int(random.random() * 998) / 10.)
    sofar = 0
    pos = -1
    while sofar < choice:
        pos += 1
        sofar += d['chance'][pos]
    result = d['occupation'][pos]
    if result[0] == '"':
        print result[1:len(result)-1]
    else:
        print result

create_dict()
print "If you would like to choose a random occupation, enter the command 'choose_occupation()'"
