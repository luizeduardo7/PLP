lista = [3,6,23,67,-98,8,90,-8,0]
sum = 0
for i in range(len(lista)):
    sum += lista[i]
media = sum/i

for i in range(len(lista)):
    if(lista[i] > media):
        print(lista[i])
    