#atm simmulation
pin = 1234
balance = 10000
enter=int(input('pin: '))
if enter == pin:
    print('''1.withdraw
2.deposite
3.check balance''')
    option= int(input('select option'))
    if option == 1:
        atm = float(input('enter amount'))
        if atm<=balance:
            balance-=atm
            print('remaning:',balance)
        else:
            print('insufficent')
    elif option == 2:
        atm = float(input('enter amount'))
        balance+=atm
        print('avalilable: ',atm)
    elif option == 3:
        print(balance)
else:
    print('wrong pin')

