year = 2108 # встановити деякий рік
month = 2 # встановити деякий місяць
if month == 2:
    if year == True: # вкладений оператор if-else
        nDays = 29
    else:
        nDays = 28
elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
    nDays = 30
else:
    nDays = 31
print("Кількість днів у місяці:", month)
print("nDays=", nDays)