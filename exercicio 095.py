todos = []
keep = 's'

while 's' in keep:
    
    jogad = {}
    nome = input('Nome do jogador: ').title()
    
    if len(nome) < 13:
        for n in range(25 - 2 * len(nome)):
            nome += ' '
    
    jogad['nome'] = nome
    jogos = int(input(f'{nome.strip()} jogou quantas partidas? '))
    jogad['gols'] = gols = list()
    tot = cont = 0
    
    for n in range(jogos):
        a = (int(input(f'Gols de {nome.strip()} na {n+1}ª partida: ')))
        gols.append(a)
        tot += jogad['gols'][n]
        
        if a > 0:
            cont += 1
    
    jogad['total'] = tot
    jogad['cont'] = cont
    
    todos.append(jogad)
    keep = input('Adicionar mais jogadores (S/N)? ').strip().lower()
    print('\n', '-='*30, '\n')

print(f'{"nº":<0}{" Nome":<10}{"       Gols     ":<10}{"   Total":>0}{"       Jogos"}')
print('                                       de Gols     com Gol')

for i, v in enumerate(todos):
    print(f'{i+1:<0}', end='  ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('\n', '-='*30, '\n')

while True:
    print('\n', '-' * 40)
    busca = int(input('nº do jogador que você deseja saber mais informações (999 para encerrar): '))
    
    if busca == 999:
        break #sai do laço while
    
    if busca <= 0 or busca > len(todos):
        print(f'Valor inválido. Digite um nº inteiro entre 1 e {len(todos)}')
        continue #volta para o começo do laço while
    
    print(f'O jogador {todos[busca - 1]["nome"].strip()} fez {todos[busca - 1]["total"]}', end=' ')
    print(f'gol(s) e jogou {len(todos[busca - 1]["gols"])} partida(s).')
    
    for i, v in enumerate(todos[busca - 1]["gols"]):
        print(f'Na partida {i + 1} fez {v} gol(s).')
    print(f'{todos[busca - 1]["nome"].strip()} fez gol em ', end=' ')
    print(f'{(todos[busca - 1]["cont"] / len(todos[busca - 1]["gols"])) * 100:.0f}% dos jogos em que jogou.')

print('\n', '-='*15,'FIM DO PROGRAMA','=-'*15, '\n')    