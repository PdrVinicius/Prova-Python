####Com o passar do tempo os signos ganharam bastante popularidade, vindo de encontro também temos 
# os Zodíaco Chinês levando em conta que não é muito visto no nosso cotidiano, faça um programa que ajude as 
# pessoas a descobrirem seu signo do Zodíaco Chinês. O seu programa deve mostrar no final o nome da pessoa e o 
# signo. Use tuplas para esse exercício e um pelo menos duas funções. Levando em consideração que ele é composto 
# por animais com ciclo de 12 anos uma maneira simples de identificar é com o ano do nascimento. 
# Os signos são: 1- macaco 2-galo 3-Cão 4-Porco 5-Rato 6-Boi 7- Tigre 8-coelho 9-Dragão 10-Serpente 11-Cavalo 
# 12-Carneiro.


signos = ('Macaco','Galo','Cão','Porco','Rato','Boi','Tigre','coelho',
'Dragão','Cobra','Cavalo','Carneiro')

def zodiac():
    print('''
          **********************************
          
            BEM VINDO AO SEU ZODIACO CHINES
            
          **********************************
          (1) Seu Zodiaco Chines
          ----------------------------------
          (2) Sair
          **********************************
          ''')

def zdc():
    print('''
          Lista de Signos do Zodiaco Chines:
          
          1- Rato
          2- Boi
          3- Tigre
          4- Coelho
          5- Dragão
          6- Cobra
          7- Cavalo
          8- Macaco
          9- Galo
          10- Cão
          11- Porco
          12- Carneiro
          
          ''')

while True:
    zodiac()
    opc = input('Escolha uma Opção: ')
    print(' ')
    if opc == '1':
        zdc()
        nome = str(input('Informe seu Nome: '))
        print(' ')
        ano = int(input('Digite seu ano de Nascimento: '))
        print(' ')
        signos = signos[ano%12]
        print(f'{nome}, O seu signo do Zodíaco Chinês é {signos}.')
        break
        
    elif opc =='2':
        break