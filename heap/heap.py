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

def montar_max_heap(vet,tam):
    ultimo = int((tam/2) - 1)

    while(ultimo >= 0):
        
        vet = max_heapify(vet,ultimo,tam)

        ultimo = ultimo - 1

    return vet

def montar_min_heap(vet,tam):
    ultimo = int((tam/2) - 1)

    while(ultimo >= 0):
        
        vet = min_heapify(vet,ultimo,tam)

        ultimo = ultimo - 1

    return vet

def aumentar_chave_max_heap(heap,tam,pos,knew):

    heap[pos] = knew

    pai = int((pos - 1) / 2)

    if pai < 0:
        pai = 0

    while(pos > 0 and heap[pai] > knew):
        troca(heap,pai,pos)
        pos = pai
        pai = int((pos - 1) / 2)

    return heap

def insere_chave_nova_max_heap(heap,tam,chave):
    
    heap.append(chave)
    heap = aumentar_chave_max_heap(heap,len(heap),len(heap) - 1, chave)

    return heap

def aumentar_chave_min_heap(heap,tam,pos,knew):

    heap[pos] = knew

    pai = int((pos - 1) / 2)

    if pai < 0:
        pai = 0

    while(pos > 0 and knew < heap[pai]):
        troca(heap,pai,pos)
        pos = pai
        pai = int((pos - 1) / 2)

    return heap

def insere_chave_nova_min_heap(heap,tam,chave):
    
    heap.append(chave)
    heap = aumentar_chave_min_heap(heap,len(heap),len(heap) - 1, chave)

    return heap

heap = eval(input())

while heap != []:

    posicao = int(input())
    novo = int(input())

    if posicao == len(heap):
        heap = insere_chave_nova_min_heap(heap,len(heap),novo)
    else:
        heap = aumentar_chave_min_heap(heap,len(heap),posicao,novo)

    print(heap)

    heap = eval(input())

    