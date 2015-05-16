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

print "---"

def multiplyString(string, number):
    n = 0
    accumulator = ""
    while n < number:
        accumulator = accumulator + string
        n = n + 1
    return accumulator

testEqual(multiplyString("a", 3), "aaa")

# Problem: print one 'fir-tree' level.

def makeTreeLevel(spaceNumber, symbolNumber, symbol):
    return multiplyString(" ", spaceNumber) + multiplyString(symbol, symbolNumber)

testEqual(makeTreeLevel(4, 3, "^"), "    ^^^")

# Problem: print full 'fir-tree' with a symbol.

def printFirTree(symbol, level):
    n = 0
    symbolNumber = 1
    spaceNumber = level - 1
    while n < level:
        print makeTreeLevel(spaceNumber, symbolNumber, symbol)
        spaceNumber = spaceNumber - 1
        symbolNumber = symbolNumber + 2
        n = n + 1

level = 20
print multiplyString(" ", level - 1) + "*"
printFirTree("^", level)

print "---"

# Problem: evaluate a simple math expression "2+2"

def calculate(number1, number2, operator):
    if operator == "+":
        result = number1 + number2
    elif operator == "*":
        result = number1 * number2
    else:
        result = None
    return result

testEqual(calculate(2, 3, "*"), 6)

def parse(expression):
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
    return number1, number2, operator

testEqual(parse("2*3"), (2, 3, "*"))

def evaluate(expression):
    number1, number2, operator = parse(expression)
    return calculate(number1, number2, operator)

testEqual(evaluate("2*3"), 6)

print "------"

def symbolIsLetter(symbol):
    return ord("a") <= ord(symbol) <= ord("z") or ord("A") <= ord(symbol) <= ord("Z")

testEqual(symbolIsLetter("a"), True)
testEqual(symbolIsLetter("1"), False)

# Problem: count number of words in a string. Word is a sequence of letters.
# Usually when building a parsing algorithm
# it's convinient to use special End-Of-String character.

def countWords(string):
    index = 0
    lettersInWord = 0
    wordsNumber = 0
    while index <= len(string):
        if index == len(string):
            character = None
        else:
            character = string[index]
        
        if character != None and symbolIsLetter(character):
            lettersInWord = lettersInWord + 1
            
        else:
            if lettersInWord != 0:
                wordsNumber = wordsNumber + 1
            lettersInWord = 0

        index = index + 1
        
    return wordsNumber

testEqual(countWords("Word is a sequence of letters"), 6)

print "---"

# Problem: check that braces are paired correctly.

def checkBraces(string):
    index = 0
    bracesNumber = 0
    while index < len(string) and bracesNumber >= 0:
        character = string[index]
        if character == "(":
            bracesNumber = bracesNumber + 1
        elif character == ")":
            bracesNumber = bracesNumber - 1
            
        index = index + 1
        
    return bracesNumber == 0


testEqual(checkBraces("(2+3)*(3+(4-1))"), True)
testEqual(checkBraces("(2+3)*(3+(4-1)"), False)
testEqual(checkBraces(")2+3))*((3+4-1)"), False)
