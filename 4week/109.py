file_html = open("result_4.html", "w", encoding='utf-8')
page = ('''<html>
<body>
<h1>Отчет за 4 неделю ознакомительной практики по разработке программного обеспечения геосервиса</h1> 
<h2>Выполнил: Шуняева Н.С. группа 2024-ФГиИБ-ИС-4см</h2>''')


with open('map_4.html', 'r', encoding='utf-8') as f2:
    data2 = f2.readlines()
for str2 in data2:
    page = page + str2
page = page + ('''
</body>
</html>''')

file_html.write(page)
file_html.close()