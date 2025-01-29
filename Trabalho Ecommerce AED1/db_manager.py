import csv

def limpar_linhas_vazias():
    with open('Trabalho Ecommerce AED1/estoque.csv', 'r') as estoque:
        linhas = estoque.readlines()
    linhasnaovazias = [linha for linha in linhas if linha.strip()]
    with open('Trabalho Ecommerce AED1/estoque.csv', 'w') as estoque:
        estoque.writelines(linhasnaovazias)

def mostrar():
    stocklist = []
    with open('Trabalho Ecommerce AED1/estoque.csv', 'r') as estoque:
        reader = csv.reader(estoque)
        next(reader)
        for linha in reader:
            produto, quantidade = linha
            stocklist.append(f"Há {quantidade} unidades de {produto} no estoque.")
    return stocklist
        
def remove(produto):
    with open('Trabalho Ecommerce AED1/estoque.csv', 'r') as estoque:
        linhas = estoque.readlines()
    if produto == '':
        linhas_filtradas = [linha for linha in linhas]
    else:
        linhas_filtradas = [linha for linha in linhas if produto != linha.split(',')[0]]
            

    with open('Trabalho Ecommerce AED1/estoque.csv','w') as estoque:
        estoque.writelines(linhas_filtradas)

def compras(produto, comprado):
    with open('Trabalho Ecommerce AED1/estoque.csv', 'r') as estoque:
        linhas = estoque.readlines()
    cabeçalho = linhas[0]
    linhas_atualizadas = [cabeçalho]  
    produto_encontrado = False

    for linha in linhas[1:]:  
        nome, quantidade_str = linha.strip().split(',')
        quantidade = int(quantidade_str)

        if nome == produto:
            produto_encontrado = True
            if comprado < 0:
                nova_quantidade = quantidade + comprado
            else:
                nova_quantidade = quantidade - comprado
            if nova_quantidade > 0:
                linhas_atualizadas.append(f"{nome},{nova_quantidade}\n")
            elif nova_quantidade == 0:
                print(f"Produto '{produto}' removido do estoque.")
            elif nova_quantidade < 0:
                print(f'produto com falta de estoque! Temos apenas {quantidade} no estoque.')
                linhas_atualizadas.append(f"{nome},{quantidade}\n")
        else:
            linhas_atualizadas.append(linha)

    if not produto_encontrado:
        print(f"Produto '{produto}' não encontrado no estoque.")
            

    with open('Trabalho Ecommerce AED1/estoque.csv', 'w') as estoque:
        estoque.writelines(linhas_atualizadas)

def adicionar(produto, quantidade, menu):
    with open('Trabalho Ecommerce AED1/estoque.csv', 'r') as estoque:
        linhas = estoque.readlines()
        if menu == 'add produto':
            repetido = False
            for linha in linhas:
                estoque = linha.split(',')[0]
                if produto == estoque:
                    print('Esse produto já está no estoque caso queira adionar mais\nquantidades, por favor selecionar add quantidade no menu!')
                    repetido = True
                    break
            if not repetido: 
                if len(linhas) == 1:
                    linhas.append(f'{produto},{quantidade}')
                else:
                    linhas.append(f'\n{produto},{quantidade}')
                with open('Trabalho Ecommerce AED1/estoque.csv', 'w') as estoque:
                    estoque.writelines(linhas)
        elif menu == 'add quantidade':
            linhas_atualizadas = []
            for linha in linhas:
                estoque, nova_quantidade = linha.strip().split(',')
                if produto.lower() == estoque.lower():
                    numero = int(nova_quantidade)
                    numero += quantidade
                    nova_linha = (f'{estoque},{str(numero)}\n')
                    linhas_atualizadas.append(nova_linha)
                else:
                    linhas_atualizadas.append(linha)
                with open('Trabalho Ecommerce AED1/estoque.csv', 'w') as estoque:
                    estoque.writelines(linhas_atualizadas)