#Dissecando uma variavel

a=input('Digite algo:')
print('O tipo primitivo desse valor é',type(a))
print('Tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())