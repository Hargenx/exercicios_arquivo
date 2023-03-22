def exercicio02():
  arquivo = './lista.txt'
  with open(arquivo, 'a') as agenda:
    agenda.write('\nRaphael')
  with open(arquivo, 'r') as agenda:
    for nomes in agenda:
      print(nomes, end='')
