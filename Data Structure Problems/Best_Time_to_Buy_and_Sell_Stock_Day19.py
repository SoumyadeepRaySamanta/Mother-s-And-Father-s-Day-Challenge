class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price to a very large value
        min_price = float('inf')
        
        # Initialize the maximum profit to 0
        max_profit = 0
        
        # Iterate over each price in the list
        for price in prices:
            # If the current price is less than the minimum price seen so far,
            # update the minimum price
            if price < min_price:
                min_price = price
            # Otherwise, check if selling at the current price yields a higher profit
            # than the maximum profit seen so far
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        # Return the maximum profit found
        return max_profit