num = int(input('Informe um número: '))
print(f'Analisando o número {num}')
print(f'Unidade: {num // 1 % 10}')  # divide o número por 1 e pega o resto da divisão por 10 (sendo apenas a unidade)
print(f'Dezena: {num // 10 % 10}')  # divide o número por 10 e pega o resto da divisão por 10 (sendo apenas a dezena)
print(f'Centena: {num // 100 % 10}')  # divide o número por 100 e pega o resto divisão por 10 (sendo apenas a centena)
print(f'Milhar: {num // 1000 % 10}')  # divide o número por 1000 e pega o resto da divisão por 10 (sendo apenas o milhar)
