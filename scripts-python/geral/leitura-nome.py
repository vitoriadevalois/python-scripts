#Programa para saber quantas cidades começam com a palavra "Santo"
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5] == 'Santo')