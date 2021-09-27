
while True:
    print('hola')
    break

while 4>5:
    print("si")
else:
    print("chao")

while 5>4:
    print("hola entre a este ciclo")
    break
else:
    print('chao de nuevo')

i = 0
while i<2:
    print("hola entre a este ciclo !!")
    i += 1
else:
    print('chao de nuevo')

while 0: #Es considerado False
    print("hola")

while 1: #Es considerado True
    print("chao pescao")
    break

while 4: #Cualquier numero distinto de 0 es True
    print("chao pescao de nuevo")
    break
