a=int(input())

b=list(map(int,input().split()))
c=sum(b)
print((a*(a+1))//2 - c)