n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break #A operação irá dar um break, não irá somar o 999 pois o 999 vira a Flag de Stop
    s += n
print(f'A soma vale {s}')