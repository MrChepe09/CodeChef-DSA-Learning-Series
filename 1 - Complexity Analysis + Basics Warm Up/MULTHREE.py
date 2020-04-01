def div3(a):
  pre, curr = a[1], a[2]#*a[0]
  sumk = pre+curr
  for k in range(2, a[0]):
    nex = (pre + curr)
    sumk += nex
    pre, curr = curr, nex
  if(sumk%3==0):
    return ("YES")
  else:
    return ("NO")

test = int(input())
for i in range(test):
  a = list(map(int, input().split()))
  print(div3(a))
