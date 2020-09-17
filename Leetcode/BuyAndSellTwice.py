'''
Write a program that computes the maximum profit that can be made by buying and selling a share at most twice.
The second buy must be made on another date after the first sale.
'''
#returns profit and end index
def BuyAndSell(prices, StartIndex) -> (int, int):
    if StartIndex < len(prices):
        return (0,-1)
    Profit, minPriceSoFar, IndexSell = 0, prices[StartIndex], 0
    for index in range(StartIndex, len(princes)):
        ProfitToday = prices[index] - minPriceSoFar
        if ProfitToday > Profit:
            Profit = ProfitToday
            IndexSell = index
        minPriceSoFar = min(prices[index], minPriceSoFar)
    return Profit, IndexSell

def BuyAndSellTwice(prices):
    profit, SecondBuy = BuyAndSell(prices, 0)
    SecondProfit, _ = BuyAndSell(prices, SecondBuy+1)
    return profit+SecondProfit

if __name__ == "__main__":
    print(BuyAndSellTwice([12,11,13,9,12,8,14,13,15]))
