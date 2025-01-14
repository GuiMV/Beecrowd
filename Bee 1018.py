''' BEE 1018 - Cédulas '''

N = int(input())
print(N)
notas = (100, 50, 20, 10, 5, 2, 1)

for i in notas:
    qua = N // i
    N %= i
    print(f"{qua} nota(s) de R$ {i},00")

# tempo: 0.000s