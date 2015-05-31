#!/usr/bin/python

def testEqual(actualResult, expectedResult):
   if actualResult == expectedResult:
      print "passed"
   else:
      print "failed, expected " + str(expectedResult) + ", returned " + str(actualResult)

###

# Problem: implement phone book.

# Components, decomposition, interfaces, abstraction, divide & conquer.
# Computer-world objects, complex structures, lists, indexing.
# Positive and negative scenarios, correlation of easiness to understand with proper decomposition.
# Application main loop.

# Dictionary as the storage.

def createDictionary():
    return []

def insertEntry(dictionary, key, value):
    index = 0
    existingIndex = None
    while index < len(dictionary):
        if dictionary[index] == key:
            existingIndex = index
            break
        index = index + 1
        
    if existingIndex == None:
        dictionary.append(key)
        dictionary.append(value)
    else:
        dictionary[existingIndex+1] = value

def getEntry(dictionary, key):
    index = 0
    value = None
    while index < len(dictionary):
        if dictionary[index] == key:
           value = dictionary[index+1]
           break
        index = index + 2

    return value

# Prompting user input and input validation.

def promptData(promptMessage, dataIsValid):
   while True:
      data = raw_input(promptMessage)
      if dataIsValid(data):
         break
      else:
         print ("Wrong data")
         
   return data

def dataIsNotEmpty(data):
   return data != ""

# Prompting for concreet meaningful data: name & phone.

def promptName():
   return promptData("Enter name: ", dataIsNotEmpty)

def promptPhoneNumber():
   return promptData("Enter phone number: ", dataIsNotEmpty)

# User stories.

def interactToRegisterPerson():
   registerPerson(promptName(), promptPhoneNumber())

def interactToFindPhoneNumber():
   number = findPhoneNumber(promptName())
   if number != None:
      print "Phone number: " + number
   else:
      print "Can't find the name"

# Phone book model & database.

storage = createDictionary()
        
def registerPerson(name, number):
    insertEntry(storage, name, number)

def findPhoneNumber(name):
    return getEntry(storage, name)


registerPerson("xxx", "123")
testEqual(findPhoneNumber("xxx"), "123")

print "---"

# Menu UI framework.

def exitMenu():
   return True

def printMenu(menu):
   number = 1
   index = 0
   while index < len(menu):
      print str(number) + "." + menu[index]
      number = number + 1
      index = index + 2

def selectMenuItem(menu):
   while True:
      choiceText = raw_input("Your choice: ")
      isValid = False
      if choiceText.isdigit():  
         choiceNumber = int(choiceText)
         if 0 < choiceNumber <= len(menu)/2:
            isValid = True
      
      if isValid:
         break
      else:
         print "Wrong choice"
   return choiceNumber

def performMenuAction(itemNumber, menu):
   index = (itemNumber-1)*2 + 1
   action = menu[index]
   return action()

def runInteractiveLoop(menu):
   shouldStop = False
   while not shouldStop:
        printMenu(menu)
        itemNumber = selectMenuItem(menu)
        shouldStop = performMenuAction(itemNumber, menu)

# The phone book application.

phonebookMenu = [
   "Register a person", interactToRegisterPerson,
   "Find a person", interactToFindPhoneNumber,
   "Exit", exitMenu
]

runInteractiveLoop(phonebookMenu)
