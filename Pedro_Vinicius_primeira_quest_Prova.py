#####Cinco amigos saíram para jantar fora e nessa noite ficou definido que seria feito 
# um sorteio para quem iria pagar a conta. Para isso faça um dicionário com os nomes dos amigos, 
# faça um sorteio dentre esses para ver quem vai pagar a conta. Além disso, seu programa deve pegar o 
# valor da conta que pode ser adiciono os 10% do garçom. 


import random
import math

nomes = {}

quantidade = 5



print(' ')
conta = float(input('Qual o Valor da Conta a Pagar: R$'))
print(' ')
for i in range(quantidade):
    nomes[i] = str(input('Quem irá participar? '))
    print(' ')
    
def valorGorjeta(valorconta, pagarGorj ,taxa = 0.10):
    if pagarGorj == 'S':
        return conta*0.10
    return 0

valid = ('S','N')
pagar = None


while not pagar in valid:
    print(' ')
    pagar = input('Você deseja pagar a gorjeta? [S/N] ').upper()
    print(' ')

print(' ')
print('O número de cada um é: ')
print(nomes)
print(' ')

sorteio = math.ceil((quantidade - 1) * (random.random()))

print(f'Número Sorteado é: {sorteio}')
print(nomes[sorteio],' irá Pagar a Conta Hoje.')
print(' ')
print(f'\nValor da Gorjeta é: R$ {valorGorjeta(conta,pagar)}')
print(f'Valor Total da Conta é {valorGorjeta(conta,pagar)+conta}')
print(' ')