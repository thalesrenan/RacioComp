titulo = 'Seja bem-vindo(a) a Loja do '
primeironome = 'Thales'
segundonome = 'Renan'
sobrenome = 'Miranda'
ultimonome = 'Nakalski'
nomecompleto = primeironome + ' ' + segundonome + ' ' + sobrenome + ' ' + ultimonome
print(titulo + nomecompleto)
print('Para análise de crédito digite:')
cargo = input('Seu cargo: ')
salario = input('Seu salário: ')
nasc = input('Seu ano de nascimento: ')
print(f'Cargo: {cargo}, '
      f'Salário: R${salario}, '
      f'Ano de Nascimento: {nasc}.')
idade = 2020 - int(nasc)
print(f'Idade: {idade}')
limite = int(salario)*(int(idade)/1000)+100
print(f'Você pode gastar: R${limite}')
produto = input('Digite o nome do produto: ')
valor = input('Digite o preço do produto: ')
if int(valor) < int(limite)*0.6:
    print('Liberado!')
elif int(limite)*0.6 < int(valor) < int(limite)*0.9:
    print('Liberado ao parcelar em até 2 vezes.')
elif int(limite)*0.9 < int(valor) < int(limite):
    print('Liberado ao parcelar em 3 vezes ou mais.')
else:
    print('Bloqueado')

if idade < int(valor) < len(nomecompleto):
    desconto = len(primeironome)
    print(f'Você tem direito a um desconto de R${desconto}')
    novovalor = int(valor) - desconto
    print(f'Valor do produto com desconto: R${novovalor}')
