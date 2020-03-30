def lapin(s):
  l = int(len(s)//2)
  if(len(s)%2==0):
    a = s[:l]
    b = s[l:]
    a, b = list(a), list(b)
    a.sort()
    b.sort()
    if(a==b):
      return 'YES'
    else:
      return 'NO'
  else:
    a = s[:l]
    b = s[(l)+1:]
    a, b = list(a), list(b)
    a.sort()
    b.sort()
    if(a==b):
      return 'YES'
    else:
      return 'NO'

test = int(input())
for i in range(test):
  s = input()
  print(lapin(s))
    
