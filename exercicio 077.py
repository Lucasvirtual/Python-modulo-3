tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR', 'FUTURO')
for palavras in tupla:
    vogais = ''
    for contador in range(0, len(palavras)):
        vogal = palavras[contador].lower()
        if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':
            vogais += vogal + ' '
    print(f'Na palavra \033[94m{palavras}\033[m Temos: \033[95m{vogais}\033[m')