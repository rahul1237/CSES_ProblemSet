a=int(input())
x=0
while(a!=0):
    b=str(a)
    c=[]
    for i in range(len(b)):
       c.append(int(b[i]))
    a-=max(c)
    b=str(a)
    x+=1
print(x)

# CodeBy:RahulMahajan
# CF:anonymous3107
# CC:anonymous0201
# CSES:rahulmahajan