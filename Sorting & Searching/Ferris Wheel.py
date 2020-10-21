a,b=map(int,input().split())
c=sorted(list(map(int,input().split())))
d=0
e=0
while(d<a):
    if(c[d]+c[(a-1)] > b):
        a-=1
    else:
        d+=1
        a-=1
    e+=1
print(e)

# CodeBy:RahulMahajan
# CF:anonymous3107
# CC:anonymous0201
# CSES:rahulmahajan