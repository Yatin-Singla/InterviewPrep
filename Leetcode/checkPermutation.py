'''
Give two string, write a method to decide if one is a permutation of the other
'''

#assuming input string is only characters
# O(n)            O(n)
def isPermutation(A, B):
    lenA = len(A)
    lenB = len(B)
    A = A.casefold()
    B = B.casefold()
    A.strip(' ')
    B.strip(' ')
    if lenA != lenB:
        return False

    hashTable = {}
    #add all characters
    for char in A:
        if char not in hashTable:
            hashTable[char] = 1
        else:
            hashTable[char] += 1

    #substract all characters
    for char in B:
        if char not in hashTable:
            return False
        else:
            hashTable[char] -= 1
    
    #check if all values == 0

    for char in A:
        if hashTable[char] != 0:
            return False

    return True
        
# other solutions 
# 1) sorting O(nlog(n))
# 2) again missed the use of character array of 128 characters.

if __name__ == "__main__":
    A = "ratta"
    B = "taar"
    print(isPermutation(A,B))