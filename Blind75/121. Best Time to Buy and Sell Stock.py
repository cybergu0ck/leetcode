class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0  #left point indicates index of buy value 
        
        for r in range(1, len(prices)):  #right pointer is indicative of index of sell value
            if prices[r] < prices[l]:
                l = r       #if sell value is less than buy value, then that sell is the new buy
            profit = max(profit, prices[r] - prices[l])
        
        return profit
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    