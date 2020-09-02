n = input("Digite uma quantidade de numeros\n");
n1 = int(n)
x = 0
i = 0
vetor = []
v1 = 0
controle = 0
contador = 0

while x < n1:
    numero = input("Digite um numero\n")
    n2 = int (numero)
    vetor.append(n2)
    x = x + 1;
    int (x)
    print (vetor)

v2 = len(vetor)

while v1 < (int(n1/2)):

    if vetor[controle] == vetor[len(vetor) - 1 - controle]:
        contador = contador + 1
    controle = controle + 1
    v1 = v1 + 1

if contador == int(n1/2):
    print ('SIM')
else:
    print('NAO')


