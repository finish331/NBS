import json

class MergePlayer:
    def __init__(self):
        self.reference = self.openFile("team_final.json", "r")
        self.picture = self.openFile("player_pic_final.json", "r")

    # 寫檔
    def writeFile(self, fileName, type, result):
        path = "./JSON/" + fileName
        with open(path, type) as file_object:
            json.dump(result, file_object)
            print(path + "寫檔成功！")

    # 開檔並讀取資料
    def openFile(self, fileName, type):
        path = './JSON/' + fileName
        with open(path, type) as loadFile:
            print(path + "開檔成功！")
            return json.load(loadFile)

    def checkPlayer(self):
        

    def process(self):
        for player in reference:



if __name__ == '__main__':
    mergePlayer = MergePlayer()
