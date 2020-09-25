import json
from itertools import combinations
import sys


# class GranularityRecord:
#     def __init__(self, store, logisticType, metric):
#         self.store = store
#         self.logisticType = logisticType
#         self.metric = metric


logisticTypes = ["Delivery", "Pickup", "In-Store"]
metrics = ["Orders", "Units"]
values = []

for i in range(1400):
    values.append({"dateTime": "2020-08-09 00:00", "value": "658565"})

def make_json(store, logisticType, metric):
    data = {
        "granularityRecord": {
            "store": i,
            "logisticType": j,
            "Metric": k
        },
        "values": values
    }
    return data

with open('stores.json', 'w') as outfile:
    sys.stdout = outfile
    for i in range(1, 2):
        for j in logisticTypes:
            for k in metrics:
                data = make_json(i, j, k)
                json.dump(data, outfile)
                outfile.write("\n")
