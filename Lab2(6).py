print("введіть 1 за сортуванням за збільшенням")
print("введіть 2 за сортуванням за зменшенням")

try:
    ans = int(input("/зробіть вибір > "))

    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    arr = [a, b, c]

    if ans == 1:
        print('за збільшенням', sorted(arr))
    elif ans == 2:
        print('за зменшенням', sorted(arr, reverse=True))
    else:
        print("\n число не відповідає! \n  enter 1 or 2")

except ValueError:
    print("Error! напишіть тільки  Integer числа!")

    input("\n нажміть  ENTER to exit")

