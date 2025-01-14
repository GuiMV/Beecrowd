''' BEE 1021 - Notas e Moedas '''

N = int(float(input()) * 100)
notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    quantidade = int(N / nota)
    print("{} nota(s) de R$ {:.2f}".format(quantidade, nota/100))
    N -= quantidade * nota

print("MOEDAS:")
for moeda in moedas:
    quantidade = int(N / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(quantidade, moeda/100))
    N -= quantidade * moeda

# tempo: 0.000s