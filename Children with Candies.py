candies = [2,3,5,1,3]
extraCandies = 3
result =  [False for i in range(len(candies))]
excan = candies.copy()
for x in range(0,len(candies)):
    if candies[x]+extraCandies >= max(candies):
        result[x] = True
print(result)