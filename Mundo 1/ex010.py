#Crie um programa de conversão de moeda

real= float(input('Digite o valor:'))

dolar = real / 6.29 #USD  #$
euro= real / 6.39 #EUR  #€
libra = real / 7.39 #GBP  #£
iene = real / 0.0394 #JPY  #¥

print('-'*20)
print('Dolar(USD) = ${:.2f}'.format(dolar))
print('Euro(EUR) = €{:.2f}'.format(euro))
print('Libra(GBP) = £{:.2f}'.format(libra))
print('Iene(jpy) = ¥{:.2f}'.format(iene))
print('-'*20)