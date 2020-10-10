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


******* Exercicio 3 *******
nome1, nome2 = input('qual seu nome completo? ').split()
print(nome1)
print(nome2)

qual seu nome completo? fe degolin
fe
degolin


******* Exercicio 4 *******
rosa, roxo, azul = map(int, input("Informe separado por virgulas quantas participantes por cor: ").split(","))
total_participantes = rosa + roxo + azul

porcentagem_rosa = rosa / total_participantes * 100
porcentagem_roxo = roxo / total_participantes * 100
porcentagem_azul = azul / total_participantes * 100

print(f"{porcentagem_rosa:.2f} % de pessoas preferem rosa.")
print(f"{porcentagem_roxo:.2f} % de pessoas preferem roxo.")
print(f"{porcentagem_azul} % de pessoas preferem azul.")

Informe separado por virgulas quantas participantes por cor: 10, 20, 30
16.67 % de pessoas preferem rosa.
33.33 % de pessoas preferem roxo.
50.0 % de pessoas preferem azul.
