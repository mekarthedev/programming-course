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

# Defining a function.
# The function is like any other operation. A function may have arguments.
# Argument is a variable that getsf a value when the function is called.
def myPrint(text):
    print "my: " + text

myPrint("xxxxx")

# Like any other operation the function returns a value.
# The 'return' operator is used to return a value from the function.
def add1(number):
    number = number * 10
    return number + 1

# The value returned by a function may be passed to any other operation as an argument.
print add1(4)

# Problem: reverse the order of digits in a number
number = 123987
def reverse(number):
    reverseNumber = 0
    while number != 0:
        digit = number % 10
        number = number / 10
        reverseNumber = reverseNumber *  10 + digit
    return reverseNumber

# When designing a function a test for that function should be written first.
# The test should analyze the result of a function call and tell if the result is wrong.
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

# Problem: print each digit of a number.
def printNumberDigits(number):
    while number !=0:
        digit = number % 10
        number = number / 10
        print digit 
printNumberDigits(234)

print "---"

# You may use other functions as components for your own functions.
# Problem: print each digitn of a number starting form the most significant digit.
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

# The function may have multiple arguments.
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

# Problem: find index of a specific digit in a number.
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

# Problem: count number of digits in a number.
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

# The test function should check the arguments for some condition.
# There are many test functions: equal, greater than, non-null, etc.
def testEqual(actualResult, expectedResult):
   if actualResult == expectedResult:
      print "passed"
   else:
      print "failed, expected " + str(expectedResult) + ", returned " + str(actualResult)
      
testEqual(countDigits(123456), 6)

print "---"

# Problem: return digit at the specified index.
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
# If the index is invalid the function should return None.
testEqual(digitAtIndex(154326, 8), None)

print "---"

# Problem: count number of occurences of a digit in a number.
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

# Problem: calculate sum of numbers in a range.
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

# This is a function declaration.
# This is the same as making a variable by assignment.
# The function is also a value. The function name is a variable that holds the function value.
def add1(number):
   return number + 1

print add1

# As any other value the function value may be passed as an argument to some other function.
def callFunc(function, param):
   return function(param)

print callFunc(add1, 42)
