'''
Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabccccaa would become a2b1c5a3. 
If the compressed string would not become smaller than the original string,
you method should return the original string. Assume the string has only uppercase and lowercase letters.
'''

def StringCompression(charString):
    counter = 1
    result = []
    for index in range(1,len(charString)):
        if charString[index] == charString[index-1]:
            counter += 1
        else:
            # doubtful if ''.join would work on int type list
            result.extend([charString[index-1],str(counter)])
            counter = 1

    result.extend([charString[-1], str(counter)])
    return ''.join(result) if len(result) < len(charString) else charString

# more efficient solution would be where we first estimate the length the length of the compressed string
# rather than forming the string and figuring out which one to return.

if __name__ == "__main__":
    print(StringCompression("aabccccaaa"))
    
            
