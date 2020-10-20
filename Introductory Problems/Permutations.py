a=int(input())

if(a==1):
    print(1)
elif(1<a<4):
    print('NO SOLUTION')
elif(a==4):
    print('2 4 1 3')
else:
    for i in range(1,a+1,2):
        print(i)
    for i in range(2,a+1,2):
        print(i)


# CodeBy:RahulMahajan
# CF:anonymous3107
# CC:anonymous0201
# CSES:rahulmahajan