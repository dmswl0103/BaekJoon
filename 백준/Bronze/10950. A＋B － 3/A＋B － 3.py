n=int(input())
c=[]
for i in range(0,n):
    a,b=map(int,input().split())
    c.append(a+b) 
for j in range(0,len(c)):
    print(c[j])


