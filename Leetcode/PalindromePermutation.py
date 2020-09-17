'''
give a string, write a functino to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
'''

#solution 1
#       O(n)        O(n)
def PalindromePermutation(A: str):
    B = A.casefold()
    hashtable = {}
    countOdd = 0
    for char in A:
        if char in hashtable:
            hashtable[char] += 1
        else:
            hashtable[char] = 1
    
    if len(A) % 2 == 0:
        for key,value in hashtable.items():
            if value % 2 == 1:
                return False
    else: # length is odd
        for key, value in hashtable.items():
            if value % 2 == 1:
                countOdd += 1
        if countOdd > 1:
            return False

    return True

if __name__ == "__main__":
    print(PalindromePermutation("tactcoapapa"))