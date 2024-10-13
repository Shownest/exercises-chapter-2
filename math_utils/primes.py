import math

def isprime(n):
    flag= True
    if n==1:
        flag=False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            flag=False
        
    return flag
