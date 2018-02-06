'''This short program is intended to find 'e' with as many decimals
as your input number (this number will have a limitation)'''
from __future__ import division
import math
while True:

    decimals = int(raw_input('Please enter a decimals number between 1 - 30:'))
    e = '2.718281828459045235360287471352'
    if decimals >= 1 and decimals <= 30:
        print e[0:(decimals+2)]
        break
    else:
        print "Your input number is not between 1 and 30 as requested! \
 Please try again."
