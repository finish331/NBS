import json

class ProcessTeamFile:
    def __init__(self):
        self.statsFile = None
        self.picFile = None

    def openFile(self, fileName, type):
        path = './JSON/' + fileName
        with open(path, type) as loadFile:
            print(path + "開檔成功！")
            return json.load(loadFile)

    def writeFile(self, fileName, type, result):
        path = "./JSON/" + fileName
        with open(path, type) as file_object:
            json.dump(result, file_object)
            print(path + "寫檔成功！")

    def Merge(self, mainList, secondaryList):
        for team in mainList:
            for checkTeam in secondaryList:
                if team['name'] == checkTeam['name']:
                    team['pic_url'] = checkTeam['pic_url']
                    print(team['name'] + "加入成功！")

    def process(self, statsFile, picFile):
        self.statsFile = self.openFile(statsFile, 'r')
        self.picFile = self.openFile(picFile, 'r')
        self.Merge(self.statsFile, self.picFile)
        self.writeFile("team_final.json", 'w', self.statsFile)
        # self.test()

    def test(self):
        for item in self.statsFile:
            print(type(item))

if __name__ == '__main__':
    process = ProcessTeamFile()
    process.process("team.json", "team_pic.json")
    # print(type(process.picFile[1]))
