numero_01 = int(input('Digite um número: '))

par_ou_impar = numero_01 % 2
if par_ou_impar == 0:
    print(f'O número {numero_01} é par')
else:
    print(f'O número {numero_01} é impar')