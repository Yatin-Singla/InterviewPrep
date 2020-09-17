'''
Wrote a method to replace all spaces in a string with '%20'.
you may assume that the string has sufficient space at the end to hold the additional characters.
and you are givent the true length of the string.
'''

def URLify(A: str, length: int):
    strEnd = len(A) -1
    Alist = [item for item in A]
    for index in reversed(range(length)):
        if A[index] != ' ':
            Alist[strEnd] = A[index]
            strEnd -= 1
        else:
            Alist[strEnd-2:strEnd+1] = "%20"
            strEnd -= 3

    return ''.join(Alist)

if __name__ == "__main__":
    print(URLify("Mr John Smith    ", 13))