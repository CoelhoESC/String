# JOIN
string = 'O Brasil é penta'
lista = string.split(' ')
string2 = ' '.join(lista)  # Estou juntando as palavras separadas da lista, usando ','

print(string)
print(lista)
print(string2)

# Enumerate

for indices, valor in enumerate(lista):
    print(indices, valor)

# lista dentro de lista
lista_1 = [[1, 2], [3, 4], [5, 6]]
print('Lista dentro de lista')
for valor in lista_1:
    print(valor, valor[0], valor[1])
print()
for indice, valor in enumerate(lista_1):
    print(indice, valor)

# Posso separar usando Join
Nome = 'Everton'
Separado = '-'.join(Nome)
lista = []
for letra in Separado:
    if letra != '-':
        lista.append(letra)
print(lista)