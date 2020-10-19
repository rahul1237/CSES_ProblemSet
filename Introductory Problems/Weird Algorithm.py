a=int(input())
b=[str(a)]

while(a!=1):
    if(a%2==0):
        a//=2
        b.append(str(a))
    else:
        a=((a*3)+1)
        b.append(str(a))
print(''.join(b))


# CodeBy:RahulMahajan
# CF:anonymous3107
# CC:anonymous0201
