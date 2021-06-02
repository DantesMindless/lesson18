import sys

print(sys.path)
sys.path = ['']
sys.path.append('\random\path')
print(sys.path)
import random

print(random.randint(1, 43))
