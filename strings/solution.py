#!/usr/bin/python

# The string is a value.
s = "asdf"
# The '+' operator for strings is a concatenation operator.
s2 = s + "123"
print s2

# Problem: print half 'fir-tree' with a symbol.
def tree(floorNumber, symbol):
    n = 1
    floor = ""
    while n <= floorNumber:
        floor = floor + symbol
        print floor
        n = n + 1

tree(10, "^")

print "---"

def testEqual(actualResult, expectedResult):
   if actualResult == expectedResult:
      print "passed"
   else:
      print "failed, expected " + str(expectedResult) + ", returned " + str(actualResult)

# Problem: Convert number to string.
def stringFromNumber(number):
    if number == 0:
        string = str(number)
    else:
        string = ""
        while number != 0:
            digit = number % 10
            number = number / 10
            string = str(digit) + string
    return string

testEqual(stringFromNumber(234), "234")
testEqual(stringFromNumber(0), "0")

print "---"

# Problem: join list of numbers with a string
def joinNumbers(firstNumber, lastNumber, separator):
    number = firstNumber
    string = ""
    while number <= lastNumber:
        string = string + str(number)
        if number != lastNumber:
            string = string + separator
        number = number + 1
    return string


testEqual(joinNumbers(5, 8, ", "), "5, 6, 7, 8")
testEqual(joinNumbers(5, 8, "-"), "5-6-7-8")
