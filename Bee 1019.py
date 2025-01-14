''' BEE 1019 - Conversão de Tempo '''

N = int(input())
h, m, s = N // 3600, N % 3600 //60, N % 3600 % 60
print(f"{h}:{m}:{s}")

# tempo: 0.000s