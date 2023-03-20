
import math
from decimal import Decimal

# NaN - Not a numbre ( no es un numero )
# No es sensible a Mayusculas / Minusculas, 
a = float("NaN")
print(f" a : {a}")
print(f" Es NaN (not a numbre) ? : {math.isnan(a)}")

b = Decimal("NaN")
print(f" b : {b}")
print(f" Es NaN (not a numbre) ? : {math.isnan(b)}")




