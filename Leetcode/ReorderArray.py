'''
Question: Input is an array of integers, nad you have to reorder its entries so that the even entries appear first.
'''
import copy

def swap(integerArray, posA, posB):
    temp = integerArray[posA]
    integerArray[posA] = integerArray[posB]
    integerArray[posB] = temp

def reorder(integerArray):
    start = 0
    end = len(integerArray)-1
    while start < end:
        if integerArray[start] % 2 == 0:
            start += 1
        else:
            swap(integerArray, start, end)
            end -= 1
    

if __name__ == "__main__":
    integerArray = [0,7,5,4,1,2,8,3]
    print(reorder(integerArray))   