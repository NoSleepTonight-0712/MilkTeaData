import geopandas as gpd
from shapely.geometry import Point

class GeoInfo:
    def __init__(self):
        self.names = []
        self.geometrys = []
        self.data = {
            'name': self.names,
            'geometry': self.geometrys
        }

    def getGeoDataFrame(self):
        return gpd.GeoDataFrame(self.data, crs='EPSG:4236')

    def addName(self, name : str):
        self.names.append(name)

    def addGeometry(self, loc : tuple):
        self.geometrys.append(Point(loc))

    def addGeoData(self, name : str, loc : tuple):
        self.addName(name)
        self.addGeometry(loc)

    def addGeoDataList(self, geodataList : list):
        for i in geodataList:
            self.addName(i[0])
            self.addGeometry(i[1])

    def addLocationList(self, locationList : list):
        for index, location in enumerate(locationList):
            self.addName('location_'+str(index))
            self.addGeometry(location)
