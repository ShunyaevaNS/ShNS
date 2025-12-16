import pandas as pd
from geopy.distance import geodesic

# Чтение данных из CSV
df = pd.read_csv('Rus_schools_final-5B691859-27B3-54AA-BA88-23D2BAC0BB64.csv', encoding = 'windows-1251')

# Точка отсчета (ваш дом)
point_0 = (55.57452, 38.20942)

result_html='''<html>
    <body>
      <h1>Отчет за 1 неделю ознакомительной практики по разработке программного обеспечения геосервиса</h1>
      <h2>Выполнил: Шуняева Н.С. группа 2024-ФГиИБ-ИС-4см</h2>'''

# здесь вставить выполнение пункта 1.3

df['distance'] = df.apply(lambda row: geodesic(point_0, (row['lat'], row['lon'])).km, axis=1)
nearest_school = df.loc[df['distance'].idxmin()]

output_string_1_3 = f"""
<h3>Ближайшая школа к дому:</h3>
Название: {nearest_school['name']}<br>
Адрес: {nearest_school['addr']}<br>
Тип: {nearest_school['struct']}<br>
Координаты: ({nearest_school['lat']}, {nearest_school['lon']})<br>
Расстояние: {nearest_school['distance']:.2f} км
"""

# записать полученное в 1.3 в конце result_html:

result_html = result_html + "<p>"+ output_string_1_3 +"</p>"

# выполнить и дописать в result_html пункты 1.4:

schools_3km = df[df['distance'] <= 3]
output_string_1_4 = "<h3>Школы в радиусе 3 км:</h3><ul>"
for idx, school in schools_3km.iterrows():
    output_string_1_4 += f"<li><strong>{school['name']}</strong> — {school['addr']}</li>"
output_string_1_4 += "</ul>"

result_html = result_html + output_string_1_4

# выполнить и дописать в result_html пункты 1.5:

gov_schools_count = df[df['struct'] == "(Государственное образовательное учреждение)"].shape[0]
output_string_1_5 = f"<p><strong>Количество государственных образовательных учреждений:</strong> {gov_schools_count}</p>"

result_html = result_html + output_string_1_5


result_html = result_html + ('''
    </body>
</html>''')
file_html = open("result.html", "w")
file_html.write(result_html)
file_html.close()
