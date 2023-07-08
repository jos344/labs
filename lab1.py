import math

calculations = 0
total_volume= 0
choice =''

def number_of_calculations():
    """
    Increment calculations.
    """
    global calculations
    calculations += 1

def total_volume_calculated(volume):
    """
    Total volume appended.
    """
    global total_volume
    total_volume += volume

def cube_volume():
    """
    Calculate the volume of a cube.
    """
    a = eval(input("Enter side of cube in cm "))
    volume = a**3
    return round(volume, 2)

def tetrahedron_volume():
    """
    Calculate the volume of a tedrahedron.
    """
    b = eval(input("Enter side of tetrahedron in cm "))
    volume = (b ** 3 / (6 * math.sqrt(2)))
    return round(volume, 2)

def ask_user():
    """
    Ask user what to calculate.
    """
    try:
        choice = input('select: ') 
        return choice
    except:
        return 0

def show_menu():
    print('============================================')
    print('                 WELCOME                    ')
    print('Press 1. Calculate the volume of a cube'     )
    print('Press 2. Calculate the volume of tetrahedron')
    print('============================================')

show_menu()
while True:
    choice = ask_user()
    if choice == '1':
        x = cube_volume()
        print(f'The volume of your cube is {x} cm^3\n')
        number_of_calculations()
        total_volume_calculated(x)
    
    elif choice == '2':
        y = tetrahedron_volume()
        print(f'The volume of your tedrahedron is {y} cm^3\n')
        number_of_calculations()
        total_volume_calculated(y)
        
    elif choice == 'Q':
        print('Good bye')
        break
    else:
        print('wrong option')

    print(f'You have made calculations: {calculations}')
    print(f'Your total area calculated: {total_volume}')