#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = number % 10
if number < 0:
    lastdig -= 10
if lastdig > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, lastdig))
elif lastdig == 0:
    print("Last digit of {} is {} and is 0"
          .format(number, lastdig))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, lastdig))
