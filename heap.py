def troca(vet, a, b):
    aux = vet[a]
    vet[a] = vet[b]
    vet[b] = aux
    return vet


def max_heapify(vet,raiz,tam):
    maior = raiz

    esq = 2 * raiz + 1

    if(esq < tam and vet[esq] > vet[maior]):
        maior = esq

    dir = 2 * raiz + 2

    if(dir < tam and vet[dir] > vet[maior]):
        maior = dir

    if maior != raiz:
        vet = troca(vet, raiz, maior)
        max_heapify(vet,maior,tam)

    return vet

def min_heapify(vet,raiz,tam):
    menor = raiz

    esq = 2 * raiz + 1

    if(esq < tam and vet[esq] < vet[menor]):
        menor = esq

    dir = 2 * raiz + 2

    if(dir < tam and vet[dir] < vet[menor]):
        menor = dir

    if menor != raiz:
        vet = troca(vet, raiz, menor)
        min_heapify(vet,menor,tam)

    return vet

caso = eval(input())

while caso != []:

    caso = min_heapify(caso,0,len(caso))

    print(caso)

    caso = eval(input())