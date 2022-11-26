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
    w = n
    d = input('Введите верхнюю границу оклада вакансии: ')
    try:
        n = int(d)
    except ValueError as e:
        break
    q = n
    o = w + n
    try:
        n = int(o)
    except ValueError as e:
        break
    j = o // 2
    e = input('Есть ли свободный график (да / нет): ')
    try:
        n = bool(e)
    except ValueError as e:
        break
    f = input('Является ли данная вакансия премиум-вакансией (да / нет): ')
    try:
        n = bool(f)
    except ValueError as e:
        break

print(f"{s}")
print(f"Описание: {a}")
if b[-1] in '1':
    print(f"Требуемый опыт работы: {b} год")
elif b[-1] in '234':
    print(f"Требуемый опыт работы: {b} года")
else:
    print(f"Требуемый опыт работы: {b} лет")
if j == 1:
    print('Средний оклад:', j, 'рубль')
elif j == 2 or j == 3 or j == 4:
    print('Средний оклад:', j, 'рубля')
else:
    print('Средний оклад:', j, 'рублей')
print(f"Свободный график: {e}")
print(f"Премиум-вакансия: {f}")