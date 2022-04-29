#三角形中の*の最大の長さは５
for n in range(10):
    if n < 5:
        for i in range(n+1):
            print("*",end=" ")
        print()
    else:
        for a in range(9-n):
            print("*",end=" ")
        print()


#三角形中の*の最大の長さは３
for n in range(5):
    if n<3:
        for j in range(n+1):
            print("*",end=" ")
        print()
    else:
        for b in range(5-n):
            print("*",end=" ")
        print()
