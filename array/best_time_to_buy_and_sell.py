
prices=[7,1,5,3,6,4]
prices=[4, 2, 9, 7, 1, 2]

def best_time_to_buy_and_sell(prices):
   minPrice,maxProfit=prices[0],0
   for indx in range(len(prices)):
      if prices[indx] < minPrice:
          minPrice=prices[indx]
      elif price[indx] - minPrice > maxProfit:
          maxProfit=
   print(maxProfit)


print(best_time_to_buy_and_sell(prices))
