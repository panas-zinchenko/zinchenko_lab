n=int(input("n= "))

if (n>9) and  (n<100):
    if n%10 == 0:
        print("остання цифра 0")
    else:
        print("остання цифра не 0")
else:
    print("не двохзначне")