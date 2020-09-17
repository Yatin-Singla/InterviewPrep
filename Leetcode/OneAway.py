'''
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character. Given two strings, 
write a function to check if they are one edit (or zero edits) away.
'''

def OneAway(A, B):
    lenA = len(A)
    lenB = len(B)
    count = 0
    if abs(lenA - lenB) > 1:
        return False

    hashtable = {}
    for char in A:
        if char in hashtable:
            hashtable[char] += 1
        else:
            hashtable[char] = 1
    for char in B:
        if char in hashtable:
            hashtable[char] -= 1
            if hashtable[char] == 0:
                hashtable.pop(char)
        else:
            hashtable[char] = 1

    for value in hashtable.values():
        count += value

    if lenA == lenB:
        if count != 2:
            return False
    else:
        if count != 1:
            return False

    return True

#cleaner solution
def OneEditAway(A, B):
    OddOneOut = False
    for index in range(len(A)):
        if A[index] != B[index]:
            if OddOneOut:
                return False
            else:
                OddOneOut = True
    return True

#first is shorter in length
def OneInsertAway(first, second):
    index1 = 0
    index2 = 0
    insert = 0
    while index1 < len(first) and index2 < len(second):
        if first[index1] != second[index2]:
            # check if more than once we have skipped or not
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1, index2 = index1 + 1, index2 + 1

    return True

def OneAwayCleaner(A, B):
    if len(A) == len(B):
        return OneEditAway(A,B)
    elif len(A) + 1 == len(B):
        return OneInsertAway(A,B)
    elif len(B) + 1 == len(A):
        return OneInsertAway(B, A)
    return False

if __name__ == "__main__":
    print(OneAway("pale","bake"))