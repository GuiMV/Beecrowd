''' BEE 1023 -  '''

# import sys
# i, s = 1, []
# 
# while (N := int(input())) != 0:
#     l = [0] * 201
#     sx = sy = 0
#     
#     for _ in range(N):
#         x, y = map(int, input().split())
#         a, sx, sy = y // x, sx + x, sy + y
#         l[a] = l[a] + x
#         
#     cons = int(sy / sx * 100) / 100
#     sv = [f"{l[i]}-{i}" for i in range(201) if l[i] > 0]
#     s.append(f"Cidade# {i}:\n" + " ".join(sv) + f"\nConsumo medio: {cons:.2f} m3.")
#     i += 1
#     
# sys.stdout.write("\n\n".join(s) + "\n")
# 
# 
# import sys
# i, s = 1, []
# 
# while (N := int(input())) != 0:
#     count = [0] * 201
#     sum_x = sum_y = 0
#     
#     for _ in range(N):
#         x, y = map(int, input().split())
#         atual = y // x
#         count[atual] += x
#         
#         sum_x += x
#         sum_y += y
#         
#     consumo_m = int(sum_y / sum_x * 100) / 100
# 
#     sorted_val = [f"{count[i]}-{i}" for i in range(201) if count[i] > 0]
#     saida.append(f"Cidade# {i}:\n" + " ".join(sorted_val) + f"\nConsumo medio: {consumo_m:.2f} m3.")
#     i += 1
#     
# sys.stdout.write("\n\n".join(saida) + "\n")

# tempo: 2.811s / 0.970s

import timeit, time

t1o = time.time()
for _ in range (1000000):
    sx = sy = 0
t1i = time.time()

t2o = time.time()
for _ in range (1000000):
    sum_x = sum_y = 0
t2i = time.time()

t1 = timeit.timeit("sx = sy = 0", number=1_000_000)
t2 = timeit.timeit("sum_x = sum_y = 0", number=1_000_000)
# separate_time2 = timeit.timeit("l = [0] * 201; sum_x = 0; sum_y = 0", number=10_000)

print(f"cod1: {t1i - t1o}")
print(f"cod2: {t2i - t2o}")

print(f"rep1: {t1}")
print(f"rep2: {t2}")