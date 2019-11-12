# задача №1
n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1
# задача №2
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)  
# задача №3
n = int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)
# задача №4
x = int(input())
y = int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)
# задача №5
x = int(input())
p = int(input())
y = int(input())
i = 0
while x < y:
    x *= 1 + p / 100
    x = int(100 * x) / 100
    i += 1
print(i)

# задача №6
len = 0
while int(input()) != 0:
    len += 1
print(len)
# задача №7
sum = 0
element = int(input())
while element != 0:
    sum += element
    element = int(input())
print(sum)
# задача №8
import random
x=1
y=0
sun=0
max=0
while x!=0:
    x = random.randint(0, 10)
    print ("среднее:", sun/y, "максимальное: ",max)
# задача №9
import random
x=1
y=0
max=0
index=0
while x!=0:
    x = random.randint(0, 10)
    print(x)
    y+=1
    if max<x:
         max=x
         index=y
print("Индекс",index, "числа ",max)
# задача №10
import random
x=1
y=0
max=0
len=0
while x!=0 and y<20:
    x = random.randint(0,20)
    print(x)
    len+=1
    if max<=x:
        max=x
print ("Max - ",max,"Len - ",y)

           
        
        
        