# 1.Deberá construir una aplicación desarrollada en Python la cual calcula la serie de Fibonacci, mediante consola o de forma gráfica el usuario deberá ingresar el número de iteraciones desea calcular de la serie y mostrar la serie completa hasta dicho momento en forma lineal. Ej. N° de Iteraciones: 5 - Resultado esperado: “1, 2, 3, 5, 7”

numero= input("Escriba el número de fibbonaci que quiere: ") 
lista=range(int(numero))
lista[0] = 0
lista[1] = 1
for i in xrange(2, numero):
    lista[i]=lista[i-2]+lista[i-1]
print (lista)
