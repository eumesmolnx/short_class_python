def assassino():
    pontos = 0
    pergunta = 1
    while pergunta <= 5:
        resposta = input(f'Pergunta {pergunta}: ')
        if resposta == 'sim':
            pontos += 1
        pergunta += 1
    if pontos == 5:
        print('Assassino')
    elif pontos == 4 or pontos == 3:
        print('Cúmplice')
    elif pontos == 2:
        print('Suspeito')
    else:
        print('Liberado')


assassino()
