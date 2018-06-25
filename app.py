# Abrimos o documento e lemos todas as informações
sentilexpt = open("SentiLex-lem-PT01.txt", 'r')

# Criamos um dicionário para receber as informações
dic_palavra_polaridade = {} 

# Neste trecho atribuímos a cada palavra uma Polaridade
for i in sentilexpt.readlines(): 
    pos_ponto = i.find('.')
    palavra = (i[:pos_ponto])
    pol_pos = i.find('POL')
    polaridade = (i[pol_pos+4:pol_pos+6]).replace(';','')
    dic_palavra_polaridade[palavra] = polaridade

#print(dic_palavra_polaridade)
#print(dic_palavra_polaridade.get('abandonado'))


def Pontuação_sentimento(frase):
    frase = frase.lower()
    l_sentimento = []

    for p in frase.split():
        l_sentimento.append(int(dic_palavra_polaridade.get(p, 0)))

    pontuacao = sum(l_sentimento)
    if pontuacao > 0:
        return 'Positivo, Pontuação: {}'.format(pontuacao)
    elif pontuacao == 0:
        return 'Neutro, Pontuação:{}'.format(pontuacao)
    elif pontuacao < 0:
        return 'Negativo, Pontuação:{}'.format(pontuacao)


frase = Pontuação_sentimento('Eu estou muito feliz hoje, porém, triste com a politica')
print(Pontuação_sentimento(frase))

# Consultar polaridades 
#dic_palavra_polaridade.get('feliz')
#dic_palavra_polaridade.get('triste')
