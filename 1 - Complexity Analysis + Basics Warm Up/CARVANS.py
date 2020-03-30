def max_speed(a):
  count = 1
  for j in range(1, len(a)):
    if(a[j]<a[j-1]):
      count+=1
  return count

test = int(input())
for i in range(test):
  n = int(input())
  arr = list(map(int, input().split()))
  print(max_speed(arr))
