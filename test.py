
f = open("temp.out", "w")

print("This is a test file, which I can call from github actions", file=f)

from math import pi, exp
print(f"PI = {pi:5f}, e^pi = {exp(pi):10f}", file = f)

import os

print(os.listdir("."), file=f)

f.close()