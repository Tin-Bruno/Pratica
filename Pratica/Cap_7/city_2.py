def city(city_name, city_location):
    city_country = city_name + " " + city_location
    return city_country.title()


while True:
    print('\nTell me the name for the city with your live: ')
    print("Enter 'q' to quit")

    name = input("\nEnter city name: ")
    if name.lower() == 'q':
        break

    location = input("Enter city location: ")
    if location.lower() == 'q':
        break

    CITY_FORMATTED = city(name, location)

    print("\n____YOUR CITY IS: " + CITY_FORMATTED + '____\n')
