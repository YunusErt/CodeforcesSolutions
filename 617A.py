x = int(input())
if (x<=5):
    print(1)
else:

    r=int(x/5)
    if(x%5==0):
        print(r)
    else:
        print(r+1)