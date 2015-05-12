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

def enumerate(count, processNumber):
   i = 0
   while i < count:
      processNumber(i)
      i = i + 1

def printNumber(number):
   print number

enumerate(5, printNumber)

print "---"

def fromNumberToNumber(firstNumber, lastNumber, processNumber):
   n = firstNumber
   while n <= lastNumber:
      processNumber(n)
      n = n + 1

fromNumberToNumber(2, 5, printNumber)

print "---"

def reduce(firstNumber, lastNumber, calculate):
   number = firstNumber
   accumulator = 0
   while number <= lastNumber:
      accumulator = calculate(accumulator, number)
      number = number + 1
   return accumulator

def add(number1, number2):
   summ = number1 + number2
   return summ

testEqual(add(1, 2), 3)
testEqual(reduce(1, 3, add), 6)

print "1---"

def parse2(expression, onParsed):
    size = len(expression)
    index = 0
    operator = " "
    number1 = 0
    number2 = 0
    while index < size:
        if 47 < ord(expression[index]) and ord(expression[index]) < 58:
            character = int(expression[index])
            if operator == " ":
                number1 = number1 * 10 + character
            else:
                number2 = number2 * 10 + character
        else:
            operator = expression[index]
        index = index + 1
    onParsed(number1, number2, operator)

onParsedWasCalled = False
returnedNumber1 = 0
returnedNumber2 = 0
returnedOperator = ""
def onParsedTest(number1, number2, operator):
    global onParsedWasCalled
    global returnedNumber1
    global returnedNumber2
    global returnedOperator
    onParsedWasCalled = True
    returnedNumber1 = number1
    returnedNumber2 = number2
    returnedOperator = operator

    

parse2("2*3", onParsedTest)

if onParsedWasCalled and returnedNumber1 == 2 and returnedNumber2 == 3 and returnedOperator == "*":
    print "works"
else:
    print "failed"



    
print "---"

funcWasCalled = False
def func(a, b, c, d):
    global funcWasCalled
    funcWasCalled = True

def callFunc():
    func(1, 2, 3, 4)

callFunc()
if funcWasCalled:
    print "passed"
else:
    print "failed"
    

testEqual(evaluate("2+2"), 4)
testEqual(evaluate("2*3"), 6)
testEqual(evaluate("22-10"), None)


print "2---"

def f2():
    print "f2"

def f1(f):
    print "f1 started"
    f()
    print "f1 finished"

f1(f2)

def parseTokens(expression, onNumber, onOperator):
    index = 0
    number = 0
    operator = ""
    while index < len(expression):
        character = expression[index]
        print "character == " + character
        isDigit = 47 < ord(character) < 58
        print "isDigit == " + str(isDigit)
        if isDigit:
            if operator == "":
                number = number*10 + int(character)
                print "added digit. number == " + str(number)
            else:
                print "operator == " + operator
                onOperator(operator)
                operator = ""
                number = int(character)  
        else:
            if number != 0:
                print "number == " + str(number)
                onNumber(number)
                number = 0
                operator = character
            else:
                operator = operator + character
               
        index = index + 1
    if operator == "":
        onNumber(number)
    else:
        onOperator(operator)




onNumberWasCalled = False
onNumberTestArgument1 = None
onNumberTestArgument2 = None

def onNumberTest(number):
    global onNumberWasCalled
    global onNumberTestArgument1
    global onNumberTestArgument2
    onNumberWasCalled = True
    print "onNumberTestArgument1 == " + str(onNumberTestArgument1)
    if onNumberTestArgument1 == None:
         onNumberTestArgument1 = number
        
    else:
        onNumberTestArgument2 = number
        print onNumberTestArgument2
               
onOperatorWasCalled = False
onOperatorTestArgument = None
def onOperatorTest(operator):
    global onOperatorWasCalled
    global onOperatorTestArgument
    onOperatorWasCalled = True
    onOperatorTestArgument = operator

parseTokens("23+45", onNumberTest, onOperatorTest)

print onNumberTestArgument1, onNumberTestArgument2, onOperatorTestArgument
if onNumberWasCalled and onOperatorWasCalled and onNumberTestArgument1 == 23 and onNumberTestArgument2 == 45 and onOperatorTestArgument == "+":
    print "works"
else:
    print "failed"
