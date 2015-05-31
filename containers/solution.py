#!/usr/bin/python

def testEqual(actualResult, expectedResult):
   if actualResult == expectedResult:
      print "passed"
   else:
      print "failed, expected " + str(expectedResult) + ", returned " + str(actualResult)

# Container is an object that 'contains' other objects.
# It's just a box for other values.
#
# A basic container allows to iterate over its contents.
# The two basic functions to iterate are: getItem, getSize
# getItem allows to get one of the contained objects by
# identifying with some sort of a key, e.g. with an index.
# getSize allows to get averall number of objects contained in the container.

# Problem: Implement getItem and getSize assuming
# a number is a container of digits.
def getDigit(number, digitIndex):
    n = 0
    while number != 0:
        digit = number % 10
        number = number / 10
        if n == digitIndex:
            return digit
        n = n + 1

testEqual(getDigit(3456, 0), 6)
testEqual(getDigit(3456, 1), 5)

def countDigits(number):
    n = 0
    while number != 0:
        digit = number % 10
        number = number / 10
        n = n + 1
    return n

testEqual(countDigits(3456), 4)

print "---"

# Container allows different operations over its contents:
# sorting, filtering, searching, etc.
# In common case the operation is abstract and may work with any container type.
# Everythin the operation should know is how to iterate over the container.

# Problem: find maximum value in a container of integers.
# The algorithm should know nothing about the container internal structure.
# Use this operation to get maximum digit in a number
# and maximum number in a list.

def getMax(container, getItem, getSize):
    n = 0
    maxNumber = 0
    while n < getSize(container):
        if maxNumber < getItem(container, n):
            maxNumber = getItem(container, n)
        n = n + 1
    return maxNumber


testEqual(getMax(34567811, getDigit, countDigits), 8)

# List is a container, a linear ordered sequence of objects.
# You may use special []-syntax to access list items by index.
def getNumber(container, index):
    return container[index]

testEqual(getMax([42, 1989, 2015, 33], getNumber, len), 2015)


print "---"

# Problem: make a dictionary interface based on a list.

# 1. create dictionary
# 2. insert entry
# 3. find entry by key

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


dictionary = createDictionary()

insertEntry(dictionary, "apple", "fruit")
testEqual(getEntry(dictionary, "apple"), "fruit")

insertEntry(dictionary, "apple", "non-vegetable")
testEqual(getEntry(dictionary, "apple"), "non-vegetable")

insertEntry(dictionary, "tomato", "vegetable")
testEqual(getEntry(dictionary, "tomato"), "vegetable")

testEqual(getEntry(dictionary, "orange"), None)

d = createDictionary()
insertEntry(d, 42, "fourty two")
insertEntry(d, 9, "nine")
insertEntry(d, 1, "one")

def printHello():
    print "Hello!"

def printGoodBye():
    print "Good bye!"

insertEntry(d, "bye", printGoodBye)
insertEntry(d, "hello", printHello)

doSomething = getEntry(d, "hello")
doSomething()
