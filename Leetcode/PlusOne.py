'''
Given an array of digits encoding a nonengative decimal integer D and updates the array to represent the integer D+1.
eg if the input is <1,2,9> then uou should update the array to <1,3,0>
'''

#complicated Approach
#   O(n)            O(n)
def PlusOne(arr):
    additant = [1]
    for index in range(abs(len(arr) - len(additant))):
        additant.append(0)
    additant.reverse()
    result = []
    summation, carry = 0,0
    for index in reversed(range(len(arr))):
        summation = additant[index] + arr[index] + carry
        result.append(summation%10)
        carry = summation // 10
    
    if carry:
        result.append(carry)

    return result[::-1]        

def PlusOneSimple(number):
    number[-1] += 1
    
    for i in reversed(range(1,len(number))):
        if number[i] != 10:
            break
        #else number[i] == 0
        number[i] = 0
        number[i-1] += 1

    if number[0] == 10:
        number[0] = 1
        number.append(0)
    
    return number

if __name__ == "__main__":
    print(PlusOneSimple([9,9,8]))