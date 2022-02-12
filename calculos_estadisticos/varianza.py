import numpy as np

def moda(lista):
    lista.sort()
    moda = (lista[0], 1)
    count = 0
    current = lista[0]
    for n in lista:
        if n == current:
            count += 1
        else:
            if count > moda[1]:
                moda = (current, count)
            current = n
            count = 1
    return moda[0]

def media(lista):
    return sum(lista) / len(lista)

def mediana(lista):
    total = len(lista)
    i = int((total + 1) / 2)
    lista.sort()
    return lista[i] + ((total + 1) / 2 - i) * (lista[i + 1] - lista[i])

# Para calcular la mediana también podemos simplemente seleccionar el primer elemento cuya frecuencia absoluta acumulada supere int((total + 1) / 2)

def media2(xi, fi):
    it = len(xi)
    total = 0
    for i in range(it):
        total += xi[i] * fi[i]
    return total / sum(fi)

n_de_coches = [4, 0, 1, 2, 3, 1, 0, 1, 1, 1, 4, 0, 1, 3, 2, 2, 1, 1, 0, 1, 2, 3, 1, 1, 1]
total = len(n_de_coches)
xi = list(set(n_de_coches))
fi_frecuencia_absoluta = [n_de_coches.count(i) for i in xi]
Fi_frecuencia_absoluta_acumulada = [sum(fi_frecuencia_absoluta[:i]) for i in range(1, len(fi_frecuencia_absoluta) + 1)]
hi_frecuencia_relativa = [i / total for i in fi_frecuencia_absoluta]
porcentaje_relativo = [100 * i for i in hi_frecuencia_relativa]

print("Elementos:", xi)
print("Frecuencia absoluta:", fi_frecuencia_absoluta)
print("Frecuencia absoluta acumulada: ", Fi_frecuencia_absoluta_acumulada)
print("Frecuencia relativa:", hi_frecuencia_relativa)
print("Porcentajes: ", porcentaje_relativo)
print(sum(porcentaje_relativo), sum(hi_frecuencia_relativa))

print("Media: ", media(n_de_coches))
print("Media otra formula: ", media2(xi, fi_frecuencia_absoluta))
print("Moda:", moda(n_de_coches))
print("Mediana:", mediana(n_de_coches))

def varianza(lista):
    total = len(lista)
    med = media(lista)
    acc = 0
    for i in lista:
        elem = i - med
        acc += elem * elem
    return acc / total

def varianza2(lista):
    elementos = list(set(lista))
    total = len(lista)
    fi = [lista.count(i) for i in elementos]
    med = media(lista)
    acc = 0
    for i in range(len(elementos)):
        acc += elementos[i] * elementos[i] * fi[i]
    return acc / total - med * med

def deviation(lista):
    return np.sqrt(varianza(lista))

def coeficiente_de_variacion(lista):
    return deviation(lista) / media(lista)

print("Varianza:", varianza(n_de_coches))
print("Varianza:", varianza2(n_de_coches))
print("Desviación típica:", deviation(n_de_coches))
print("Coeficiente de variación:", coeficiente_de_variacion(n_de_coches))

