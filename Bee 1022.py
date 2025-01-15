''' BEE 1022 - TDA Racional '''

import math, sys
s = []
for _ in range(int(input())):
    n1, _, d1, op, n2, _, d2 = input().split()
    n1, d1, n2, d2 = int(n1), int(d1), int(n2), int(d2)
  
    if op == "+":
        num = n1 * d2 + n2 * d1
        den = d1 * d2
    elif op == "-":
        num = n1 * d2 - n2 * d1
        den = d1 * d2
    elif op == "*":
        num = n1 * n2
        den = d1 * d2
    else:
        num = n1 * d2
        den = d1 * n2
     
    mdc = math.gcd(num, den) 
    s.append(f"{num}/{den} = {num // mdc}/{den // mdc}")
    
sys.stdout.write("\n".join(s) + "\n")

# tempo: 0.032s