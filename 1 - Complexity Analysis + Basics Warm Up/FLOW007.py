def reverse(n):
  strn = str(n)
  rstrn = strn[::-1]
  return int(rstrn)

test = int(input())
for i in range(test):
  n = int(input())
  print(reverse(n))
