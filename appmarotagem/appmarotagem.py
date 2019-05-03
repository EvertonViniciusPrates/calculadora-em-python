import sys


print("------------------------- +++++++++++Calculadora para doente mental+++++++++++ -------------------------")

print("Digite um número")
x1 = int(input())
print("Digite outro número")
x2 = int(input())
op = "X"
while op != "E":
	print("O que você deseja fazer? [A]dicionar/ [M]ultiplicar/ [D]ividir/ [S]ubtrair, [E]xit")
	op = input()
	op = op.upper()
	if op == "A":
		print(x1 + x2)
	elif op == "M":
		print(x1 * x2)
	elif op == "D":
		print(x1 / x2)
	elif op == "S":
		print(x1 - x2)
	else:
		sys.exit