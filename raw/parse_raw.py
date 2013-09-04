from __future__ import print_function
import json
from pprint import pprint

filename1 = 'github-users-stats.json'
log = open("top-users-final.csv", "w")
json_data = open(filename1)

data = json.load(json_data)

for d in data:
    
    i = -1
    h = -1
    try:
        x = d["language"]

        x1 = x.split(' in ')
        x2 = x1[1].split('.')
        x3 = x2[0]
        x3 = x3.replace(' and ', ' ')
        x4 = x3.split(' ')

        z = ['', '', '']

        z[0] = str(x4[0])
        z[1] = str(x4[1])
        z[2] = str(x4[2])

    except KeyError:
        #print 'KeyError'
        z = ''
    except IndexError:
        #print 'IndexError'
        lambda:None
        #donothing actually
    finally:
        for y in z:
            i = i + 1
            if (y.find(',') > -1):
                y = y.replace(',', '')
                #print 'replaced..'
            z[i] = y.strip()
    
    for y in z:
        h = h + 1
        if (len(y) < 1):
            del z[h]
    
    print(str('\'' + d["login"]) + '\', ' + str(z).replace('[','').replace(']',''), file=log)

#print data[0]
json_data.close()