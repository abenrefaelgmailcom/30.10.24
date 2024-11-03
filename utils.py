def input_int_number():
    """input an int until its valid"""
    x: int = 0
    while True:
        try:
            x = int(input('enter number:'))
            break
        except:
            print('must be int')

def print_hellow():
    '''input hellow'''
    print('my first function')

if __name__ == '__name__':
    print('alot of code')
    print('alot of code')
    print('alot of code')
    print('alot of code')

print('[utils] what is ypur name? ', __name__)