file_html = open("result_2.html", "w")
page = ('''<html>
<body>
<h1>Отчет за 2 неделю ознакомительной практики по разработке программного обеспечения геосервиса</h1> 
<h2>Выполнил: Шуняева Н.С. группа 2024-ФГиИБ-ИС-4см</h2>''')
with open('input_and_SA.html', 'r', encoding='utf-8') as f1:
    data1 = f1.readlines()
for str1 in data1:
    page = page + str1
with open('map.html', 'r', encoding='utf-8') as f2:
    data2 = f2.readlines()
for str2 in data2:
    page = page + str2
page = page + ('''
</body>
</html>''')
file_html.write(page)
file_html.close()