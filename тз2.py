n = int(input())
a = n
b = 0
while n > 0:
    b = b*10+n % 10
    n //= 10
if a == b:
    print("YES")
else:
    print("NO")