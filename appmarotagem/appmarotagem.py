import sys
from Calculadora import Calculadora

print("------------------------- +++++++++++Calculadora+++++++++++ -------------------------")
x1 = None
x2 = None
print("Digite um número")

if x1 is None:
	x1 = int(input())

print("Digite outro número")
if x2 is None:
	x2 = int(input())
	
op = "X"
while op != "E":
    print("O que você deseja fazer? [A]dicionar/ [M]ultiplicar/ [D]ividir/ [S]ubtrair, [C]lear/ [E]xit")
    op = input()
    op = op.upper();
    calculadora = Calculadora(x1,x2,op) 
    calculadora.calcular()