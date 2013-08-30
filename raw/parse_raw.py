import json
from pprint import pprint

filename1 = 'github-users-stats.json'

json_data = open(filename1)

data = json.load(json_data)

for d in data:
    try:
        x = d["language"]
    except KeyError:
        x = ''
    print str(d["login"]) + ' ' + str(x)


#print data[0]
json_data.close()