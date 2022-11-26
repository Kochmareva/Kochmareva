for i in range(1):
    s = input('Введите название вакансии: ')
    try:
        n = str(s)
    except ValueError as e:
        break
    a = input('Введите описание вакансии: ')
    try:
        n = str(a)
    except ValueError as e:
        break
    b = input('Введите требуемый опыт работы (лет): ')
    try:
        n = int(b)
    except ValueError as e:
        break
    c = input('Введите нижнюю границу оклада вакансии: ')
    try:
        n = int(c)
    except ValueError as e:
        break
    d = input('Введите верхнюю границу оклада вакансии: ')
    try:
        n = int(d)
    except ValueError as e:
        break
    e = input('Есть ли свободный график (да / нет): ')
    try:
        n = bool(e)
    except ValueError as e:
        break
    finally:
        if e == 'да':
            e = True
        if e == 'нет':
            e = False
    f = input('Является ли данная вакансия премиум-вакансией (да / нет): ')
    try:
        n = bool(f)
    except ValueError as e:
        break
    finally:
        if f == 'да':
            f = True
        if f == 'нет':
            f = False

print(f"{s} (str)")
print(f"{a} (str)")
print(f"{b} (int)")
print(f"{c} (int)")
print(f"{d} (int)")
print(f"{e} (bool)")
print(f"{f} (bool)")