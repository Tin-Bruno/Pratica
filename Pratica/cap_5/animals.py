pets = {'Tobi': {'animal': 'dog',
                 'owner': 'leidiane'},
        'Mari': {'animal': 'cat',
                 'owner': 'nice'},
        'Simba': {'animal': 'dog',
                  'owner': 'henrigue'}}
for name, pet in pets.items():
    print('Name is :', name)
    print('\tAnimal is :', pet['animal'])
    print('\tOwner is :', pet['owner'])
