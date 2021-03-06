import json

class ProcessTeamFile:
    # 初始化List
    def __init__(self):
        self.statsFile = None
        self.picFile = None

    # 開檔並讀取資料
    def openFile(self, fileName, type):
        path = './JSON/' + fileName
        with open(path, type) as loadFile:
            print(path + "開檔成功！")
            return json.load(loadFile)

    # 寫檔
    def writeFile(self, fileName, type, result):
        path = "./JSON/" + fileName
        with open(path, type) as file_object:
            json.dump(result, file_object)
            print(path + "寫檔成功！")

    # 負責合併兩個List
    def Merge(self, mainList, secondaryList):
        count = 0
        for team in mainList:
            for checkTeam in secondaryList:
                if team['name'] == checkTeam['name']:   # 當球隊名稱相同
                    team['pic_url'] = checkTeam['pic_url']
                    print(team['name'] + "加入成功！")
                    count += 1
        print("總共合併" + str(count) + "支球隊")

    def process(self, statsFile, picFile):
        self.statsFile = self.openFile(statsFile, 'r')
        self.picFile = self.openFile(picFile, 'r')
        self.Merge(self.statsFile, self.picFile)
        self.writeFile("team_final.json", 'w', self.statsFile)

    def test(self): #測試用
        for item in self.statsFile:
            print(type(item))

if __name__ == '__main__':
    process = ProcessTeamFile()
    process.process("team1.json", "team_pic.json")
