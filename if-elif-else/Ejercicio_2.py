# Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# ● 6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
# ● 4 y 5 ---> Aprobado, la nota es ...
# ● 1, 2 y 3 ---> Desaprobado, la nota es ...

import random
nota_1 = random.randint(1, 10)
nota_2 = random.randint(1, 10)
promedio = (nota_1 + nota_2) / 2
if promedio >= 6:
    print("Promoción directa, la nota es:", promedio)
elif promedio >= 4:
    print("Aprobado, la nota es:", promedio)
else:
    print("Desaprobado, la nota es:", promedio)