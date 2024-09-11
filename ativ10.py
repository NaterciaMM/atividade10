# Crie um programa que receba um número inteiro e informe se ele é par ou ímpar.

numero = float(input("digite o numero"))
resto = numero % 2

if resto == 0:
    print("numero é par")
else:
    print("numero é impar")
    