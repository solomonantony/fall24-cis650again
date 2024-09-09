def get_password():
  print('Hello, Joe. What is the password? (It is a fish.)')
  return input()

if __name__ == '__main__':
   print('Who are you?')
   name = input()
   if name == 'Joe':
    while True:
        if get_password() == 'swordfish':
            print('Access granted.')
            break
