import math

def xbar(n, x):
    i = 0
    soma = 0
    while i < n:
        soma += x[i]
        i += 1
    return 1/n * soma

def ybar(n, y):
    i = 0
    soma = 0
    while i < n:
        soma += y[i]
        i += 1
    return 1/n * soma

def cP(n, x, y, t, p): #t = xbar p = ybar
    i = 0
    somaA = 0
    somaB = 0
    somaC = 0
    while i < n:
        a = ((x[i] - t)* (y[i] - p))
        b = pow((x[i] - t), 2)
        c = pow((y[i] - p), 2)
        somaA += a
        somaB += b
        somaC += c
        i += 1
    resultado = somaA / math.sqrt(somaB*somaC)
    return resultado


try:
    nomeArq = input("Insira o nome do arquivo: ")
    arq = open(nomeArq)
    x = []
    y = []
    n = 0
    for line in arq:
        k = line.find(',')
        x.append(float(line[0:k]))
        y.append(float(line[k+1:]))
        n += 1
    t = xbar(n, x)
    p = ybar(n, y)
    resultado = cP(n, x, y, t, p) #t = xbar p = ybar
    print(resultado)
except OSError:
   print("Não foi possível abrir o arquivo.")
except ValueError:
   print("Valor não aceito.")
except ZeroDivisionError:
    if(n == 0):
        print("Arquivo Vazio.")
    else:
        print("Erro, divisão por zero!")
except Exception:
    print("Ocorreu um erro Inesperado.")



    

