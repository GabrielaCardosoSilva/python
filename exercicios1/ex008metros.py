m = float(input('Distância em metros: '))

print('A medida de {:.1f}m corresponde a:'.format(m))
print('{}Km'.format(m/1000))
print('{}hm'.format(m/100))
print('{}dam'.format(m/10))
print('{}dm'.format(m*10))
print('{}cm'.format(m*100))
print('{}mm'.format(m*1000))