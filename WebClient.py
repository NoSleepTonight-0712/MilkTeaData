import httpx
import json

def search(keywords : str, page : int, city : str = '0755', apiKey : str = 'd5e2f62ac6dda355e0cb175733bee509'):
    apiString = 'https://restapi.amap.com/v3/place/text'
    params = {
        'key': apiKey,
        'keywords': keywords,
        'city': city,
        'citylimit': True
    }
    response = httpx.get(apiString, params=params)
    content = response.content
    jsonObject = json.loads(content)
    pois = jsonObject.get('pois')
    result = []

    for i in pois:
        locString : str = i.get('location')
        loc = locString.split(',')
        result.append((float(loc[0]), float(loc[1])))

    return result
