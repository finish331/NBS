import json
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('../project_key/PythonKey.json')
default_app = firebase_admin.initialize_app(cred)

# 2019/09/12
# 要取的球員屬性
template = [
    'Season',
    'Age',
    'Tm',
    'Pos',
    'G',
    'GS',
    'MP',
    'FG',
    'FGA',
    'FG%',
    '3P',
    '3PA',
    '2P',
    '2PA',
    '2P%',
    'eFG%',
    'FT',
    'FTA',
    'FT%',
    'ORB',
    'DRB',
    'TRB',
    'AST',
    'STL',
    'BLK',
    'TOV',
    'PF',
    'PTS',
]

# 要取的賽季範圍
SeasonRange = [
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

outputJson = {}
dataJson = {}
playerCount = 0
attributesIndex = []

with open("../python/JSON/all_players.json", 'r') as load_f:
    load_dict = json.load(load_f)

# 將要取得的屬性跟json檔map在一起
def MapPlayerAttributes(nowPlayer, attributesIndex, whichData):
    attributesJson = {}
    for attributes in nowPlayer[whichData]:
        for index,value in enumerate(attributesIndex):
            attributesJson[str(index)] = nowPlayer[whichData][attributes][value]
        dataJson[attributes] = attributesJson.copy()
        attributesJson.clear()

# 新增球員
def AddData():
    global attributesIndex
    global playerCount
    # nowPlayer代表目前在json檔中的第幾位球員
    # nowSeasonIndex代表賽季的index，nowPlayer[whichData]['Season']的key
    # index代表目前填到第幾個賽季
    # json要透過copy的方式取得，如果用 a = b 會取得reference而非value
    whetherInSeasonRange = False  # 判斷球員是否屬於Range內的球員
    whichData = 'data'  # 判斷是否是菜鳥 菜鳥:college_data 一般球員:data
    for nowPlayer in load_dict:
        outputJson = nowPlayer.copy()
        if 'data' in nowPlayer.keys():
            whichData = 'data'
        elif 'college_data' in nowPlayer.keys():
            whichData = 'college_data'
        del outputJson[whichData]
        if(nowPlayer[whichData] != None):
            for nowSeasonIndex in nowPlayer[whichData]['Season']:
                # 利用賽季的index(nowSeasonIndex)將賽季資料讀出來，判斷是否在要取的range內
                nowSeasonValue = nowPlayer[whichData]['Season'][nowSeasonIndex]
                if(nowSeasonValue in SeasonRange):
                    attributesIndex.append(nowSeasonIndex)
                    whetherInSeasonRange = True
                if(whetherInSeasonRange and nowSeasonValue == 'Career'):
                    attributesIndex.append(nowSeasonIndex)
        if whetherInSeasonRange:
            MapPlayerAttributes(nowPlayer, attributesIndex, whichData)
            outputJson[whichData] = dataJson.copy()
            print(outputJson)
            doc_ref = db.collection('Player').document(outputJson['name'] + '-' + str(random.randint(10000,99999)))
            doc_ref.set(outputJson)
            playerCount = playerCount + 1
        outputJson.clear()
        whetherInSeasonRange = False
        attributesIndex.clear()


if __name__ == '__main__':
    db = firestore.client()
    AddData()
    print(playerCount)
    # 測試案例
    # doc_ref = db.collection('NBA').document('2011-12').collection('Player').document('Curry')
    # data = {
    #   'name': 'test',
    #   'age': '23',
    #   'team': 'GSW'
    # }
    # doc_ref.set(data)
    # docs = doc_ref.get()
    # print('{}'.format(docs.to_dict()['name']))
