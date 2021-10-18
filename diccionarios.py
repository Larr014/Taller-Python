#Arreglos asociativos
#{key:value}
curso = {'Claudio': [4,3.6,7],'Cata':[3.7,6.7,7]}
print(curso['Claudio'])

for x in curso:
    print(f'clave: {x} notas: {curso[x]}')

print(curso.values())
print(curso.keys())
print(curso.items())

for clave,valor in curso.items():
    print(f'clave: {clave} notas: {valor}')

curso['Duvan'] = [0.5*x for x in range(1,4)]
for clave,valor in curso.items():
    print(f'clave: {clave} notas: {valor}')