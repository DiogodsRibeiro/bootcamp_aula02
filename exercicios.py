import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# try: 
#     first_number = int(input('Digite um número:'))
#     second_number = int(input('Digite outro numero: '))

#     Resultado = first_number + second_number
#     print(f'O valor total é: {Resultado}')
# except ValueError:
#     print('Please, type a valid number!')



# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# try:
#     number_user = int(input('Digite um numero inteiro: '))

#     resto = number_user % 5

#     print(f'O resto da divisao do {number_user} é {resto}')
# except ValueError:
#     print('Please, type a int number')


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# first_number = float(input(f'Type a number: '))
# second_number = float(input(f'type another number: '))

# result = int(first_number * second_number)

# print(f'O resultado da multiplicação é: {result}')


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# try:
#     numero_01 = int(input('insira um numero inteiro: '))
#     numero_02 = int(input('insira outro numero inteiro: '))

#     resultado = numero_01 // numero_02
#     print(f'Resultado da divisao: {resultado}')
# except ValueError:
#     print('Por favor, insira apenas números inteiros válidos.')
# except ZeroDivisionError:
#     print('Não é possível dividir por zero.')



# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# first_number = int(input(f'Type a number: '))

# Result = first_number ** 2

# print(f'este numero ao quadrado é: {Result}')

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# try:
#     first_number = float(input(f'Type a float number: '))
#     second_number = float(input(f'Type a second float number: '))

#     Result = first_number + second_number

#     print(f'O resultado dos dois numeros flutuantes é: {Result}')
# except ValueError:
#     print(f'comma its not allowed')    

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio_do_circulo = float(input('Digite o raio: '))
# area_do_circulo = math.pi *  raio_do_circulo ** 2
# print(f'{area_do_circulo:.2f}')


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data_usuario = input('insira uma data no formato dd/mm/aaaa: ')
# lista_dia_mes_ano = data_usuario.split("/")
# print(f'o elemento 1 é o: {lista_dia_mes_ano[0]}')
# print(f'o elemento 2 é o: {lista_dia_mes_ano[1]}')
# print(f'o elemento 3 é o: {lista_dia_mes_ano[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
