X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]

print([(x, y, z) for x in X for y in Y for z in Z if x + y + z == 70])
