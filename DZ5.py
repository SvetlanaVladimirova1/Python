#2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

list = [0,1]
for x in list:
        for y in list:
            for z in list:
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)