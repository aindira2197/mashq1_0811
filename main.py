#1 - misol
sonlar = [1, 2, 3, 4, 5]
kvadratlar = list(map(lambda x: x ** 2, sonlar))
print("Kvadratlar:", kvadratlar)


#2 - misol
raqamlar = [-3, 0, 4, 7, -2, 5]
musbat_ikki = list(map(lambda x: x * 2, filter(lambda x: x > 0, raqamlar)))
print("Musbat sonlar 2 barobar:", musbat_ikki)


#3 - misol
satrlar = ["salom", "python", "dastur"]
katta_satrlar = list(map(lambda s: s.upper(), satrlar))
print("Katta harflar:", katta_satrlar)


#4 - misol
sonlar = [2, 3, 6, 8, 9, 12, 15]
bolinadiganlar = list(filter(lambda x: x % 3 == 0, sonlar))
print("3 ga bo‘linadiganlar:", bolinadiganlar)


#5 - misol
import math

ebob = lambda a, b: math.gcd(a, b)
print("EBOB(24, 36):", ebob(24, 36))
