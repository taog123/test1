a = int(input("a"))
for i in range(1,a+1):
    if i == 1 or i == a:
        print("*"*a)
    else:
        print("*"+" "*(a-2)+"*")