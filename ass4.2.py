cities = {'Karachi' : {'country' : 'Pakistan', 'population' : '5 lac', 'fact' : 'it has seaside'},
          'Quetta' : {'country' : 'Pakistan', 'population' : '2 lac', 'fact' : 'city of tea'},
          'Lahore' : {'country' : 'Pakistan', 'population' : '3 lac', 'fact' : 'beautiful people'}}
          

for city,info in cities.items():
    country = info['country'].title()
    population = info['population']
    fact = info['fact'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("It has a population of about " + str(population) + ".")
    print(fact)