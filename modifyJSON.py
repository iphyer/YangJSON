"""
Read in forcase.json and add a new field to the values

Created: 2020-09-24

"""

# Import packages
import json
import random

with open('forecast.json') as infile:
    data = json.load(infile)

dataTime_set =set()
for dic in data["values"]:
    if dic['dateTime'] not in dataTime_set:
        dataTime_set.add(dic['dateTime'])
    else:
        print("Conflicting: {}".format(dic))
    dic["override"] = random.randint(100000, 200000)

# convert into JSON:
with open("new_forcast.json", "w") as outfile:
    json.dump(data, outfile)