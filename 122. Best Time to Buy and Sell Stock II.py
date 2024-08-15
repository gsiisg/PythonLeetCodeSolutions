class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought_price = 0

        length = len(prices)

        if length < 2:
            return 0
            
        profit = 0

        bought_price = None
        if prices[0]<prices[1]:
            bought_price = prices[0]

        for i in range(1,len(prices)-1):

            # peak->sell
            if (bought_price is not None) and (prices[i-1]<=prices[i]>prices[i+1]) :
                # profit += prices[i] - bought_price
                # bought_price = 0
                # print(f'selling at {prices[i]}, profit at {profit}')
                profit += prices[i] - bought_price
                bought_price = None
            # trough->buy
            elif (bought_price is None) and (prices[i-1]>=prices[i]<prices[i+1]) :
                # profit -= prices[i]
                # bought_price = prices[i]
                # print(f'buying at {prices[i]}, profit at {profit}')
                bought_price = prices[i]

            # print(f' index {i} prices {prices[i]} {bought_price} {profit}')
        
        # if prices were increasing, sell
        if (bought_price is not None) and (prices[-2]<=prices[-1]):
            profit += prices[-1] - bought_price

        # if not sold at end put it back to profit as if never bought
        elif bought_price:
            profit += bought_price

        # print(bought_price, profit)
        return profit