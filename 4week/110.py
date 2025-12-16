import pandas as pd
import shapely
import ast
import folium
from folium.plugins import MarkerCluster

# Функция парсинга координат
#Преобразование координат в формат списка
def parse_coordinates(coord_str):
    try:
        return (ast.literal_eval(coord_str))[0]
    except:
        return None

df = pd.read_csv('russian_regions.csv', sep=';', encoding='cp1251')
df1 = df[df['Регион'] == "Московская область" ]

for idx, row in df1.iterrows():
    coords = parse_coordinates(row['Полигон'])
    # Создаем полигон с помощью библиотеки Shapely
    polygon = shapely.Polygon(coords)

if coords:
  # Получаем координаты центроида
  centroid = polygon.centroid.coords[0]

  # Координаты центроида
  lat_centroid, lon_centroid = centroid
  m = folium.Map(location=[lat_centroid, lon_centroid], zoom_start=8, tiles='Cartodb Positron',)
  folium.Polygon(
                locations=coords,
                tooltip=row['Регион'],
                color='blue',
                weight=0.5,
                fill = True,
            ).add_to(m)


df3 = pd.read_csv('objects_v2.csv', sep=';', low_memory=False, encoding='utf-8')
df3.head()
marker_cluster = MarkerCluster().add_to(m)
#найти все точки, которые попадают в "наш" полигон и при этом в названии содержат слово "Завод"

for cur_row in df3.iterrows():
  cur_pos = shapely.Point([float(cur_row[1]["latitude"]), float(cur_row[1]["longitude"])])
  if shapely.contains(polygon, cur_pos) and " Мира" in str(cur_row[1]["address"]):
    folium.Marker(
        location = [float(cur_row[1]["latitude"]), float(cur_row[1]["longitude"])],
        popup=cur_row[1]["address"], tooltip=cur_row[1]["name"]
    ).add_to(marker_cluster)

  if shapely.contains(polygon, cur_pos) and " Пушкина" in str(cur_row[1]["address"]):
    folium.Marker(
        location = [float(cur_row[1]["latitude"]), float(cur_row[1]["longitude"])],
        popup=cur_row[1]["address"], tooltip=cur_row[1]["name"]
    ).add_to(marker_cluster)

  if shapely.contains(polygon, cur_pos) and " Ленина" in str(cur_row[1]["address"]):
    folium.Marker(
        location = [float(cur_row[1]["latitude"]), float(cur_row[1]["longitude"])],
        popup=cur_row[1]["address"], tooltip=cur_row[1]["name"]
    ).add_to(marker_cluster)

m.save("map_4.html")