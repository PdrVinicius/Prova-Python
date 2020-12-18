####Lurdes tem um brechó e quer um programa que armazene todas as suas peças com seus respectivos preços, 
# quantidade da peça e que ela possa excluir e incluir itens depois. Use uma lista ou lista composta para 
# armazenar o nome do item, o preço e a quantidade. Faça um menu com opções de incluir e excluir os itens 
# ( que forem vendidos). No final o programa deve mostrar os itens vendidos (excluídos), 
# a lista com os itens cadastrados( apenas aqueles que não foram vendidos e o total vendido.


pecas = list()
vendidos = list()
total = 0
op = 1

while op != 0 :
    print("menu")
    print("0- sair")
    print("1-inclui")
    print("2-excluir")

    op = int(input())

    if op == 1 :
        a = int(input("quantas quer incluir agora: "))
        for i in range(0,a) :
            cadastro = [input("nome: "),float(input("preço: ")),int(input("quantidade: "))]
            pecas.append(cadastro)
            
    elif op == 2 :
        print(pecas)
        nome = input("nome: ")
        for j in range(0,len(pecas)) :
            if nome in pecas[j][0] :
                vendidos.append(pecas[j])
                total = 1+1
                pecas[j][2]-=1


print("vendidos")
for h in range(0,len(vendidos)) :
    print(vendidos[h])
print("estoque")
for h in range(0,len(pecas)) :
    print(pecas[h])

print("total vendas : ",total)