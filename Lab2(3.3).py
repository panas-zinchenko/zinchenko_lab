n=int(input("n= "))

if (n>9) and  (n<100):

    sumN = sum(map(int, str(n)))
    if sumN>9 and sumN<100 :
        print("двохзначне")

        print()

    else:
        print("невірно")

else:
    print("введіть двохзначне число")