n = int(input())
num = n
numdig = 0
ans = 0
while num >0:
    numdig +=1
    num //= 10
num = n
while num>0:
    ld = num%10
    ans += ld**numdig
    num //= 10
if ans == n:
    print(True)
else:
    print(False)
