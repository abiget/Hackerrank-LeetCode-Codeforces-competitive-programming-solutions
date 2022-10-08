#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    grades_update = []
    for grade in grades:
        if grade < 38:
            grades_update.append(grade)
        else:
            # next multiple of 5
            for i in range(grade, 101):
                if i%5 ==0:
                    if i-grade < 3:
                        grades_update.append(i)
                    else:
                        grades_update.append(grade)
                    break
    return grades_update                 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
