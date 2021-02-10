dnovo = 's'

while dnovo == 's':
    maisinf = 's'

    print('\n*** Seja bem-vindo a informação numérica ***')

    num = int(input('Digite um número inteiro: '))

    while maisinf == 's':
        print('1- Par ou ímpar \n2- Antecessor e Sucessor \n3- Dobro \n4- Negativo ou Positivo')
        inf = int(input('Selecione o que deseja saber sobre o número {}: '.format(num)))
        if inf == 1:
            if num % 2 == 0:
                print("Este número é par.")
            else:
                print("Este número é impar.")

        elif inf == 2:
            ant = num - 1
            suc = num + 1 
            print('Antecessor é: {} | Sucessor é: {}.'.format(ant, suc))

        elif inf == 3:
            dobro = num * 2
            print('O dobro de {} é: {}.'.format(num, dobro))

        elif inf == 4:
            if num > 0:
                print('Este é um número positivo.')
            elif num < 0:
                print("Este é um número negativo.")
            else:
                print("Zero é neutro.")

        else:
            print("Obrigado. Volte sempre!")
            
        maisinf = input('Deseja saber mais alguma informação? [s/n]: ')
        while maisinf != 's' and maisinf != 'n':
            maisinf = input('Entre com um valor valido: ')
       

    dnovo = input('Deseja saber sobre outro número? [s/n]: ')
    while dnovo != 's' and dnovo != 'n':
            dnovo = input('Entre com um valor valido: ')
print('Tá ok, até logo!')