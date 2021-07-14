salary = float(input('Qual o salario do funcionário? R$'))
print('Um funcionário que ganhava R${:.2f}, com aumento de 15%, irá ganhar R${:.2f}'.format(salary, salary + salary*0.15))