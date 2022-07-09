# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = {False, True}
y = {False, True}
z = {False, True}

for i in x:
    for j in y:
        for k in z:
            print(not (x or y or z) == (not x and not y and not z))
