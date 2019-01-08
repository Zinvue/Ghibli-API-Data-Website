import urllib.request
import json
import bottle

def rotten(url):
    arr = []
    a = urllib.request.urlopen(url)
    edit = a.read().decode()
    data = json.loads(edit)
    for i in data:
        if 'rt_score' in i.keys():
            arr.append([i['title'], i['rt_score']])
    arr.sort(key = lambda arr: int(arr[1]), reverse = True)
    return json.dumps(arr)
