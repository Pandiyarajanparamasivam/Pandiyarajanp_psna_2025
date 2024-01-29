import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    capitalized_name = ' '.join(word.capitalize() for word in s.split(' '))
    return capitalized_name
if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
