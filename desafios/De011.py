print("Descubra o quanto de tinta é necessario para pintar sua parade.")
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura 
tinta = area / 2

print("Area total da parede {}. ".format(area))
print("Quantidade de tinta necessaria: {} litros. ".format(tinta))
