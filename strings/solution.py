#!/usr/bin/python

s = "asdf"
s2 = s + "123"
print s2

def tree(floorNumber, symbol):
    n = 1
    floor = ""
    while n <= floorNumber:
        floor = floor + symbol
        print floor
        n = n + 1


tree(10, "3")


def testEqual(actualResult, expectedResult):
   if actualResult == expectedResult:
      print "passed"
   else:
      print "failed, expected " + str(expectedResult) + ", returned " + str(actualResult)

print "---"

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
