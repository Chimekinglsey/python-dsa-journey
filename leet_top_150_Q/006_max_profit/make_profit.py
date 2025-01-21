from typing import List
import time
from functools import wraps
import timeit

def timer(f):
    @wraps(f)
    def executor(*args, **kwargs):
        start = time.perf_counter()
        p_start = time.process_time()
        result = f(*args, **kwargs)
        end_time = time.perf_counter()
        p_end = time.process_time()
        time_taken = end_time - start
        print(f"{f.__name__} executed in {time_taken:.6f} with result: {result} and process time {p_end - p_start}")
        return result
    
    return executor
        

class Solution:
    @timer
    def maxProfit(self, prices: List[int]) -> int:
        """We will use two pointers to keep the buy, sell points while updating max profit"""
        if len(prices) < 2:
            return 0
        
        buy, sell = 0, 1
        max_profit = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            sell += 1
        return max_profit

    @timer
    def maxProfit2(self, prices: List[int]) -> int:
        """
        Two pointers with for_loop
        """
        if len(prices) < 2:
            return 0
        max_profit, min_buy = 0, 0
        for p in range(1, len(prices)):
            if prices[p] > prices[min_buy]:
                profit = prices[p] - prices[min_buy]
                max_profit = max(max_profit, profit)
            else:
                min_buy = p
        return max_profit
    
    @timer
    def maxProfit3(self, prices: List[int]) -> int:
        """
            We will go through all the items in the and for each time determine the day with total max profit
            by maintaining the buy day
        """
        if len(prices) < 2:
            return 0
        max_profit = 0
        min_price = float('inf')
        for p in prices:
            min_price = min(min_price, p)
            profit = p - min_price
            max_profit = max(max_profit, profit)
        return max_profit
    
    @timer
    def maxProfit4(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0
        buy = prices[0]

        for price in prices:
            buy = price if price < buy else buy
            profit = price - buy
            max_profit = profit if profit > max_profit else max_profit
        return max_profit

solution = Solution()
prices = [7,1,5,3,6,4]
print(
    solution.maxProfit(prices), 
    solution.maxProfit2(prices), 
    solution.maxProfit3(prices), 
    solution.maxProfit4(prices)
    )
