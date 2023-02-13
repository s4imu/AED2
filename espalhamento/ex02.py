import math

def f_espalhamento(k,m):
    return math.floor(k % m)

def f_sondagem_linear(k,i,m):
    hk = f_espalhamento(k,m)

    return math.floor((hk + i) % m)

def f_criar_tabela(tam):
    tabela = [None] * tam

    count = 0

    while count < tam:

        tabela[count] = -1
        count = count + 1

    return tabela

def f_inserir_valores_na_tabela(tab,num_valores):

    count = 0

    while count < num_valores:

        string = (input())

        valor = f_calcular_chave(string)

        pos = f_espalhamento(valor,len(tab))

        if tab[pos] == -1:
            tab[pos] = string
        else:
            num_colisoes = 1

            while num_colisoes > 0:
                pos = f_sondagem_linear(valor,num_colisoes,len(tab))

                if tab[pos] == -1:
                    tab[pos] = valor
                    num_colisoes = 0
                else:
                    num_colisoes = num_colisoes + 1

        count = count + 1

    return tab

def f_imprimir_resposta(tab):
    for i, valor in enumerate(tab):
        if tab[i] != -1:
            print("%d: %s" % (i, tabela[i]))

def f_calcular_chave(str):
    res = 0

    for c in str:
        res = ord(c) + res

    return res

if __name__ == '__main__':

    tam = int(input())
    num_valores = int(input())

    tabela = f_criar_tabela(tam)

    tabela = f_inserir_valores_na_tabela(tabela,num_valores)

    f_imprimir_resposta(tabela)