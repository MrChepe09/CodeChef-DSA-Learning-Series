def div3(a):
  ans = [0, 0]#*a[0]
  ans[0] = a[1]
  ans[1] = a[2]
  #for k in range(2, a[0]):
   # ans[k] = (sum(ans))%10
  if(sum(ans)%3==0):
    return ("YES")
  else:
    return ("NO")

test = int(input())
for i in range(test):
  a = list(map(int, input().split()))
  print(div3(a))
