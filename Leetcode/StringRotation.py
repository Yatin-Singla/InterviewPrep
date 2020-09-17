'''
Assume you have a method isSubstring which checks if one word is a substring of another.
Five two string, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
'''

def StringRotation(s1,s2):
    s3 = s1+s1
    return isSubstring(s1,s3)