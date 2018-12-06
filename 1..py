# a=0
# b=1
# while b < 100:
#     print(b)
#     a,b=b,a+b


num=int(input(">>>"))

for i in range(3,101):
    for j in range(2,i):
        if i % j == 0:

            break
        else:
            print(i)




