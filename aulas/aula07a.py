nome = input('Qual é o seu nome? ')
print('Prazer em te conhercer {:20}!'.format(nome))   #Para escrever a string em 20 espaços
print('Prazer em te conhercer {:>20}!'.format(nome))   #Para escrever a string em 20 espaços e alinhada a direita
print('Prazer em te conhercer {:<20}!'.format(nome))   #Para escrever a string em 20 espaços e alinhada a esquerda
print('Prazer em te conhercer {:^20}!'.format(nome))   #Para escrever a string em 20 espaços e centralizada
