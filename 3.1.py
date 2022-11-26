import re
import csv
with open(input(), encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    b = ''
    count = 0
    i = 0
    m = 1
    p = list('')
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
                b=(f'{"=#".join(row)}')
                numbers = b.replace("\n", ", ")
                numbers = numbers.replace("<p>", "")
                numbers = numbers.replace("False=#", "Нет=#")
                numbers = numbers.replace("True=#", "Да=#")
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
                u = len(words)
                g = len(numbers)
                if g<u:
                    x = 0
                else:
                    trans = {
                        'name': 'Название',
                        'description': 'Описание',
                        'key_skills': 'Навыки',
                        'experience_id': 'Опыт работы',
                        'premium': 'Премиум-вакансия',
                        'employer_name': 'Компания',
                        'salary_from': 'Нижняя граница вилки оклада',
                        'salary_to': 'Верхняя граница вилки оклада',
                        'salary_gross': 'Оклад указан до вычета налогов',
                        'salary_currency': 'Идентификатор валюты оклада',
                        'area_name': 'Название региона',
                        'published_at': 'Дата и время публикации вакансии'
                    }
                    for i in range(0, len(words), 1):
                        myDict = {words[i]: numbers[i]}
                        if myDict[words[i]] != '':
                            x = len(words) - 1
                            x = x - i
                            t = words[i]
                            t2 = trans[t] + ':'
                            if x != 0:
                                print(t2, myDict[words[i]])
                            if x == 0:
                                print(t2, myDict[words[i]], '\n')
                g = p
                p = p + [numbers]
            else:
                d = 0
        count += 1
#print(p)