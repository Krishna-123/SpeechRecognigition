# importing the requests library
import requests
import json
import os
import speech

URL = "https://www.googleapis.com/youtube/v3/search"
def makeGet():
	querry = speech.voice_querry()
	parts = "snippet"
	keys = "AIzaSyAizRdzIlDAY3Pc_VfUe5kfqFCSZeWPL7U"

	PARAMS = {'q':querry, 'maxResults':1, 'part':parts, 'key': keys}

	r = requests.get(url = URL, params = PARAMS)

	data = r.json()

	t = json.dumps(data)
	temp = json.loads(t)
	t = temp['items']
	_id = t[0]

	t = json.dumps(_id)
	temp = json.loads(t)
	t= temp['id']  
	vid = t['videoId']
	os.system("google-chrome https://youtube.com/watch?v=%s"%vid)
