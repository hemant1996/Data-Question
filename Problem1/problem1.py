import json
import csv
def getLabelByCode(data, code, type):
    for x in data:
        if(x["variable"] == type):
            for i in x["options"]:
                if(i["code"] == code):
                    return i["label"]

with open('assesment_survey.json') as json_file:  
    data = json.load(json_file)
    p = list(data)
with open('Store_customer_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    csv = list(csv_reader)
pointer = []
map_2 = [[0 for i in range(5)] for j in range(3)]
map_3 = [[0 for i in range(5)] for j in range(3)]
pointer_3 = []
for x in data:
    if(x["variable"] == "v10"):
        for i in x["options"]:
            i["count"] = 0
        pointer = x["options"]
count = 0

for i in csv:
    if(count > 0):
        map_2[int(i[2]) - 1][int(i[11]) - 1] = map_2[int(i[2]) - 1][int(i[11]) - 1] + 1
        for j in i[10]:
            if(j!= "|"):
                map_3[int(i[2]) - 1][int(j) - 1] = map_3[int(i[2]) - 1][int(j) - 1] + 1

        for t in pointer:
            if(i[9] == str(t["code"])):
                t["count"] = t["count"]+1
    count = count + 1

for i in range(0, len(map_2)):
    for j in range(0, len(map_2[i])):
        i_label = getLabelByCode(data,i + 1,"v3")
        j_label = getLabelByCode(data,j + 1,"v12")
        print(i_label, j_label + " Star Experience")
        val = (float(map_2[i][j])/500000)*100
        print(str(val) + "%")
print("\n")
print("\n")

for i in range(0, len(map_3)):
    for j in range(0, len(map_3[i])):
        i_label = getLabelByCode(data,i + 1,"v3")
        j_label = getLabelByCode(data,j + 1,"v11")
        print(i_label, j_label)
        val = (float(map_3[i][j])/500000)*100
        print(str(val) + "%")
print("\n")
print("\n")
for x in pointer:
    val = (float(x["count"])/500000)*100
    print(str(val) + "% " + x["label"])