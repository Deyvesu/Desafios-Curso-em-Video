from math import hypot

cateto_op = float(input("Digite o cateto oposto: "))
cateto_ad = float(input("Digite o cateto adjacente: "))


hipotenusa = hypot(cateto_op, cateto_ad)

print("A hipotenusa dos catetos digitados é igual à: {:.2f}".format(hipotenusa))

