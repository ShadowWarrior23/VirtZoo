zoo = list()
print('Ez egy állatkert.')
print('Állat hozzáadása (1) - elvétele (2) - kilépés (0)')
select = None

while select != "0":
    select = input('Mit szeretne tenni? ')
    if select != '0':
        if select == '1':
            animal = dict()
            name = input('A dög neve: ')
            if name not in animal.keys():
                animal[name] = 1
                zoo.append(animal)
            else:
                animal[name] += 1
                
            animal=dict

for a in zoo:
    print(a)

input('Press Enter to exit!')