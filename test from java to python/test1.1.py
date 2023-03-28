import re
with open("2.1.txt", 'w') as f2:
    f2.write('')


with open("1.1.txt", 'r', encoding='utf8') as f:
    all=f.readlines()
    for row in all:
        row=row.replace(') ','):\n')
        row = row.replace('{', '\t')
        row = row.replace('}; ', '\n')
        row = row.replace('};', '')
        row = row.replace('} ; ', '\n')
        row = row.replace('var ', '')
        res = re.findall(r'user_naber_\d+', row)
        if res:
            print(res)
            print(res[0])
            for results in res:
                row = row.replace(results, f'data["{results}"]')
        row = row.replace('true', "'a'")
        with open("2.1.txt", 'a+', encoding='utf8') as f2:
            f2.write(row+'\n')

