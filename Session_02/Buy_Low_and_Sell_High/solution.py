
input()
prices = list(map(int, input().split()))


profit = 0
current_low = prices[0]

# Calculating maximum profit
for i in range(len(prices) - 1):
    if prices[i] >= prices[i + 1]:
        continue
    if current_low > prices[i]:
        current_low = prices[i]
    
    temp_profit = prices[i + 1] - current_low
    if temp_profit > profit:
        profit = temp_profit

# Printing the maximum profit
print(profit)
