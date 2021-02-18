city = input('Enter Town/City: ')
cities = ['Dublin', 'Belfast', 'Cork', 'Limerick', 'Derry',
'Galway', 'Lisburn', 'Kilkenny', 'Waterford', 'Sligo']

if city in cities:
    if (city == cities[0] or city == cities[7] or city == cities[8]):
        prov = 'Leinster'
    elif (city == cities[2] or city == cities[3]):
        prov = 'Munster'
    elif (city == cities[1] or city == cities[4] or city == cities[6]):
        prov = 'Ulster'
    elif (city == cities[5] or city == cities[9]):
        prov = 'Connacht'
    
    print('You entered {0}. {0} is in {1}.' .format(city, prov))

else:
    print('Sorry, I didn\'t recognise that name.')