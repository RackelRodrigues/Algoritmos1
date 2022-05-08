num = 10
filmes = [0] * num
usuario1 = [0] * num
usuario2 = [0] * num

nome1 = input('1° usuario, Qual o seu nome? ')
nome2 = input('2° usuario, Qual o seu nome? ')

def operador():
 print('Operador, informe os nomes dos filmes! ')
 for i in range(num):
  filmes[i] = input(f'Adicione o {i + 1}o filme: ')
  print('Estes são os filmes no catálogo:' ,filmes)

def usuario_um():
 for i in range(num):
  usuario1[i] = input(f'{nome1} você já assistiu ao filme {filmes[i]}? ')
 for i in range(num):
  if usuario1[i] == 's':
   usuario1[i] = True
  else:
   usuario1[i] = False

def usuario_dois():
 for i in range(num):
  usuario2[i] = input(f'{nome2} você já assistiu ao filme {filmes[i]}? ')

for i in range(num):
 if usuario2[i] == 's':
  usuario2[i] = True
 else:
  usuario2[i] = False

def comparacao():
 print(f'Recomendações para {nome1}: ')
for i in range(num):
 if usuario1[i] == False and usuario2[i] == True:
  print(filmes[i])
  print(f'Recomendações para {nome2}: ')
for i in range(num):
 if usuario2[i] == False and usuario1[i] == True:
  print(filmes[i])

operador()
usuario_um()
usuario_dois()
comparacao()
