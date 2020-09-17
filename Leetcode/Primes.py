'''
Write a program that takes an integer argument and returns all the rpimes between 1 and that integer.
For example, if hte input is 18, you should return <2,3,5,7,11,13,17>.
'''
from math import sqrt

# Method name Sieve of Eratosthenes
def ComputePrimes(N: int) -> [int]:
    # N inclusive
    ProbablePrimes = [True] * (N+1)
    answer = []
    for no in range(2,N+1):
        if ProbablePrimes[no] == True:
            answer.append(no)
            for i in range(no*2, N+1, no):
                ProbablePrimes[i] = False
    
    return answer

if __name__ == "__main__":
    print(ComputePrimes(100))
