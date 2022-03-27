# Import allows us to make use of the bisect module.
import bisect

# This sorted list will be used throughout this lesson
# to showcase the functionality of the "bisect" method.
A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
print('bisect_left()')
# -10 is at index 1
print(bisect.bisect_left(A, -10))

# First occurrence of 285 is at index 6
print(bisect.bisect_left(A, 285))

"""bisect_right()"""
# Index position to right of -10 is 2.
print('bisect_right()')
print(bisect.bisect_right(A, -10))

# Index position after last occurrence of 285 is 9.
print(bisect.bisect_right(A, 285))

"""bisect()# This function is equivalent to bisect_right and 
takes a sorted list and the target element to be searched as input parameters """
print('bisect()')
# Index position to right of -10 is 2. (Same as bisect_right)
print(bisect.bisect(A, -10))

# Index position after last occurrence of 285 is 9. (Same as bisect_right).
print(bisect.bisect(A, 285))

'''
insort_left() and insort_right
Given that the list A is sorted, it is possible to insert elements into A so that the list remains sorted.
'''
print('insort_left() and insort_right')
print(A)
bisect.insort_left(A, 108)
print(A)

bisect.insort_right(A, 108)
print(A)