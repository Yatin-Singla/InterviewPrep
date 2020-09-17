"""
Write a program tha takes two arrays representing integers, adn returns an integer representing their product.
"""


def Multiply(A, B):
    # sign = -1 if ((A[0] > 0 and B[0] < 0) or (A[0] < 0 and B[0] > 0)) else 1
    # ? I have no idea what kind of ^ operator is this, what if both are false?
    sign = -1 if (A[0] < 0) ^ (B[0] < 0) else 1
    A[0], B[0] = abs(A[0]), abs(B[0])

    result = [0] * (len(A) + len(B))
    for j in reversed(range(len(B))):
        for i in reversed(range(len(A))):
            result[i + j + 1] += A[i] * B[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] = result[i + j + 1] % 10

    curr = 0
    while result[curr] == 0:
        curr += 1

    A[curr] *= sign
    return A[curr:]
