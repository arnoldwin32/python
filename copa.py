#Python 3
#Arnold
import random
def criaGrupos(lista):
    grupos = [];i=0;j=0
    while i < 8:
        grupos.append([])
        while j < 4:
            paisEscolhido = random.choice(lista)
            grupos[i].append(paisEscolhido)
            lista.remove(paisEscolhido)
            j+=1
        j = 0
        i+=1
    return grupos
def criaConfrontos(lista):
    i = 0
    j = 0
    confrontos = [];pares = []
    while i < len(lista):
        j=i +1
        while j < len(lista):
            confrontos.append(lista[i])
            confrontos.append(lista[j])
            j += 1
        i+=1
    i = 0
    j = 0
    while i < len(confrontos):
        pares.append([])
        pares[j].append(confrontos[i])
        pares[j].append(confrontos[i+1])
        j += 1
        i += 2
    return pares
def criaTbFaseGrupos(lista):
    i=0;j=0;resultados=[]
    while i < len(lista):
        resultados.append([])
        resultados[j].append(lista[i])
        resultados[j].append(lista[i+1])
        resultados[j].append(random.choice(range(0,5)))
        resultados[j].append(random.choice(range(0,5)))
        i+=2
        j+=1
    return resultados
def imprimir(tabela,argumento):
    i=0;j=0;letras = ['A','B','C','D','E','F','G','H'];fases = ['AS OITAVAS DE FINAL','AS QUARTAS DE FINAL','AS SEMIFINAIS','A GRANDE FINAL'];texto=""
    if argumento ==0:
        print('PAISES PARTICIPANTES')
        while i < len(tabela):
            print(tabela[i])
            i +=1
        i=0
    elif argumento ==1:
        print("IMPRIMINDO RESULTADOS DOS CONFRONTOS")
        while i < len(tabela):
            while j < len(tabela[i]):
                print('Jogo',i+1,'-',tabela[i][j][0],tabela[i][j][2],'x',tabela[i][j][3],tabela[i][j][1],end=' ')
                j+=1
            print()
            j=0
            i+=1
        i=0
        j=0
    elif argumento == 2:
        print('SORTEIO DOS GRUPOS')
        while i < len(tabela):
            print('GRUPO',letras[i])
            while j < len(tabela[i]):
                print(tabela[i][j])
                j +=1
            j=0
            print()
            i +=1
        i=0
        j=0
    elif argumento == 3:
        print("IMPRIMINDO CONFRONTOS:")
        for i in range(len(tabela)):
            for j in range(len(tabela[i])):
                print(tabela[i][j][0],'X',tabela[i][j][1])
    elif argumento == 4:
        print("IMPRIMINDO CLASSIFICAÇÃO FINAL DOS GRUPOS")
        for i in range(len(tabela)):
            if i % 4 == 0:
                print("GRUPO",letras[i//4])
                print("Pais","V","E","D","GP","GC","SG","P")
            print(tabela[i])
    elif argumento == 5:
        #print("CLASSIFICADOS PARA A PROXIMA FASE:")
        for i in tabela:
            print(i)
    elif argumento == 6:
        for i in tabela:
            if i[4] == 0 and i[5] == 0:
                texto = "{} {} x {} {}"
                print(texto.format(i[0],i[2],i[3],i[1]))
            else:
                texto = "{} {} ({}) x ({}) {} {}"
                print(texto.format(i[0],i[2],i[4],i[5],i[3],i[1]))
    print()
def classificacao(lista):
    tabela = [];i=0;j=0;k=0;temp=[]
    while i < len(lista):
        while j < len(lista[i]):
            temp.append([])
            #temp[i].append(lista[i][j])
            j +=1
        j=0
        i+=1
    i = 0
    j = 0
    while i < len(lista):
        while j < len(lista[i]):
            temp[k].append(lista[i][j])
            temp[k].append(0)
            temp[k].append(0)
            temp[k].append(0)
            temp[k].append(0)
            temp[k].append(0)
            temp[k].append(0)
            temp[k].append(0)
            k+=1
            j+=1
        j=0
        i+=1
    tabela = temp
    return tabela
def classificacaoFinal(lista):
    maior = 0;i=0;maiorSG=0;indice = 0;swap = []
    while len(lista) > 0:
        while i < len(lista):
            if lista[i][7] > maior:
                maior = lista[i][7]
                indice=i
            elif lista[i][7] == maior:
                if lista[i][6] > maiorSG:
                    maiorSG = lista[i][6]
                    indice=i
            i+=1
        swap.append(lista[indice])
        lista.pop(indice)
        i = 0
        indice = 0
        maior = 0
        maiorSG = 0
    #print(swap)
    return swap
def tabelaGeral(faseGrupos):
    i=0;j=0
    while i < len(faseGrupos):
        while j < len(faseGrupos[i]):
            print(faseGrupos[i][j])
            j+=1
        j=0
        i+=1
def classPrimeiraFase(lista):
    classificados = [];i=0
    while i < len(lista):
        #print(lista[i][0],'x',lista[i+1][0])
        classificados.append(lista[i][0])
        classificados.append(lista[i+1][0])
        i+=4
    return classificados
def criaMataMata(lista):
    i=0;j=1;k=0
    confrontos = []
    if len(lista) > 2:
        while i < len(lista):
            confrontos.append([])
            confrontos[k].append(lista[i])
            confrontos[k].append(lista[i+2])
            k+=1
            confrontos.append([])
            confrontos[k].append(lista[j])
            confrontos[k].append(lista[j+2])
            k+=1
            j+=4
            i+=4
    elif len(lista) == 2:
        confrontos.append([])
        confrontos[0].append(lista[0])
        confrontos[0].append(lista[1])
    else:
        confrontos.append(lista[0])
    return confrontos
def criaResultMataMata(lista):
    resultados = [];i=0;p1=0;p2=0
    if len(lista)> 1:
        while i < len(lista):
            lista[i].append(random.choice(range(0,5)))
            lista[i].append(random.choice(range(0,5)))
            lista[i].append(0)
            lista[i].append(0)
            i += 1
        i=0
        j=0
        while i < len(lista):
            if lista[i][2] > lista[i][3]:
                lista[i].append(lista[i][0])
            elif lista[i][2] == lista[i][3]:
                while p1 == p2:
                    p1 = random.choice(range(0,4))
                    p2 = random.choice(range(0,4))
                if p1 > p2:
                    lista[i].append(lista[i][0])
                else:
                    lista[i].append(lista[i][1])
                lista[i][4] = p1
                lista[i][5] = p2
                p1 = 0
                p2 = 0
            else:
                lista[i].append(lista[i][1])
            i+=1
    elif len(lista) == 1:
        lista[0].append(random.choice(range(0,5)))
        lista[0].append(random.choice(range(0,5)))
        lista[0].append(0)
        lista[0].append(0) 
        if lista[0][2] > lista[0][3]:
            lista[0].append(lista[0][0])
        elif lista[0][2] == lista[0][3]:
            while p1 == p2:
                p1 = random.choice(range(0,4))
                p2 = random.choice(range(0,4))
            if p1 > p2:
                lista[0].append(lista[0][0])
            else:
                lista[0].append(lista[0][1])
            lista[0][4] = p1
            lista[0][5] = p2
            p1 = 0
            p2 = 0
        else:
            lista[i].append(lista[i][1])
    resultados = lista
    return resultados
def vencedoresMataMata(lista):
    i=0;j=0;vencedores = [];terceiroLugar = []
    if len(lista)>1:
        while i < len(lista):
            vencedores.append(lista[i][len(lista[i])-1])
            i +=1
        if len(lista) == 2:
            terceiroLugar.append([])
            for i in range(len(lista)):
                if lista[i][0] == lista[i][6]:
                    terceiroLugar[0].append(lista[i][1])
                else:
                    terceiroLugar[0].append(lista[i][0])
            
            
            print("DISPUTA DO TERCEIRO LUGAR:")
            imprimir((criaResultMataMata(terceiroLugar)),6)
    else:
        vencedores.append(lista[0][6])
    return vencedores
def classificar(selecoes,faseGrupos):
    i=0;j=0;k=0
    while i < len(faseGrupos):
        while j < len(faseGrupos[i]):
            while k < len(selecoes):
                if faseGrupos[i][j][0] in selecoes[k]:
                    if faseGrupos[i][j][2] > faseGrupos[i][j][3]:
                        selecoes[k][1]+=1
                        selecoes[k][7]+=3
                    elif faseGrupos[i][j][2] == faseGrupos[i][j][3]:
                        selecoes[k][2]+=1
                        selecoes[k][7]+=1
                    else:
                        selecoes[k][3]+=1
                    selecoes[k][4]+=faseGrupos[i][j][2]
                    selecoes[k][5]+=faseGrupos[i][j][3]
                    selecoes[k][6]=selecoes[k][4]-selecoes[k][5]
                    
                if faseGrupos[i][j][1] in selecoes[k]:
                    if faseGrupos[i][j][2] < faseGrupos[i][j][3]:
                        selecoes[k][1]+=1
                        selecoes[k][7]+=3
                    elif faseGrupos[i][j][2] == faseGrupos[i][j][3]:
                        selecoes[k][2]+=1
                        selecoes[k][7]+=1
                    else:
                        selecoes[k][3]+=1
                    selecoes[k][4]+=faseGrupos[i][j][3]
                    selecoes[k][5]+=faseGrupos[i][j][2]
                    selecoes[k][6]=selecoes[k][4]-selecoes[k][5]
                k+=1
            k=0
            j+=1
        j=0
        i+=1
    return selecoes

def main():
    paises = ['Rússia','Brasil','Irã','Japão','México','Bélgica','Coreia do Sul','Arábia Saudita','Alemanha','Inglaterra','Espanha','Nigéria','Costa Rica','Polônia','Egito','Islândia','Sérvia','França','Portugal','Argentina','Colômbia','Uruguai','Panamá','Senegal','Marrocos','Tunísia','Suíça','Croácia','Suécia','Dinamarca','Austrália','Peru']
    fases = ['FASE DE GRUPOS','OITAVAS DE FINAL','QUARTAS DE FINAL','SEMIFINAIS','FINAL']
    grupos = [];confrontos = [];faseGrupos=[];selecoes = [];classfinal = [];lista = [];listaclassificados = [];vencedores = [];i=0
    #imprimir(paises,0)
    grupos = criaGrupos(paises)
    imprimir(grupos,2)
    while i < len(grupos):
        confrontos.append(criaConfrontos(grupos[i]))
        i +=1
    i=0
    j=0
    imprimir(confrontos,3)
    while i < len(confrontos):
        while j < len(confrontos[i]):
            faseGrupos.append(criaTbFaseGrupos(confrontos[i][j]))
            j+=1
        j = 0
        i +=1
    i=0
    j=0
    imprimir(faseGrupos,1)
    selecoes = classificar(classificacao(grupos),faseGrupos)
    #print(selecoes)
    while i < len(selecoes):
        while j < 4:
            classfinal.append(selecoes[i + j])
            j+=1
        lista += classificacaoFinal(classfinal)
        i += j    
        j=0
    i=1
    imprimir(lista,4)
    print(fases[0])
    listaclassificados = (classPrimeiraFase(lista))
    imprimir(listaclassificados,5)
    while i < 5:
        print(fases[i])
        vencedores = criaResultMataMata(criaMataMata(listaclassificados))
        imprimir(vencedores,6)
        #print(vencedores)
        listaclassificados = vencedoresMataMata(vencedores)
        #imprimir(listaclassificados,5)
        i+=1
    print("CAMPEÃO DO MUNDO:",listaclassificados[0])
    return 0

if __name__ == "__main__":
    main()