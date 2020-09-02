n = input("Insira a quantidade de alunos \n")
ni = int(n)
x = 0
i = 0
y = 0
vetor2 = []
mediafinal = 0

while x < ni:
        aluno = input("Digite o nome do aluno \n")
        vetor1 = []
        vetor1.append(aluno)
        media = input("Digite a media do aluno\n")
        media1 = int(media)
        vetor1.append(media1)
        vetor2.append(vetor1)
        print (vetor2)
        x = x +1
        mediafinal = mediafinal + media1


mediafinal = mediafinal/ni

for x in vetor2:
    if mediafinal < x[1]: 
        print(x[0])
