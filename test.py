print("This is a test file, which I can call from github actions")

from math import pi, exp
print(f"PI = {pi:5f}, e^pi = {exp(pi):10f}")

import os

print(os.listdir("."))