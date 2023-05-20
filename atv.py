print('Atividade 1')
print('')

while True:
  try:
    nota = float(input('Digite a Nota: '))
    if nota > 10 or nota < 0:
      print('Valor inválido a nota deve estar entre 1 e 10.')
    else:
      break
  except ValueError:
    print('Valor inválido.')
    
print(f'O valor digitado foi {nota}.')   

############
print('')
print('-'*30)
print('')
print('Atividade 2')
print('')

n1 = float(input('Primeiro lado do triângulo: '))
n2 = float(input('Segundo lado do triângulo: '))
n3 = float(input('Terceiro lado do triângulo: '))
print('='*35)
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
  if n1 > 0 and n2 > 0 and n3 > 0:
    if n1 == n2 and n1 == n3:
      print('Triângulo Equilátero.')
    elif n1 == n2 or n1 == n3 or n2 == n3:
      print('Triângulo Isósceles.')
    elif n1 != n2 and n1 != n3 and n2 != n3:
      print('Triângulo Escaleno.')
else:
  print('Não compõem triângulo.')
  

################
print('')
print('-'*30)
print('')
print('Atividade 3')
print('')

numeros = []
while True:
    numero = int(input("Digite um número inteiro positivo ou -1 para encerrar: "))
    if numero == -1:
        break
    numeros.append(numero)

quantidade = len(numeros)
soma = sum(numeros)
media = soma / quantidade
maior = max(numeros)
menor = min(numeros)
print('='*30)
print(f'Foram digirados {quantidade} números inteiros positivos.')
print(f'A soma dos números é: {soma}')
print(f'A média dos números é: {media}')
print(f'O menor número é: {maior}')
print(f'O maior número é: {menor}')

#############
print('')
print('-'*30)
print('')
print('Atividade 4')
print('')

def pos(j):
 if j > 0:
  return 'P'
  
 else:
    return 'N'
j = int(input("Digite um número: "))
print(pos(j))
