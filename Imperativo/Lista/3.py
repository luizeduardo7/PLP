import math

def meuIMC(altura, peso):
    imc = peso/pow(altura,2)
    if imc < 18.5:
        print("Abaixo do peso.")
    elif imc < 25 and imc >= 18.5:
        print("Normal.")
    elif imc >= 25:
        print("Sobrepeso.")
    print(imc)

peso = float(input("Insira seu peso:"))
altura = float(input("Insira seu altura:"))

meuIMC(altura, peso)