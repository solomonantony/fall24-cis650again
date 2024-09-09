#Exit example
import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        break
    print('You typed ' + response + '.')
