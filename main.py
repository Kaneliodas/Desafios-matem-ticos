#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
a = float(input("Ponha o 1° número inteiro: "))
b = float(input("Ponha o 2° número inteiro: "))
c = float(input("Ponha o 1° número real: "))
#Agora o que eu vou mostrar
prim = (a*2) + (b/2)
seg = (a*3) + c
ter = c**3

print("o produto do dobro do primeiro com metade do segundo: " + str(prim))
print("a soma do triplo do primeiro com o terceiro: " + str(seg))
print("o terceiro elevado ao cubo: " + str(ter))
