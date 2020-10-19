a=input()
b,c=0,1

for i in range(1,len(a)):
    if(a[i]!=a[i-1]):
        b=max(b,c)
        c=0
    c+=1
print(max(b,c))


# CodeBy:RahulMahajan
# CF:anonymous3107
# CC:anonymous0201
# CSES:rahulmahajan
