'''
Implement an algorith to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''

# Time Complexity               Space Complexity
#   O(n^2)                          O(1)
def LoopUnique(A: str):
    length = len(A)
    for i in range(length):
        j = i+1
        while j < length:
            if A[j] == A[i]:
                return False
            j += 1

    return True

#   O(n)                            O(n)
def HashUnique(A: str):
    hashtable = {}
    for item in A:
        if item in hashtable:
            return False
        else:
            hashtable[item] = 1

    return True

# Note if len of array > 128 then it has repeating characters
# Other solutions include:
# 1) sorting O(nlog(n))
# 2) creating a flag array of size 128 to indicate a value at index i => char i has already been noticed. O(n) & O(1) and we could
#aregue that the time complexity is O(1) as it loops around only once over 128 characters.

if __name__ == "__main__":
    print(LoopUnique("hi how are you doing?"))