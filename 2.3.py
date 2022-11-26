import re
import csv

def clear_str(str_value):
    return ' '.join(re.sub(r"<[^>]+>", '', str_value).split())

with open(input(), encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    b = []
    count = 0
    i = 0
    m = 1
    p = list('')
    n = {}
    baze = []
    rep2 = {}
    for row in file_reader:
        w = len(row)
        if count == 0:
            if row[0] == '\ufeffname':
                words = (['name', row[1]])
            else:
                a=(f'{" ".join(row)}')
                words = a.split()
                #print(words)
        else:
            o = 100
            q = len(row)
            if row[q-1] == '':
                m = 0
                i = 1
                o = o - 1
            if row[q-1] == 'Инженер':
                m = 2
            for t in range(q-1):
                if row[t] == '':
                    o = o-1;
            if o == 100:
                b = (f'{"=#".join(row)}')
                numbers = b.replace("\n", "%$")
                numbers = numbers.replace("<p>", "")
                numbers = numbers.replace("<strong>", "")
                numbers = numbers.replace("</strong>", "")
                numbers = numbers.replace("</p>", "")
                numbers = numbers.replace("<br />", "")
                numbers = numbers.replace("</em>", "")
                numbers = numbers.replace("<em>", "")
                numbers = numbers.replace("<li>", "")
                numbers = numbers.replace("</li>", "")
                numbers = numbers.replace("<ul>", "")
                numbers = numbers.replace("</ul>", "")
                numbers = numbers.replace("</div>", "")
                numbers = numbers.replace("<div>", "")
                numbers = re.sub(r'\s+', ' ', numbers)
                numbers = numbers.replace(" =#", "=#")
                numbers = numbers.replace("=# ", "=#")
                numbers = numbers.split('=#')
                for i in range(0, len(numbers)):
                    if numbers[i].find("%$") != -1:
                        numbers1 = [clear_str(el) for el in numbers[i].split('%$')]
                    else:
                        numbers1 = clear_str(row[i])
                    rep2[words[i]] = numbers1
                    n = {**n, **rep2}
                baze.append(n)
        count += 1

def salary_avg(dic):
    return int((dic['salary_from'] + dic['salary_to']) / 2)

def pluralize(count, p_1, p_2, p_3):
    if count % 100 < 11 or count % 100 > 14:
        if count % 10 == 1:
            return p_1
        if 1 < count % 10 < 5:
            return p_2
    return p_3

RUR = [x for x in baze if x['salary_currency'] == 'RUR']
for vac in RUR:
    vac['salary_from'] = int(float(vac['salary_from']))
    vac['salary_to'] = int(float(vac['salary_to']))


TO = sorted(RUR, key=lambda x: salary_avg(x), reverse=True)
print(f"Самые высокие зарплаты:")
for i in range(min([len(TO), 10])):
    st = TO[i]
    print(f"    {i + 1}) {st['name']} в компании \"{st['employer_name']}\" - {salary_avg(st)} {pluralize(salary_avg(st), 'рубль', 'рубля', 'рублей')} (г. {st['area_name']})")

FROM = sorted(RUR, key=lambda x: salary_avg(x))
print()
print(f"Самые низкие зарплаты:")
for i in range(min([len(FROM), 10])):
    st = FROM[i]
    print(f"    {i + 1}) {st['name']} в компании \"{st['employer_name']}\" - {salary_avg(st)} {pluralize(salary_avg(st), 'рубль', 'рубля', 'рублей')} (г. {st['area_name']})")

SKILLS = {}
for st in RUR:
    if type(st['key_skills']).__name__ == 'list':
        for i in st['key_skills']:
            if i in SKILLS:
                SKILLS[i] += 1
            else:
                SKILLS[i] = 1
    else:
        if st['key_skills'] in SKILLS:
            SKILLS[st['key_skills']] += 1
        else:
            SKILLS[st['key_skills']] = 1


SKILLSL = sorted(SKILLS.items(), key=lambda item: item[1], reverse=True)
print()
print(f"Из {len(SKILLSL)} {pluralize(len(SKILLSL), 'скилла', 'скиллов', 'скиллов')}, самыми популярными являются:")
for i in range(min([len(SKILLSL), 10])):
    st = SKILLSL[i]
    print(f"    {i + 1}) {st[0]} - упоминается {st[1]} {pluralize(st[1], 'раз', 'раза', 'раз')}")

AREA = {}
for st in RUR:
    if st['area_name'] in AREA: AREA[st['area_name']].append(salary_avg(st))
    else: AREA[st['area_name']] = [salary_avg(st)]

AREAL = AREA.items()
AREAL = [x for x in AREAL if len(x[1]) >= int(len(RUR) / 100)]
AREAL = sorted(AREAL, key=lambda item: sum(item[1]) / len(item[1]), reverse=True)

print()
print(f"Из {len(AREA)} {pluralize(len(AREA), 'города', 'городов', 'городов')}, самые высокие средние ЗП:")
for i in range(min([len(AREAL), 10])):
    st = AREAL[i]
    print(f"    {i + 1}) {st[0]} - средняя зарплата {int(sum(st[1]) / len(st[1]))} {pluralize(int(sum(st[1]) / len(st[1])), 'рубль', 'рубля', 'рублей')} ({len(st[1])} {pluralize(len(st[1]), 'вакансия', 'вакансии', 'вакансий')})")