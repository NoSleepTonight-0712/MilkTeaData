from WebClient import *
from GeoInfoFormatter import GeoInfo
import geopandas as gpd

searchList = ['喜茶', '益禾堂', '蜜雪冰城']

for keyword in searchList:
    webClient = WebClient(keyword, '0755')
    webClient.searchAll()
    locationList = webClient.getResult()
    geoInfo : GeoInfo = GeoInfo()
    geoInfo.addLocationList(locationList)
    gdf = geoInfo.getGeoDataFrame()
    gdf.to_file('data/{}.shp'.format(keyword))