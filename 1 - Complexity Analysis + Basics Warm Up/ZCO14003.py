def mobile(price):
  maxp = 0
  for j in range(len(price)):
    maxp = max(maxp, (len(price)-j)*price[j])
  return maxp

p = int(input())
price = [0]*p
for i in range(p):
  price[i] = int(input())
price.sort()
print(mobile(price))
