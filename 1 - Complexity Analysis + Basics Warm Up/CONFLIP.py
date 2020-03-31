def elephant(a):
  l = a[1]
  if(l%2==0):
    return int(l/2)
  else:
    if(a[0]==a[2]):
      return int(l/2)
    else:
      return int((l/2)+1)
    
test = int(input())
for i in range(test):
  n = int(input())
  for j in range(n):
    a = list(map(int, input().split()))
    print(elephant(a))
