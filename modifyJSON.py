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
del_list =list()

for dic in data["values"]:
    if dic['dateTime'] not in dataTime_set:
        dataTime_set.add(dic['dateTime'])
        dic["override"] = random.randint(100000, 200000)
    else:
        print("Conflicting: {}".format(dic))
        del_list.append(dic)

# del duplicated dateTime
for item in del_list:
    data["values"].remove(item)

# convert into JSON:
with open("new_forcast.json", "w") as outfile:
    json.dump(data, outfile)