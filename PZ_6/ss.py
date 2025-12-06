import random

A = []
for i in range(10):
    A.append(random.randint(0, 10))

print(A)

B = []
for inx in A:
    if inx % 7 == 0:
        B.append(inx)

print(B)
