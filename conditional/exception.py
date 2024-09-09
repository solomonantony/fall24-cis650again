# Raising Exception 
def getNumber():
    userInput = input('Enter a number')
    if userInput.isdigit():
        print('Thanks')
    else:
        raise Exception('Must input only integers')

try:
    print ('hi')
    userINput = getNumber()
except Exception as err:
    print('invalid input', str(err))
