#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberPosi = number
if number < 0:
    numberPosi = number * -1

if (number < 0):
    last = (numberPosi % 10) * -1
else:
    last = numberPosi % 10
print(last)
if last > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".
          format(number, last))
elif (last < 0 and last < 5) or (last <= 5 and last != 0):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last))
elif last == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last))
