"""
Generate JSON file with fixed format 

Format description: https://gist.github.com/njuyangyang/835338c83e88c49e71939aee33d40505

Created: 2020-09-19

"""
# Import packages
import json
import datetime
import random

# Variables that can be set
store_ID = "Store123"
logisticType_Category = "Delivery"
Metric_Setter = "Units"
file_NUMBER = 2

values_LENGTH = 10
start_date = "2020-08-09 00:00"
end_date = "2020-09-09 00:00"
baseline_Value = "658565"
# generate random date and time
def randomtimes(start_date, end_date, n):
    frmt = "%Y-%m-%d %H:%M"
    stime = datetime.datetime.strptime(start_date, frmt)
    etime = datetime.datetime.strptime(end_date, frmt)
    td = etime - stime
    # "dateTime" should be unique to act as primary key
    resultSet = set()
    while len(resultSet) < n:
        tmp = random.random() * td + stime
        resultSet.add(tmp.strftime(frmt).replace("\'","\"",2))
    return resultSet

def genearte_seq_times(start_date, n):
    frmt = "%Y-%m-%d %H:%M"
    stime = datetime.datetime.strptime(start_date, frmt)
    # can set differnt step time
    step = datetime.timedelta(days=1, hours= 2)
    # "dateTime" should be unique to act as primary key
    resultSet = []
    for _ in range(n):
        resultSet.append(stime.strftime(frmt).replace("\'","\"",2))
        stime += step
    return resultSet

for i in range(file_NUMBER):
    output_content_list = {}
    # granularityRecord geneations
    output_content_list["granularityRecord"] = {}
    output_content_list["granularityRecord"]["store"] = store_ID 
    output_content_list["granularityRecord"]["logisticType"] = logisticType_Category
    output_content_list["granularityRecord"]["Metric"] = Metric_Setter
    # Values generation
    dt_values_list = []
    dt_set = genearte_seq_times(start_date, values_LENGTH)
    for dt_item in dt_set:
        dt_dict = {}
        dt_dict["dateTime"] = dt_item
        dt_dict["baseline"] = random.randint(100000, 999999)
        dt_values_list.append(dt_dict)
    output_content_list["values"] = dt_values_list 
    # convert into JSON:
    with open("json_example" + str(i) + ".json", "w") as outfile:
        json.dump(output_content_list, outfile)