def exercicio01():
  agenda = open('lista.txt', 'x')
  nome = ['Sara\nCarol\nGilson\nVinicius']
  agenda.writelines(nome)
  agenda.close()