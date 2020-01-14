import json
from unidecode import unidecode

class MergeRookiePic:
    def __init__(self):
        self.player = self.openFile("reference")
        self.picture = self.openFile("player_pic_final")
        self.repeat = []
        self.noPicutre = []
        self.result = []
        self.season = [
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

    # 開檔並讀取資料
    def openFile(self, fileName):
        fileName = '../JSON/' + fileName + '.json'
        with open(fileName, 'r') as loadFile:
            return json.load(loadFile)

    # 最後寫入檔案
    def save_to_json(self, name, data):
        file_name = "../JSON/" + name + ".json"
        with open(file_name, 'w') as file_object:
            json.dump(data, file_object)
            print(file_name + "完成！！！")

    def checkInRangeSeason(self, player):
        for playerSeason in range(len(player['data']['Season'])):
            if(player['data']['Season'][str(playerSeason)] in self.season):
                return 1
        return 0

    def process(self):
        for player in self.player:
            if self.checkInRangeSeason(player) == 1:
                check = 0
                temp = {
                    'name': None,
                    'pic_url': []
                }
                for pic in self.picture:
                    if unidecode(player["name"]) == unidecode(pic["name"]):
                        temp["name"] = player["name"]
                        temp["pic_url"].append(pic["pic_url"])
                        # print(rookie["name"] + "有照片！！！")
                        check += 1
                if check == 0:
                    player["pic_url"] = "https://stats.nba.com/media/img/league/nba-headshot-fallback.png"
                    self.noPicutre.append(player["name"])
                elif check == 1:
                    player["pic_url"] = temp["pic_url"][0]
                elif check > 1:
                    self.repeat.append(temp)
                    player["pic_url"] = None
                self.result.append(player)

        self.save_to_json("player_final", self.result)
        self.save_to_json("repeat", self.repeat)
        self.save_to_json("NoPicutre", self.noPicutre)

if __name__ == '__main__':
    merge = MergeRookiePic()
    merge.process()
    print("沒有照片總共有：" + str(len(merge.noPicutre)))
    print("重複地總共有：" + str(len(merge.repeat)))
