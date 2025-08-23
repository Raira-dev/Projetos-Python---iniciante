num_alunos = int(input('Informe a quantidade de alunos (mínimo 3): '))

while num_alunos < 3:
    num_alunos = int(input('Informe a quantidade de alunos (mínimo 3): '))
    nomes = []
    notas = []

for aluno in range(num_alunos):
    nome = input(f'Informe o nome {aluno + 1}: ')
    nota_final = float(input('Informe a nota final (número entre 0 e 10): '))

while not (nota_final >= 0 and nota_final <= 10):
    nota_final = float(input('Informe a nota final (número entre 0 e 10: '))

nomes.append(nome)
notas.append(nota_final)
if nota_final:
    media_geral = sum(notas)/len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    aluno_maior_nota = nomes[notas.index(maior_nota)]
    aluno_menor_nota = nomes[notas.index(menor_nota)]
    alunos_acima_media = sum(1 for nota_finais in notas if nota_finais > media_geral)

print('Resultados: \n')
print(f'Média geral da turma: {media_geral:.2f}')
print(f'Aluno com maior nota: {aluno_maior_nota} ({maior_nota:.2f})')
print(f'Aluno com menor nota: {aluno_menor_nota} ({menor_nota:.2f})')
print(f'Alunos acima da média: {alunos_acima_media}')
