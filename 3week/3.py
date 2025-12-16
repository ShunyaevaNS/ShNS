from pyproj import Geod
from shapely.geometry import LineString, Point, Polygon
from pyproj import Transformer
from IPython.display import HTML, display
import random
import math
# задаем стартовую точку
startPoint = Point(38.20942, 55.57452)
# генерация полигона - начало
lst = []
j = 1
count_p = 10 + round(7*random.random())
center_x = startPoint.x
center_y = startPoint.y
while j < count_p:
    radius = 0.0021*(0.1+random.random())
    angle = j*2*math.pi/count_p
    lat = (center_x+radius*math.cos(angle))
    lon = (center_y+radius*math.sin(angle))
    lst.append([lat, lon])
    j = j+1
polygon = Polygon(lst)
# генерация полигона - конец
result_html='''<html>
    <body>
    <h1>Отчет за 3 неделю ознакомительной практики по разработке программного обеспечения геосервиса</h1> 
    <h2>Выполнил: Шуняева Н.С. группа 2024-ФГиИБ-ИС-4см</h2>
    <br>'''

geod = Geod(ellps="WGS84")
poly_area, poly_perimeter = geod.geometry_area_perimeter(polygon)
s = '<br>' + "Площадь полигона: " + str(round(poly_area, 2)) + " кв. метров, периметр полигона: " + str(round(poly_perimeter, 2)) + " метров. <br>"

html_pol =polygon._repr_svg_()

transformer = Transformer.from_crs(4326, 3857)

result_html = result_html + html_pol  + s + ('''<br> Пересчет из EPSG:4326 в EPSG:3857:''')

for point in transformer.itransform(polygon.exterior.coords):
  result_html = result_html + ("<br>") + str(point)

result_html = result_html + ("<br>") + ('''
    </body>
</html>''')
file_html = open("result_3.html", "w")
file_html.write(result_html)
#file_html.write(html_pol)
#file_html.write(s)
#file_html.write("<br> Пересчет из EPSG:4326 в некую МСК: ")

#file_html.write("<br>") 
file_html.close()
