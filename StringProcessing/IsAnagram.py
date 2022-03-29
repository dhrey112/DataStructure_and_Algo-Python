s1 = "fairy tales"
s2 = "rail safety"

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

# Requires n log n time (since any comparison
# based sorting algorithm requires at least
# nlogn time to sort).
print(sorted(s1) == sorted(s2))


# The Preferred Solution
# This solution is of linear time complexity which is an improvement on O(nlogn)
# O(nlogn).
def is_anagram(s1, s2):
    ht = dict()
    # normalizing the strings
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    print(s1, '  ', s2)
    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    for i in ht:
        if ht[i] != 0:
            return False
    return True


s1 = "fairy tales"
s2 = "rail safety"

print(is_anagram(s1, s2))
