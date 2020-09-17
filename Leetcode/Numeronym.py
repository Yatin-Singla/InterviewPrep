# A "numeronym" is the abbreviation of a word by replacing all the middle characters with the number of characters removed. For example localization becomes l10n and internationalization becomes i18n. Write a program that takes a word and a dictionary file as input and outputs whether or not the word's numeronym is unique.


def numeronym(word: string) -> string:    
    length = len(word)
    if length <= 2:
        return word  
    return word[0] + str(length-2) + word[-1]

def isUnique(word: String, dictionaryFile) -> Bool:
    uniqueSet = set()
    for everyWord in dictionaryFile:
        uniqueSet.add(numeronym(everyWord))
        
    if numeronym(word) in uniqueSet:
        return False
    else:
        return True
    
    
 

If we allow replacing any one section of the word with the length, then given a word and a dictionary, how would you find the shortest abbreviation unique to that word?



localization => l10n, lo9n, l9on, loc8n....

# l10n
# ocalizatio => l10n, lo9n, l9on
# calizatio => lo8n, loc8n, lo9n
# ocalizati
l8ion

# localization
# (1, 11)
# (1, 10), (2, 11)
# (1, 9), (2, 10), (3, 11)
# ...

l[10]n
l[9]on
lo[9]n
lo[8]on
loc[8]n
l[8]ion