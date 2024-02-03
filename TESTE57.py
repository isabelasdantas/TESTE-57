sexo = str(input('Escolha seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Digite seu sexo [F/M]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
