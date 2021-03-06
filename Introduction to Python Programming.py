# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Variables and Multiple Assignment
print('Hello world')

age = 27
age

sentence = "my name is Anna"

Amaro, Carol, John = 31, 27, 20
Amaro

name, age = "Anna", 27

#Arithmetic Operators
age1, age2 = 10, 13
age1 + age2
age1 - age2
age1 * age2
age1 / age2

Firstname = "Anna"
Lastname = "Gomez"
Firstname + " " + Lastname

string = "Anthony was cleaning the room"
string[0:7]

#Placeholders in Strings
placeholder ="%s is becoming old"
placeholder%name

placeholder%("Beatrice")

placeholder2 = "%s is %d years old"
placeholder2%("Carol", 27)

print("Hello %s!" % name)

#Introduction to lists
shoplist = ["chesse", "bread", "chocolate", "water"]

shoplist[1]

shoplist[3]

shoplist[0:3]

shoplist.append("wine")

shoplist

shoplist.remove("water")

shoplist

shoplist[1] = "beer"

len(shoplist)

shoplist2 = ["shampoo", "cookies", "Noodles"]
shoplist2

shoplist + shoplist2

len(shoplist + shoplist2)

Numbers = [1, 12, 26, 192, 1992]
min(Numbers)
max(Numbers)

#Dictionaries
Dictionary = {"Wine":3, "Chocolate":1, "Beer":6, "cheese":24}
Dictionary

Dictionary["cheese"]

Dictionary["chocolate"]=2
Dictionary

del Dictionary["chocolate"]
Dictionary

Dictionary["Chocolate"]=2
Dictionary

Dictionary2 = {"juice":1, "apples":3, "bananas":2}
Dictionary2

Dictionary.update(Dictionary2)

Dictionary.get("cheese")

Dictionary.__init__()

New = dict(Wine = 4, grapes = 20)
New

Dictionary.update(chips = 1)
Dictionary

#Tuples
tup = ("hi", "I", "am", "bored")
tup
tup[0]

tup[0:3]

tupl = ("and", "hungy")

tupple = tup + tupl
tupple

#Conditional statements
if(3<4):
    print("You're damn right")
else:
    print("Get a doctor appointment")
    
if(3<2):
    print("You're damn right")
else:
    print("Get a doctor appointment")
    
if(Firstname == "Anna"):
    print("Hi Anna!")
elif(Firstname == "Anne"):
    print("Hi Anne!")
elif(Firstname == "Annie"):
    print("Hi Annie!")
else:
    print("Bye")

if(Firstname == "Annie"):
    print("Hi Annie!")
elif(Firstname == "Anne"):
    print("Hi Anne!")
elif(Firstname == "Ana" or Firstname == "Anna"):
    print("Hi Anna!")
else:
    print("Bye")

#For loops
for n in shoplist:
    print(n)

for k in tupple:
    print(k)

for i in range(0,5):
    print(i)

for i in range(0,5,2):
    print(i)

for i in range(1,6):
    print(i*5)

for i in range(0,51,5):
    print(i)

#While Loops
c=0

while c<5:
    print(c)
    c = c + 1
    
d=0

while d<5:
    print(d)
    if d == 3:
        break
    d = d + 1

e=0

while e<5:
    e = e + 1
    print(e)
    if e == 3:
        break
    
f=0

while f<5:
    f = f+1
    if f == 3:
        continue
    print(f)

#Try and Expect
try:
    if year < 2000:
        print("correct")
except:
    print("no data available")
    
#Hello world

"""
This is a comment
I am awesome
"""

#Functions
def myfunction():
    print("Hi babe")
    
myfunction()

def greetings(nombre):
    print("Hi " + nombre + "!")

greetings("George")

def soma(a, b):
    c = a + b
    print(c)

soma(9, 8)

def returnsoma(d, e):
    f = e + d
    return f

returnsoma(10, 15)

outputsoma = soma(9,8)
outputsoma

outputsoma2 = returnsoma(10,15)
outputsoma2

del outputsoma

#Object-Oriented Programming
class Person:
    def getName(self):
        print("Anna")
    def getAge(self):
        print(26)

p = Person()

p.getAge()
p.getName()

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print("My name is " + self.name)
    def getAge(self):
        print("My age is " + self.age)

p1 = People("Bob", "22")
p1.age
p1.name

p1.getAge()

p1.getName()

#Inheritance
class Parent:
    def __init__(self):
        print("this is the parent class")
    def parentfunc(self):
        print("this is the parent function")

p2 = Parent()

p2.parentfunc()

class Child(Parent):
    def __init__(self):
        print("this is the child class")
    def childfunc(self):
        print("this is the child function")

p3 = Child()

p3.childfunc()

p3.parentfunc()

p3.__init__()