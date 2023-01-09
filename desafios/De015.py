dias = float(input("Quantos dias Alugado? "))
km = float(input("Quantos km rodados? "))

aluguel = (dias * 60) + (km * 0.15)

print("O total a pagar é: R${:.2f}".format(aluguel))