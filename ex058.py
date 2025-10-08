print('GERADOR DE PA')
print('=-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    mais = int(input('quantos termos você quer mostrar a mais? '))
print('Fim')