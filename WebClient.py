import httpx
import json
import math

class WebClient:
    def __init__(self, keywords : str, city : str, apiKey : str = 'd5e2f62ac6dda355e0cb175733bee509'):
        self.jsonObject = None
        self.keywords = keywords
        self.city = city
        self.apiKey = apiKey
        self.result = []

    def search(self, page : int):
        apiString = 'https://restapi.amap.com/v3/place/text'
        params = {
            'key': self.apiKey,
            'keywords': self.keywords,
            'city': self.city,
            'page': page,
            'citylimit': True
        }
        response = httpx.get(apiString, params=params)
        content = response.content
        self.jsonObject = json.loads(content)

        self.itemCount = int(self.jsonObject.get('count'))

    def getLocation(self):
        pois = self.jsonObject.get('pois')
        result = []

        for i in pois:
            locString: str = i.get('location')
            loc = locString.split(',')
            result.append((float(loc[0]), float(loc[1])))
        return result

    def getItemCount(self):
        return self.itemCount


    def getPageCount(self):
        return math.ceil(self.getItemCount() / 20)


    def searchAll(self):
        # test search
        # get Page count
        self.search(1)
        pageCount = self.getPageCount()
        if self.itemCount <= 20:
            return
        self.result.extend(self.getLocation())
        for i in range(2, pageCount + 1):
            self.search(i)
            self.result.extend(self.getLocation())

    def getResult(self):
        return self.result

    @staticmethod
    def searchDebug(a=0, b=0, c=0, d=0, e=0):
        return [(114.107037, 22.558484), (114.072968, 22.617073), (114.011515, 22.545112), (114.11065, 22.542725), (114.123645, 22.675758), (114.242648, 22.713584), (114.02597, 22.530291), (113.871593, 22.568943), (114.139953, 22.548152), (113.9455, 22.581089), (113.951588, 22.541838), (114.05956, 22.634291), (114.04122, 22.699387), (114.057074, 22.523434), (113.94203, 22.519337), (113.953102, 22.537357), (114.109257, 22.540983), (114.065913, 22.536533), (114.119183, 22.54275), (113.972873, 22.555677)]