arquivo = 'listaMercado.txt'


def add():
  item = input('Digite um item: ')
  escreve_item(item)


def escreve_item(item):
  lista = open(arquivo, 'a')
  lista.write(item + '\n')
  lista.close()


lista = ['Banana', 'Melancia', 'Manga', 'Uva']

with open(arquivo, 'w+', encoding='UTF-8') as compras:
  #Pulando linha
  for i in lista:
    compras.write(i + '\n')
  #Tirar linha em branco
  compras.seek(0, 0)
  for linha in compras:
    print(linha.strip())

add()
condicao = True
while condicao:
  resposta = input('Gostaria de digitar mais um item?')
  if resposta == 'sim' or resposta == 'SIM':
    add()
  else:
    condicao = False
