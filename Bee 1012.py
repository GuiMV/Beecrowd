''' BEE 1012 - Área '''

A, B, C = map(float, input().split())
a1, a2, a3, a4, a5 = (A * C)/2, 3.14159 * (C**2), ((A + B)*C)/2, B**2, A*B
print(f'TRIANGULO: {a1:.3f}\nCIRCULO: {a2:.3f}\nTRAPEZIO: {a3:.3f}\nQUADRADO: {a4:.3f}\nRETANGULO: {a5:.3f}')

# tempo: 0.000s