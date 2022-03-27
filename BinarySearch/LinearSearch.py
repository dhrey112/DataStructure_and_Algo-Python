"""
Worst case O(n)
"""


def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False
