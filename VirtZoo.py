def addAnimal(myName):
    animal = dict()
    found = False
    for a in zoo:
        if myName in a.keys():
            a[myName] += 1
            found = True
    if not found:
        animal[myName] = 1
        zoo.append(animal)

zoo = [{'madar': 1}]
animal = dict()

print('Ez egy állatkert.')
print('Állat hozzáadása (1) - elvétele (2) - kilépés (0)')
select = None

while select != "0":
    select = input('Mit szeretne tenni? ')
    if select != '0':
        if select == '1':
            name = input('A dög neve: ')
            addAnimal(name)
                

                
print(zoo)

input('Press Enter to exit!')