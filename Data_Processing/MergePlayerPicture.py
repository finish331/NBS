import json
from unidecode import unidecode

with open("reference.json", "r") as load_f:
  load_dict = json.load(load_f)
with open("../python/JSON/player_pic_final.json", "r") as load_p:
  load_pic = json.load(load_p)

RepeatPlayer = []
feq = 0

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

for player in load_dict:
  for player_pic in load_pic:
    if unidecode(player_pic['name']) == unidecode(player['name']):
      feq += 1
      print(unidecode(player_pic['name']), unidecode(player['name']))
  if feq != 1:
    for playerSeason in range(len(player['data']['Season'])):
      if(player['data']['Season'][str(playerSeason)] in SeasonRange):
        RepeatPlayer.append(player['name'])
        break
  feq = 0

print(RepeatPlayer)
print(len(RepeatPlayer))