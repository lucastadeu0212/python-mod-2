
def calcular_media(valores):
    return sum(valores) / len(valores)

notas = []

for i in range(4):
    nota = float(input(f'Digite a nota{i+1}: '))
    notas.append(nota)

print('Sua Média é ',calcular_media(notas))
'''
def calcular_media(valores):
    return sum(valores) / len(valores)

notas = [5, 8, 6, 10]

print(calcular_media(notas))
'''