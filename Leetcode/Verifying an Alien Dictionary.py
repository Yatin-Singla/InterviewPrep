# class Solution:
# def isLexicographically(self, arg1, arg2, dictionary):
#     if arg1 == arg2:
#         return True
#     Larg1 = len(arg1)
#     Larg2 = len(arg2)

#     if Larg1 <= Larg2:
#         if arg1 == arg2[:Larg1]:
#             return true
#         else:
#             for i in range(Larg1):
#                 if dictionary[arg1[i]] > dictionary[arg2[i]]:
#                     return False
#                 elif dictionary[arg1[i]] < dictionary[arg2[i]]:
#                     return True

#     elif Larg2 < Larg1:
#         if arg2 == arg1[:Larg2]:
#             return False
#         else:
#             for i in range(Larg2):
#                 if dictionary[arg1[i]] > dictionary[arg2[i]]:
#                     return False
#                 elif dictionary[arg1[i]] < dictionary[arg2[i]]:
#                     return True

#     return True

# def isAlienSorted(self, words, order):
#     Dictionary = {}
#     value = 1
#     for key in order:
#         Dictionary[key] = value
#         value += 1
#     Lwords = len(words)
#     for i in range(Lwords -1):
#         if not self.isLexicographically(words[i], words[i+1], Dictionary):
#             return False

#     return True

class Solution:
    def compare(self, a, b, dictionary):
        i = 0
        while i < len(a) and i < len(b):
            if dictionary[a[i]] < dictionary[b[i]]:
                return True
            elif dictionary[b[i]] < dictionary[a[i]]:
                return False
            else:
                i += 1
        if i >= len(b) and i < len(a):
            return False
        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {order[i]: i for i in range(len(order))}
        for i in range(len(words)-1):
            if not self.compare(words[i], words[i+1], dictionary):
                return False

        return True


if __name__ == "__main__":
    soln = Solution()
    print(soln.isAlienSorted(
        ["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
