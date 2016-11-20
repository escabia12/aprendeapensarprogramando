__author__ = 'Escabia'

''' Calculadora simple que realiza operaciones con dos operandos por entrada y un operador básico (+,-,*,/)'''

operando1 = int(input("Introduzca primer operando: "))
operador = input("Operador: ")
operando2 = int(input("Segundo operando: "))

if operador == '+':
    print (operando1 + operando2)
elif operador == '-':
    print (operando1 - operando2)
elif operador == '*':
    print (operando1 * operando2)
elif operador == '/':
    print (operando1 / operando2)
else:
   print("Operador Inválido")
