## Counting Sort

def maior(vet):
    maior = vet[0]

    for e in vet:
        if e > maior:
            maior = e

    return maior


def criar_vetor_ocorrencias(vet):

    maiorValor = maior(vet)

    vetOcorr = [0] * (maiorValor + 1)

    return vetOcorr

def calcular_ocorrencias(vet,vetOcorr):

    for e in range(len(vet)):
        vetOcorr[vet[e]] = vetOcorr[vet[e]] + 1

    return vetOcorr

def ordenar_vetor(vetOcorr):
    vetOrd = []
    for e in range(len(vetOcorr)):
        if vetOcorr[e] != 0:
            i = 0
            while i < vetOcorr[e]:
                vetOrd.append(e)
                i += 1
    return vetOrd

vet = [1,1,3,6,2,2,1,1]

vetOcorr = criar_vetor_ocorrencias(vet)

vetOcorr = calcular_ocorrencias(vet,vetOcorr)

resposta = ordenar_vetor(vetOcorr)

print(vet)
print(vetOcorr)
print(resposta)

