#Crie um programa que leia em metros, mas dê o resultado em km, hm, dam, dm, cm, mm

metros= float(input('Uma distância em metros:'))
print('A medida de {}m corresponde a:'. format(metros))
quilometros= metros / 1000
hectometros= metros /100
decametros= metros / 10
decimetros= metros * 10
centimetros= metros * 100
milimetros= metros * 1000

print('{}km \n{:.0f}hm\n{:.0f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(quilometros,hectometros,decametros,decimetros,centimetros,milimetros))