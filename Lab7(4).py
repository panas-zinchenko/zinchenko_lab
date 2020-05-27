def fibonacci(n):
    print('генератор')
    fib1, fib2 = 0, 1
    print('ініт готовий, починаємо петлю з  n =', n)
    for i in range(n):
        if i == 0:
            print('це є перша ітерація')
        fib1, fib2 = fib2, fib1 + fib2
        print('go to yield value', fib1, 'while i =', i)
        yield fib1
        print('i =', i, 'and fib1 =', fib1, 'fib2 =', fib2)
    print("кінець")
list(fibonacci(5))