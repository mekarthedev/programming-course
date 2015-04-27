#!/usr/bin/python

# Variables are named values.
message = "xyz"
text = message
number = 123

# Instructions are executed one by one.
print text
print message
print number + 1
print message + " " + "abc"

# Problem: switch values.
a = 123
b = 456
c = 0

c = a
a = b
b = c

print a
print b

# String and Integer are different types. Value of a type may be casted to a different type.
# An operation on an argument returns a value of some type.
# An operation may have different meaning depending on argument type.
print str(a) + ", " + str(b)
print 123 + 456

# A variable of the boolean type can have only one of two values: True or False.
# The 'if' statement is an operation that accepts a boolean value.
# There are operations that return a boolean value.
# Indentation is used to form a group of instructions.
rate = 1
if rate == 5:
    print "great"
if rate == 4:
    print "good"
if rate == 3:
    print "OK"
if rate == 2:
    print "bad"
if rate == 1:
    print "awful"

print "after if"

# The 'while' statement is an operation that accepts a boolean value.
# Cycle is a sequence of instructions that may be repeated multiple times in a row until some condition is met.
# A 'good' operation doesn't modify its arguments. It only returns a new calculated value instead.
# Problem: print numbers from N through 0.
count = 5
while count != 0:
    count = count - 1
    print count

# Dividing by 10 may be used to get a 10-base digit of a number.
number = 123456
print number / 10
print number % 10

# Problem: print each digit of a number one per a line.
# Designing a cycle consists of two parts: designing the repeat condition and designing the iteration.
# In general, the efficient way is to design each part separately and independently.
# An iteration has an input and an output. The output of the previous iteration is the input for the next interation.
# When designing the interation the goal is to determine the input/output.
# When designing the repeat condition the goal is to determine a condition when the input requires another iteration.
number = 1357924680
while number != 0:
    digit = number % 10
    number = number / 10
    print digit

# Problem: count digits in a number.
number = 34678
count = 0
while number != 0:
    number = number / 10
    count = count + 1
print count

# Problem: print some string N times.
text = "xyz"
count = 0
while count != 1:
    count = count + 1
    print text

# Problem: count number of odd digits in a number.
number = 34678111112
count = 0
while number != 0:
    digit = number % 10
    number = number / 10
    if digit % 2 != 0:
        count = count + 1
print count
