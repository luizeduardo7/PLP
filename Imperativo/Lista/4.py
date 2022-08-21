def potencias(n):
    i = 0
    pot = 2
    while i < n:
        print(pot)
        pot = 2 * pot
        i += 1

n = int(input())
potencias(n)