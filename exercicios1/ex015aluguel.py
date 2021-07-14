# Aluguel de carros:
# 1 dia = R$60,00
# 1km = 0,15

days = int(input('Quantos dias de uso? '))
km = float(input('Quantos km rodados? '))

price = days*60 + km*0.15

print('O total a pagar é de R${:.2f}'.format(price))
