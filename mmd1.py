#weith= input('enter your weitgh: ')
#unit = input()
#secret_number = 9
#guess_count=0
#guess_limit=3
#while guess_count < guess_limit:
 #   guess = int(input('guess: '))
  #  guess_count +=1
   # if guess == secret_number:
    #    print('You won!')
     #   break
#else:
 #   print('sorry u failed'
n1 = int(input('ye adad bego '))
n2 = int(input('ye adad dige ham begoo '))
hesab = input('mikhay ba adadet che konam entekab kon (+   -   *) ')
if hesab == '+' :
    print(f'khedmt shoma{n1}'+f'{n2}')
elif hesab == '*':
    print(f'khedmat shoma{n1}' * f'{n2}')
elif hesab == '-':
    print(n1-n2)
else :
    print('nmidonm chetrie')