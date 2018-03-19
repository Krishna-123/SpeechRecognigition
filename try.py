import os
import json

k = {"nextPageToken": "CAEQAA", "kind": "youtube#searchListResponse", "items": [{"snippet": {"thumbnails": {"default": {"url": "https://i.ytimg.com/vi/YQHsXMglC9A/default.jpg", "width": 120, "height": 90}, "high": {"url": "https://i.ytimg.com/vi/YQHsXMglC9A/hqdefault.jpg", "width": 480, "height": 360}, "medium": {"url": "https://i.ytimg.com/vi/YQHsXMglC9A/mqdefault.jpg", "width": 320, "height": 180}}, "title": "Adele - Hello", "channelId": "UComP_epzeKzvBX156r6pm1Q", "publishedAt": "2015-10-23T06:54:18.000Z", "liveBroadcastContent": "none", "channelTitle": "AdeleVEVO", "description": "'Hello' is taken from the new album, 25, out November 20. http://adele.com Available now from iTunes http://smarturl.it/itunes25 Available now from Amazon http://smarturl.it/25amazon Available..."}, "kind": "youtube#searchResult", "etag": "\"_gJQceDMxJ8gP-8T2HLXUoURK8c/Q0jOEUm2HG9WRLVyFCeLyj-2rsY\"", "id": {"kind": "youtube#video", "videoId": "YQHsXMglC9A"}}], "regionCode": "IN", "etag": "\"_gJQceDMxJ8gP-8T2HLXUoURK8c/lMWRyS7szWkUAmYJ5azMfZFefN8\"", "pageInfo": {"resultsPerPage": 1, "totalResults": 1000000}}

t = json.dumps(k)
temp = json.loads(t)
t = temp['items']
_id = t[0]

t = json.dumps(_id)
temp = json.loads(t)
t= temp['id']
vid = t['videoId']
print vid




# t = json.dumps(k)
# temp = json.loads(t)
# t = temp['id']
# vid = t['videoId']

# print vid
# file = open("try_json.json","w")
# file.write(json.dumps(t1))
# tem = 'YQHsXMglC9A'
# os.system("google-chrome https://youtube.com/watch?v=%s" %tem)