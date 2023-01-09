preco = int(input("Qual preço do produto? "))

descont = preco * 5 / 100

novo_preco = preco - descont

print("Preço original {}, preço com desconto {} ".format(preco,novo_preco ))