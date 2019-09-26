import json
# '../python/JSON/team_final.json','r'
with open("../python/JSON/team_final.json", "r") as load_d:
    loadData = json.load(load_d)

seasonRange = [
    '2009-10',
    '2010-11',
    '2011-12',
    '2012-13',
    '2013-14',
    '2014-15',
    '2015-16',
    '2016-17',
    '2017-18',
    '2018-19',
    '2019-20'
]

tempDataJson = {}
copyData = loadData.copy()

for data in loadData:
    for key in data:
        if key in seasonRange:
            tempDataJson[key] = data[key]
    for season in seasonRange:
        data.pop(season,None)
    data['data'] = tempDataJson
    tempDataJson.clear()

with open('../python/JSON/team_final.json','w') as load_b:
    json.dump(loadData, load_b)