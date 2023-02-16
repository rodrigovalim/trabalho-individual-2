listacand = {}
listaaprovado1 = {}
listaaprovado2 = {}


palavrachave1 = ['python','programação', 'desenvolvimento']
palavrachave2 = ['analise de dados', 'dados','sql']


sair = 1
while (sair != 0): # guardando os candidatos
    nome = input('Nome do candidato: ')
    vaga = int(input('Digite qual vaga você deseja se canditatar? (vaga 1) ou (vaga 2): '))
    resumo = input('Digite um resumo de suas qualificações: ')
    listacand[nome] = {'vaga' : vaga, 'resumo': resumo}

    sair = int(input('Digite "0" para sair: '))



def palavrachave():

    for nome, cont in listacand.items():  # adicionando os candidatos aprovados
        if cont['vaga'] == 1 and 'python' in cont['resumo']  or 'programação' in cont['resumo'] or 'desenvolvimento ' in cont['resumo']:
            listaaprovado1[nome] = cont['resumo']
        elif cont['vaga'] == 2 and 'analise de dados' in cont['resumo'] or 'dados' in cont['resumo'] or 'sql' in cont['resumo']:
            listaaprovado2[nome] = cont['resumo']    

#print(listacand)
#print(len(listacand))

palavrachave()
 

print('Quantidade de candidatos: \n',len(listacand)) # imprimindo as informações
print('')
print('Quantidade de aprovados para a vaga 1: \n',len(listaaprovado1))
print(listaaprovado1)
print('')
print('Quantidade de aprovados para a vaga 2: \n',len(listaaprovado2))
print(listaaprovado2)