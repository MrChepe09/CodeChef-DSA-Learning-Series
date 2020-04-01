def ladoo_month(p, nation):
  if(nation=='INDIAN'):
    return int(p/200)
  else:
    return int(p/400)

test = int(input())
for i in range(test):
  p = 0
  n, nation = input().split()
  for j in range(int(n)):
    a = list(input().split())
    if(a[0] == 'CONTEST_WON'):
      p+=300
      if(int(a[1]) < 20):
        g = 20 - int(a[1])
        p+=g
    elif(a[0] == 'TOP_CONTRIBUTOR'):
      p+=300
    elif(a[0] == 'BUG_FOUND'):
      p+=int(a[1])
    elif(a[0] == 'CONTEST_HOSTED'):
      p+=50
  print(ladoo_month(p, nation))
