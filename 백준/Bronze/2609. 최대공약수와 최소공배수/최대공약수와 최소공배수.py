import sys
input = sys.stdin.readline 
n, m = map(int, input().split())

# 최대공약수 
gcd = 1 
i = 2 
while i <= n and i <= m:
    if n % i == 0 and m % i == 0:
        gcd, n, m = gcd*i, n/i, m/i
    else:
        i += 1 

print(gcd)

# 최소공배수       
lcm = gcd * n * m 
print(int(lcm))