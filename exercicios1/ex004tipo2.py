x = input('Digite algo: ')

print('tipo de dado: {}'.format(type(x)))
print('Possui apenas espaços:: {}'.format(x.isspace()))
print('É numérico: {}'.format(x.isnumeric()))
print('É alfabético: {}'.format(x.isalpha()))
print('É alfanumérico: {}'.format(x.isalnum()))
print('Tem apenas letras maiúsculas: {}'.format(x.isupper()))
print('Tem apenas letras minúsculas: {}'.format(x.islower()))
print('Está capitalizada: {}'.format(x.istitle()))
print('Impressão possível: {}'.format(x.isprintable))

# Obs.: Neste exemplo, X é um objeto e oq vem a seguir são métodos.