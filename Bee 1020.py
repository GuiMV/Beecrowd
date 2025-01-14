''' BEE 1020 - Idade em Dias '''

i = int(input())
a, m, d = i // 365, i % 365 // 30, i % 365 % 30
print(f"{a} ano(s)\n{m} mes(es)\n{d} dia(s)")

# tempo: 0.000s