

while True :
    units = input('What unit is the temperature? K, F or, C`?').upper()
    if units in ('K', 'F', 'C') :
        break
    else :
        print('Invalid input!')

while True :
    temperature = input('What temperature is the water?')
    if type(temperature) != int or type(temperature) != float :
        break
    else : print('Invalid input!')

if is_gas == True :
    print('Water is a gas.')
elif is_liquid == True :
    print('Water is a liquid.')
elif is_solid == True :
    print('Water is a solid.')
else :
    print('None')