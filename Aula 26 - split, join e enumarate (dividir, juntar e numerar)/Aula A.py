"""
Split, Join e Enumarate
- Split: Dividir um Str - Só divide se eu indicar o separador ex: ,split(' ', 5) ele pode parar de dividir na indices"
- Join: Juntar uma lista # str
- Enumarate: Enumerar elementos da lista # list -> Para objetos interaveis
"""
string = 'O Brasil é é é é é é pais do futebol, o Brasil é penta'
lista_1 = string.split(' ', 4)  # Formei uma lista separando as palavras, dizendo aonde termina a separação.
lista_2 = string.split(',')  # Separou em dua frases por causa da ','
print(lista_1)
print(lista_2)

# for valor in lista_1:
#     print(f'A palavra "{valor}" apareceu {lista_1.count(valor)}x na frase!')


contagem = 0
for valor in lista_1:
    quantidade_vezes = lista_1.count(valor)

    if quantidade_vezes > contagem:  # Verificando qual a palavra que apareceu mais!
        contagem = quantidade_vezes  # Se tiver um palavra que apareceu mais vezes, ele ira att a contagem
        palavra = valor

print(f'A palavra que mais apareceu foi "{palavra}" com {contagem}x')

for valor in lista_2:
    print(valor.strip().capitalize())
