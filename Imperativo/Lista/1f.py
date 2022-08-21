distancia = 58-57
i = 0

if distancia < 0:
    while distancia < 0:
        i += 1
        distancia +=1
elif distancia > 0:
    while distancia > 0:
        i += 1
        distancia -= 1
else:
    distancia = 0

print(i)