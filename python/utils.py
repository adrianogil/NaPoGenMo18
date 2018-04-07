from random import randint

def opposite_direction(d):
    if d == 'north':
        return 'south'
    elif d == 'south':
        return 'north'
    elif d == 'west':
        return 'east'
    return 'west'

def capitalize(s):
    return s[0].upper() + s[1:]

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        pass
 
    return False

def get_random(l):
    '''
        list l
    '''
    return l[randint(0, len(l)-1)]