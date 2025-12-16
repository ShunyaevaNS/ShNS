from shapely import wkt
from shapely import Point
from shapely import Polygon
from shapely import LineString
import folium
import numpy as np
m1 = folium.Map(location=[55.57452, 38.20942], control_scale=True,
                tiles='Cartodb Positron',
                zoom_start=12)

file_wkt = open('geom.wkt', 'r')
geom_objects = wkt.loads(file_wkt.read())
for geom in geom_objects.geoms:
    number_geom = list(geom_objects.geoms).index(geom)
    if type(geom) == Polygon:
        folium.Polygon(
            locations=np.array(geom.exterior.coords),
            color="blue",
            weight=2,
            fill_color="white",
            fill_opacity=0.5,
            fill=True,
            popup="Полигон "+str(number_geom),
            tooltip=str(number_geom),
        ).add_to(m1)
    if type(geom) == LineString:
        folium.PolyLine(
            locations=np.array(geom.coords),
            color="gray",
            weight=2,
            popup="Ломаная "+str(number_geom),
            tooltip=str(number_geom),
        ).add_to(m1)
    if type(geom) == Point:
        folium.Marker(
            location=np.array(geom.coords),
            popup="Точка "+str(number_geom),
            tooltip=str(number_geom),
        ).add_to(m1) 
m1.save("map.html")
m1