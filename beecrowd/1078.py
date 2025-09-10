n = int(input())
x = 0
tab = []
num = 1

# for i in range(10):
#   x = (i+1) * n
#   i = i+1
#   print(f"{num} x {n} = {x}")
#   num = num + 1


for i in range(10):
  x = (i+1) * n
  i = i+1
  
  tab.append(x)
for v in tab:
    print(f"{num} x {n} = {v}")
    num = num + 1