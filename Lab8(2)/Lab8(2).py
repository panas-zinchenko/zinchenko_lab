f = open("f.txt")
x = f.read()
f.close()
x = x.split()
y = 0
g = []
h = []
m = []

for i in x:

    num = int(i)

    z = num % 2
    k = num
    q = (num % 3 and num % 5)
    if z == 0:
        g.append(num)
    if k > 0:
        h.append(num)
    if q == 0:
        m.append(num)


g_file = open("g.txt", "w")
h_file = open("h.txt", "w")
m_file = open("m.txt", "w")

g_file.write(str(g))
h_file.write(str(h))
m_file.write(str(m))

g_file.close()
h_file.close()
m_file.close()