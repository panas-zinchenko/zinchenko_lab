import shelve


dict = {1: 'red', 2: 'blue', 3: 'green'}


with shelve.open('004') as f:  # відкриваємо файл за допомогою модуля
    f['d'] = dict  # заповнення файлу під ключем 'd'
f.close()

with shelve.open('004') as f:  # відкриваємо файл за допомогою модуля
    print(f['d'])  # вивести дані файлу за допомогою ключа
f.close()