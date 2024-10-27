for A in range(128):
    B = True
    for x in range(128):
        if ((x&94 == 0) or (x&21 != 0) or (x&A != 0)) == 0:
            B = False
    if B:
        print(A)
        break

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
      if ((x%18 != 0) or (x%54 != 0 or x%A == 0)) == 0:
            flag = False
    if flag:
        print(A)
s = []
for a1 in range(-100, 100):
    for a2 in range(-100, 100):
        flag = True
        for x in range(-100,100):
            if ((not(a1 <= x <= a2)) or (25 <= x <= 30) or (15 <= x <= 22)) == 0:
                flag = False
        if flag:
            s.append(a2 - a1)
print(max(s))