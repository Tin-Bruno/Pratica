cities = {'São Paulo': {'location': 'Brazil',
                        'population': 46000000,
                        'Fact': 'São Paulo is the capital of Brazil.'},
          'Nova York': {'location': 'EUA',
                        'population': 8000000,
                        'Fact': 'Nova York is the capital of EUA.'},
          'Tokyo': {'location': 'Japan',
                    'population': 9000000,
                    'Fact': 'Tokyo is the capital of Japan.'}}
for city, info in cities.items():
    print('City is: ' + city.title())
    print('\tLocation is: ' + info['location'])
    print('\tPopulation is: ' + str(info['population']))
    print('\tFact is: ' + info['Fact'])
