cas_number = '7732-18-5'
rho = 1000
mu = 1
Tm = 273.15
Tb = 373.13
k = 0.58

def convert_to_kelvin(temperature, units) :
    if (type(temperature) == int or type(temperature) == float) and (units in ('K', 'C', 'F')):
        if units == 'K' :
            pass
        elif units == 'C':
            temperature += 273.15
            return temperature
        else :
            temperature = (temperature + 459.67) * 5 / 9
            return temperature
    else :
        return None

def is_gas(temperature) :
    if (type(temperature) == int) or (type(temperature) == float) :
        if temperature >= 373.15 :
            return True 
        else :
            return False
    else :
        return None 

def is_liquid(temperature) :
    if (type(temperature) == int) or (type(temperature) == float) :
        if temperature < 373.15 and temperature > 273.15 :
            return True
        else :
            return False
    else :
        return None 

def is_solid(temperature) :
    if (type(temperature) == int) or (type(temperature) == float) :
        if temperature <= 273.15 :
            return True
        else :
            return False
    else :
        return None 

if __name__ == '__main__' :

    temperature = 0
    units = 'K'

#    while True :
    units = input('What unit is the temperature? K, F or, C?').upper()
    if units in ('K', 'F', 'C') :
        #break
        pass
    else :
        print('Invalid input!')

    #while True :
    temperature = input('What temperature is the water?')
    try :
        temperature = float(temperature)
        #break
        pass
    except :
        print('Invalid input!')

    temperature = convert_to_kelvin(temperature, units)

    if is_gas(temperature) :
        print('gas')
    elif is_liquid(temperature) :
        print('liquid')
    elif is_solid(temperature) :
        print('solid')
    else :
        print('Invalid input!')
