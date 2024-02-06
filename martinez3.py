exit= False
while True:
    var1= input('Enter a number: ')
    var2= input ('Enter another number: ')

    if var1.isdigit() and var2.isdigit():
        var1= int(var1)
        var2= int(var2)

        addition = var1+var2
        subtraction= var1-var2
        multiplication= var1*var2
        division= var1/var2
        modulus= var1%var2
        print(f'The sum is: {addition}')
        print(f'The difference is: {subtraction}')
        print(f'The product is: {multiplication}')
        print(f'The quotient is: {division}')
        print(f'The remainder is: {modulus}')
    else:
        print('tanga ka ba? sabe number eh')

next_calculation = input("Let's do next calculation? (yes/no): ")
if next_calculation == "no":
    print(f'{False}')

     