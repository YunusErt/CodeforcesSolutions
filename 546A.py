k,n,w = map(int, input().split())
b=0

for i in range (1,(w+1)):
    
    b+=k*i  

if (n==b or n>b):
    print(0)
else:
    print(b-n)
