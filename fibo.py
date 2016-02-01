# 1.Deberá construir una aplicación desarrollada en Python la cual calcula la serie de Fibonacci, mediante consola o de forma gráfica el usuario deberá ingresar el número de iteraciones desea calcular de la serie y mostrar la serie completa hasta dicho momento en forma lineal. Ej. N° de Iteraciones: 5 - Resultado esperado: “1, 2, 3, 5, 7”

a=0
b=1
numero= input("Escriba el número de fibbonaci que quiere ") 
lista=range(int(numero))
i=0
for i in xrange(0, numero):
    if i == 0:
        a=0
        lista[i]=a
    elif i==1:
        b=1
        lista[i]=b
    else:
        c=a+b
        a=b
        b=c
        lista[i]=c
print (lista)
