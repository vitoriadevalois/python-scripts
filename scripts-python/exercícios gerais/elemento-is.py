#Programa utilizando .IS para receber resposta true or false sobre a variavél.
a = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É númerico? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())