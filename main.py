print('Seja bem-vindo(a) a Loja de Peças do Thales')
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

if idade <= int(valor) <= 29:
    print('Você tem direito a um desconto de R$6.00')
    novovalor = int(valor)-6
    print(f'Valor do produto com desconto: R${novovalor}')
