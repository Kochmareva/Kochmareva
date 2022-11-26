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
                print(['name', row[1]])
            else:
                a=(f'{" ".join(row)}')
                words = a.split()
                print(words)
        else:
            o = 100
            q = len(row)
            if row[q-1] == '':
                m = 0
                i = 1
            if row[q-1] == 'Инженер':
                m = 2
            for t in range(q-1):
                if row[t] == '':
                    o = o-1;
            if o == 100:
                b=(f'{"=#".join(row)}')
                numbers = b.split('=#')
                g = p
                p = p + [numbers]
            else:
                d = 0
        count += 1
if m == 0:
   print([numbers])
elif m == 2 and i == 0:
   print(g)
elif m == 2 and i == 1:
   print([])
else:
   print(p)