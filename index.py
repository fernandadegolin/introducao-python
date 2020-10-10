******* Exercicio 1 *******

valor = 25
fornecedor = valor / 2
brindes = int(input('Quantos brindes você vai fazer? '))

print(f'O valor que você vai precisar dar de entrada será {brindes * fornecedor:.2f}')



******* Exercicio 2 *******

convidados = int(input('Quantos covidados virão? '))

refri = .4 * convidados
refriPreco = 4 * refri

coxinha = 10 * convidados
coxinhaPreco = .5 * coxinha

print(f'Litros de Refri {refri}')
print(f'Valor de Refri: R${refriPreco:.2f}')

print(f'Quantas unidades de Coxinha {coxinha}')
print(f'Valor de Coxinhas: R${coxinhaPreco:.2f}')

print(f'Você terá que separar R${refriPreco + coxinhaPreco:.2f} para o coffee')
