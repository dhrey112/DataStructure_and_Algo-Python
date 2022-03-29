# Approach 1: Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(1)

def is_permutation_1(str1, str2):
    str1 = ''.join(sorted(str1.lower()))
    str2 = ''.join(sorted(str2.lower()))

    if len(str1) != len(str2):
        return False

    chars = len(str1)

    for char in range(chars):
        if str1[char] != str2[char]:
            return False
    return True


def is_permutation_2(str1, str2):
    str1 = ''.join(sorted(str1.lower()))
    str2 = ''.join(sorted(str2.lower()))

    if len(str1) != len(str2):
        return False

    str_dict = {}

    for char in str1:
        if char in str_dict:
            str_dict[char] += 1
        else:
            str_dict[char] = 1

    for char in str2:
        if char in str_dict:
            str_dict[char] -= 1
        else:
            return False

    return all(value == 0 for value in str_dict.values())


is_perm_1 = "google"
is_perm_2 = "ooggle"

not_permutation_1 = "not"
not_permutation_2 = "top"

print(is_permutation_1(is_perm_1, is_perm_2))
print(is_permutation_1(not_permutation_1, not_permutation_2))

print(is_permutation_2(is_perm_1, is_perm_2))
print(is_permutation_2(not_permutation_1, not_permutation_2))
