print(" *** String count ***")
y = str(input("Enter message : "))
c = 0
d = 0
x = y.upper()
g = y.lower()
l = []
m = []
for i in range(len(y)):
    if y[i] == x[i] and y[i] != ' ' and y[i] != '.' and y[i] != '':
        c += 1 
        temp = y[i]
        if temp not in l:
            l.append(y[i])
    
for i in range(len(y)):
    if y[i] == g[i] and y[i] != ' 'and y[i] != '.':
        d += 1 
        temp = y[i]
        if temp not in m:
            m.append(y[i])

up = l.sort()
down = m.sort()

print("No. of Upper case characters : " + str(c))
print("Unique Upper case characters :","  ".join(l))
print("No. of Lower case Characters : " + str(d))
print("Unique Lower case characters :","  ".join(m))
