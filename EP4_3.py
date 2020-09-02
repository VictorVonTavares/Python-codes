n = input("Digite uma quantidade de numeros\n");
ni = int(n)
x = 0
i = 0
vetor = []
vetor2 = [0]
v1 = 1
controle = 1
contador = 0

while x < ni:
    numero = input("Digite um numero\n")
    n2 = int (numero)
    vetor.append(n2)
    x = x + 1;
    int (x)
    print (vetor)

v2 = len(vetor)

while v1 < (v2 - 1):
    if vetor[controle] > vetor [controle -1 ] and vetor[controle] > vetor[controle +1] or vetor[controle] == vetor [controle -1 ] == vetor[controle]:
        vetor2.append (vetor[controle])
    if vetor[controle +1] > vetor[controle] and vetor[controle + 1] > vetor[controle -1]:
        vetor2.append (vetor[controle + 1])
    if vetor[controle - 1] > vetor[controle] and vetor[controle - 1] > vetor[controle  + 1]:
        vetor2.append (vetor[controle - 1])
    controle = controle + 1
    v1 = v1 + 1

vetor2.append(0)

print (vetor2)

v1 = 0
controle = 0

while (v1 < v2):
    print(vetor2[controle])
    v1 = v1 + 1
    controle = controle + 1