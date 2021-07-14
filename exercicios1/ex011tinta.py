largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura

print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m2.\nPara pintar essa parede, você precisará de {:.4f}l de tinta'.format(altura, largura, area, area/2))
