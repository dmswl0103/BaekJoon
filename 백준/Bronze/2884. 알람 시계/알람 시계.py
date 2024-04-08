a, b = map(int, input().split())
time=a*60+b
wake_time=time-45
m=wake_time%60 
h=wake_time//60


while h<0:
    h+=24
    
print(h,m)