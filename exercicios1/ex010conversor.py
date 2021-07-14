x = float(input('Informe o valor que você quer converter: R$'))

print('Com R${:.2f} você pode comprar US${:.2f}'.format(x, x/5.21))