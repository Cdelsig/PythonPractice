#Python3.7 - Automate The Boring Stuff - Al Sweigart
import random

total = 0
for num in range(101):
  total = total + num
print(total)

# only print values from 12-15
for i in range(12,16):
    print (i)

# print 2-8 by increments of 2
for j in range(0,10,2):
    print(j)

# can also count backwards
for k in range(5, -1, -1):
    print(k)

for m in range(5):
    print(random.randint(1,10))
