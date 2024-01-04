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
            for a in zoo:
                if name in animal.keys():
                    a[name] += 1
                else:
                    animal[name] = 1
                    zoo.append(animal)
                    animal=dict()