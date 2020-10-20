for _ in range(int(input())):
    a,b=map(int,input().split())
    if(a>b):
        a,b=b,a
    if(2*a < b):
        print('NO')
    # elif(2*a == b):
    #     print('YES')
    else:
        a%=3
        b%=3
        if((a==0 and b==0) or (a==1 and b==2) or (a==2 and b==1)):
            print('YES')
        else:
            print('NO')
