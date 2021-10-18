nombres = ['cata','Claudio','Vicente']
print(nombres)
nombres[0] = 'Ricardo'
print(nombres)
nombres.append('Joselito')
print(nombres)
#Slicing
print(f'slice: {nombres[1:3]}')



nombres.pop(1)
print(nombres)
nombres.remove('Vicente')
print(nombres)

numeros = [x ** 2  for x in range(100)]
print(numeros)

print(numeros[5:15])
del numeros[5:15]
print(numeros)
print(numeros[5:15])
numeros[5:15] = [1 for x in range(10)]
print(numeros)
print(numeros[16:36:2])

notas = [['Claudio',4,6,7],['Cata',5,2,3.7]]

for alumno in notas:
    print(alumno[0])
    print(min(alumno[1:]))
    print(max(alumno[1:]))