import math

a = float(input("Angle in degrees: "))
r = math.radians(a)
print(f"sin: {math.sin(r):.4f}, cos: {math.cos(r):.4f}, tan: {'undefined' if math.isclose(math.cos(r), 0, abs_tol=1e-9) else f'{math.tan(r):.4f}'}")
