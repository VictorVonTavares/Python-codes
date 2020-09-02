n = input("Digite uma quantidade de numeros\n");
ni = int(n)
x = 0
i = 0
vetor = []
v1 = 0
vetor2 = []
z = 0
w = 1
vetor3 = [22]
vetor4 = []
vetor5 = []
while x < ni:
    numero = input("Digite um numero\n")
    n2 = int (numero)
    vetor.append(n2)
    x = x + 1;
    int (x)

while z < ni: 
    for y in vetor:
        if y == max(vetor, key=int):
            vetor3[0] = y

            if len(vetor3) > 1:
                vetor5[0] = vetor3[0]
                vetor2 = vetor2 + vetor5
                vetor.remove(y)
            
            else:
                vetor2 = vetor2 + vetor3
                vetor.remove(y)
    
    z = z + 1


while w <= ni:
    for y in vetor2:
        if y == vetor2[len(vetor2) - w ]:
            vetor3[0] = y
            vetor4 = vetor4 + vetor3
    w = w + 1

for x in vetor4:
    if vetor4.count(x)>2:
        vetor4.remove(x)

for x in vetor4:
    if vetor4.count(x) >2:
        vetor4.remove(x)

print (vetor4)