#!/usr/bin/python

def testEqual(actualResult, expectedResult):
   if actualResult == expectedResult:
      print "passed"
   else:
      print "failed, expected " + str(expectedResult) + ", returned " + str(actualResult)

###

# Problem: ask the user to guess password until he enters the correct one.

def guessPassword():
    password = "qwerty123"
    value = None
    while value != password:
        value = raw_input("enter password: ")
        print "incorrect pasword"
    print "correct pasword"

print "---"

# Problem: make an interactive menu.

# 1. Print "Hello"
# 2. Exit
# Your choice: 1
# Hello
# Your choice: 2
#

def helloMenu():
    choice = None
    while True:
        print "1. Print \"Hello\"\n2. Greet me\n3. Exit"
        choice = raw_input("Your choice: ")
        if choice == "1":
            print "Hello"
        elif choice == "2":
            name = raw_input("Enter your name: ")
            print "Greetings, " + name + "!"
        elif choice == "3":
            print "Exit"
            break
        else:
            print "incorrect choice"
