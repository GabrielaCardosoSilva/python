from math import cos, sin, tan, radians

angle = float(input('Digite o ângulo: '))
ra = radians(angle)

print('O ângulo de {:.2f} tem:'.format(angle))
print('Seno: {:.2f}'.format(sin(ra)))
print('Cosseno {:.2f}'.format(cos(ra)))
print('tangente: {:.2f}'.format(tan(ra)))