n = input("Digite uma quantidade de numeros\n");
ni = int(n)
x = 0
i = 0
vetor = []
v1 = 0
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
    if vetor[controle] > vetor[controle -1] or vetor[controle] == vetor[controle-1]:
        contador= contador + 1
    controle = controle + 1
    v1 = v1 + 1

if contador == v2 -1 :
    print('SIM')
else:
    print('NAO')

