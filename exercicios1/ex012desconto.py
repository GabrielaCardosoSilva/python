product = float(input('Qual o valor so produto? R$'))
print('o produto que custava R${:.2f}, na promoção com desconto de 5% irá custar {:.2f}'.format(product, product - (product*5)/100))