import json
import random
import firebase_admin 
from firebase_admin import credentials 
from firebase_admin import firestore
cred = credentials.Certificate('../project_key/PythonKey.json') 
default_app = firebase_admin.initialize_app(cred)

#2019/09/12
#要取的球員屬性
template = [
  'name', 
  'number', 
  'team', 
  'position',
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
  '2010-11',
  '2011-12',
  '2012-13',
  '2013-14',
  '2014-15',
  '2015-16',
  '2016-17',
  '2017-18',
  '2018-19'
]

outputJson = {}

with open("./python/reference.json", 'r') as load_f:
  load_dict = json.load(load_f)

# 將要取得的屬性跟json檔map在一起
def MapPlayerAttributes(player_no, player_season):
  for attributes in template:
    if attributes in load_dict[player_no] :
      outputJson[attributes] = load_dict[player_no][attributes]
    else:
      outputJson[attributes] = load_dict[player_no]['data'][attributes][str(player_season)]

#新增球員
def AddData():
  # player_no代表目前在json檔中的第幾位球員
  # player_season代表賽季的index
  for player_no in range(len(load_dict)):
    for player_season in range(len(load_dict[player_no]['data']['Season'])):
      #利用賽季的index(player_season)將賽季資料讀出來，判斷是否在要取的range內
      if(load_dict[player_no]['data']['Season'][str(player_season)] in SeasonRange):
        MapPlayerAttributes(player_no,player_season)
        if not outputJson:  
          print(outputJson)
          doc_ref = db.collection('NBA').document(outputJson['Season']).collection('Player').document(outputJson['name'] + '-' + str(random.randint(10000,99999)))
          doc_ref.set(outputJson)
        outputJson.clear()

if(__name__ == '__main__'):
  db = firestore.client()
  AddData()
  #測試案例
  # doc_ref = db.collection('NBA').document('2011-12').collection('Player').document('Curry')
  # data = {
  #   'name': 'test',
  #   'age': '23',
  #   'team': 'GSW'
  # }
  # doc_ref.set(data)
  # docs = doc_ref.get()
  # print('{}'.format(docs.to_dict()['name']))