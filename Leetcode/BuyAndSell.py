'''
Write a program that takes an array denoting the daily stock price, 
and returns the maximum profit that could be made by buying and then selling one share of the at stock.
There is no need to buy if no profit is possible.
'''

def BuyandSell(A):
    if len(A) < 2:
        return -1

    profit = 0
    tempSum = 0
    for index in range(1, len(A)):
        difference = A[index] - A[index - 1]
        if difference + tempSum > profit:
            profit = tempSum + difference
            tempSum = difference
        elif tempSum+difference <= 0:
            tempSum = 0
        else:
            tempSum = difference+tempSum
    return profit

# iterate through prices, keeping track of the minimym element m seen thus far.
# If the difference of the current element and m is greater thant the max profit recorder so far,
# update the max profit.
def BuyandSellSimple(prices):
    minPricesoFar, Profit = prices[0], 0
    for price in prices:
        ProfitToday = price - minPricesoFar
        Profit = max(ProfitToday, Profit)
        minPricesoFar = min(price, minPricesoFar)
    return Profit

if __name__ == "__main__":
    A = [310,315,275,295,260,270,290,235,255,250]
    B = [310,310,275,275,260,260,260,230,230,230]
    print(BuyandSell(B))