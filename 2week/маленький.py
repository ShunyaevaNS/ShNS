import shapely
from shapely import wkt 
from shapely import Point
from shapely import Polygon
from shapely import LineString
file_wkt = open('geom.wkt', 'r')
geom_objects = wkt.loads(file_wkt.read())
file_wkt.close()
file_html = open("input_and_SA.html", "w", encoding='utf-8')
page = '''<html>
<body>
<p>Исходные данные (в формате wkt):'''
page = page + str(geom_objects.wkt) + '</p><br/>'
page = page + '<ul>'
for geom in geom_objects.geoms:
    number_geom = list(geom_objects.geoms).index(geom)
    str_type = ""
    if type(geom) == Polygon:
        str_type = "Полигон "
    if type(geom) == LineString:
        str_type = "Ломаная "
    if type(geom) == Point:
        str_type = "Точка "
    for another_geom in geom_objects.geoms:
        number_geom_2 = list(geom_objects.geoms).index(another_geom)
        str_type2 = ""
        if type(another_geom) == Polygon:
            str_type2 = "Полигон "
        if type(another_geom) == LineString:
            str_type2 = "Ломаная "
        if type(another_geom) == Point:
            str_type2 = "Точка "
        if (number_geom < number_geom_2):
            if (type(geom)!= Point and type(another_geom) != Point and shapely.intersects(geom, another_geom)):
                p1 = (str_type+str(number_geom)+" пересекается с "+str_type2+str(number_geom_2))
                page = page + '<li>'+p1+'</li>'
                print(p1)
            if (type(geom) == Point and type(another_geom) == Polygon and shapely.contains(another_geom, geom)):
                p2 = (str_type+str(number_geom)+" входит в "+str_type2+str(number_geom_2))
                page = page + '<li>'+p2+'</li>'
                print(p2)
page = page + '</ul>'
page = page + ('''
</body>
</html>''')
file_html.write(page)
file_html.close()