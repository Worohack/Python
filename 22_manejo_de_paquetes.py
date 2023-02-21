import os
import sys

print(os.path.dirname(sys.executable))

from paquete import operaciones_aritmeticas
print(operaciones_aritmeticas.sum(8,10))