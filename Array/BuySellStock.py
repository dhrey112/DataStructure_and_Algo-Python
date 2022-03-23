def buy_and_sell_stock_once(prices):
    max_profits = 0
    for buy_day in range(len(prices)):
        for sell_day in range(buy_day + 1, len(prices)):
            if prices[sell_day] - prices[buy_day] > max_profits:
                max_profits = prices[sell_day] - prices[buy_day]
            print(max_profits)
    return 'Maximum Profit = %s' % max_profits


# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell_once(prices):
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit


price = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
profits = buy_and_sell_stock_once(price)
print(profits)
