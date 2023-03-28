with open("2.txt", 'w') as f2:
    f2.write('')


with open("1.txt", 'r', encoding='utf8') as f:
    all=f.readlines()
    for row in all:
        row=row.replace('confirm(','')
        row=row.strip()[4:-7]
        row = row.replace('а)', '\\nа)')
        row = row.replace('б)', '\\nб)')
        print(row)
        with open("2.txt", 'a+', encoding='utf8') as f2:
            f2.write(row+'\n')