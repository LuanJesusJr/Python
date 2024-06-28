

n1 = int(input('Digite um valor: '))
print('\n')
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {} a multiplicação deu {} e a divisão {:.3f}'.format(s, m, d))
print('\n')
print('Divisão inteira é {} e a potência {}'.format(di, e))