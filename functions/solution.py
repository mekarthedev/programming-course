#!/usr/bin/python

number = 123987
reverseNumber = 0

while number != 0:
   digit = number % 10
   number = number / 10
   reverseNumber = reverseNumber *  10 + digit

while reverseNumber !=0:
       digit = reverseNumber % 10
       reverseNumber = reverseNumber / 10
       print digit 


def myPrint(text):
    print "my: " + text

myPrint("xxxxx")

def add1(number):
    number = number * 10
    return number + 1
    
print add1(4)

number = 123987

def reverse(number):
    reverseNumber = 0
    while number != 0:
        digit = number % 10
        number = number / 10
        reverseNumber = reverseNumber *  10 + digit
    return reverseNumber

result = reverse(123987)
if result == 789321:
    print "It works!!!"
else:
    print "Wrong result: " + str(result)

result = reverse(123)
if result == 321:
    print "It works!!!"
else:
    print "Wrong result: " + str(result)

def printNumberDigits(number):
    while number !=0:
        digit = number % 10
        number = number / 10
        print digit 
printNumberDigits(234)

print "---"
    
def printDigitsFromMostSignificant(number):
    number = reverse(number)
    printNumberDigits(number)
    
printDigitsFromMostSignificant(3445986)

#

def returnNumber(number):
   return number

result = returnNumber(42)
if result == 42:
   print "passed"
else:
   print "Failed: returned " + str(result) + ", expected " + str(42)

#
def summ(number1, number2):
   print number1 + number2
   return number1 + number2

summ(54, 1)


number1 = 2
number2 = 34
result = summ(2, 34)
if result == 36:
   print "passed"
else:
   print "failed: returned " + str(result) + ", expected " + str(36)

#
print "---"

def indexOfDigit(number, digitToFind):
   number = reverse(number)
   foundIndex = None
   index =  0
   while number != 0:
      digit = number % 10
      number = number / 10
      if digit == digitToFind:
         foundIndex = index
         break
      index = index + 1
   print foundIndex
   return foundIndex

result = indexOfDigit(5678, 7)
if result == 2:
   print "passed"
else:
   print "failed: returned " + str(result) + ", expected " + str(2)

result = indexOfDigit(5678, 3)
if result == None:
   print "passed"
else:
   print "failed: returned " + str(result) + ", expected " + str(None)

print "---"

def countDigits(number):
   count = 0
   while number != 0:
      digit = number % 10
      number = number / 10
      count = count + 1
   return count
   
print countDigits(2345678)

result = countDigits(34567)
if result == 5:
   print "passed"
else:
   print "failed, returned " + str(result) + ", expected " + str(5)

print "---"

def testEqual(actualResult, expectedResult):
   if actualResult == expectedResult:
      print "passed"
   else:
      print "failed, expected " + str(expectedResult) + ", returned " + str(actualResult)
      
testEqual(countDigits(123456), 6)

print "---"

def digitAtIndex(number, digitIndex):
   number = reverse(number)
   index = 0
   while number != 0:
      digit =  number % 10
      number = number / 10
      if index == digitIndex:
         return digit
      index = index + 1

testEqual(digitAtIndex(154326, 3), 3)
testEqual(digitAtIndex(154326, 8), None)

print "---"

def digitsInNumber(number, digitToCount):
   count =  0
   while number != 0:
      digit = number %10
      number = number / 10
      if digit == digitToCount:
         count = count + 1
   return count


testEqual(digitsInNumber(3454478, 4), 3)

print "---"

def rangeSumm(firstNumber, lastNumber):
   number = firstNumber
   sum = 0
   while number <= lastNumber:
      sum = sum + number
      number = number + 1
   return sum

print rangeSumm(1234, 2000)
testEqual(rangeSumm(5, 8), 26)

print "---"

def add1(number):
   return number + 1

print add1

def callFunc(function, param):
   return function(param)

print callFunc(add1, 42)
