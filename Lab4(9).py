s = input("введіть ")
if 'j' in s:
    i = s.replace('j', 'k')
else :
    s.ljust(1, 'f')
    s.rjust(1, 'f')
    i = s.replace('j', 'f')
print(i)