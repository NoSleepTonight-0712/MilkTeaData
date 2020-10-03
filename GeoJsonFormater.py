import geopandas as gpd
from shapely import geometry
import matplotlib.pyplot as plt

gdf = gpd.GeoDataFrame([114.142, 22.63])
gdf.to_file('test.shp')
