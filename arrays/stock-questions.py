# class Solution(object):
def maxProfit(prices):
        # can't buy before selling 
        # you want to buy when max diff of [indx+1]-[indx]
        empty = []
        
        for i in range(0,len(prices)-1): #6 length -> 0-5
            diff = prices[i+1] - prices[i]
            empty.append(diff)
        return empty

b = [7, 1, 5, 3, 6, 4]
    
# a = Solution()
print(maxProfit(b))

