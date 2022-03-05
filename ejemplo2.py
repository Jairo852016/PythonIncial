numeros=[1,2,3,4,5,6,918,23,1]
objetos=['hola',123, 4.5,True]
print(numeros)
print(objetos[3])
objetos.append(False)
print(objetos)
objetos.append(1)
print(objetos)
objetos.pop(1)
print(objetos)
for elemento in objetos:
    print(elemento)
reversa=objetos[::-1]
print(reversa)

