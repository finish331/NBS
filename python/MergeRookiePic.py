import json

class MergeRookiePic:
    def __init__(self):
        self.rookie = self.openFile("rookie")
        self.picture = self.openFile("player_pic_final")

    # 開檔並讀取資料
    def openFile(self, fileName):
        fileName = './JSON/' + fileName + '.json'
        with open(fileName, 'r') as loadFile:
            return json.load(loadFile)

    # 最後寫入檔案
    def save_to_json(self, name, data):
        file_name = "./JSON/" + name + ".json"
        with open(file_name, 'w') as file_object:
            json.dump(data, file_object)
            print(file_name + "完成！！！")

    def process(self):
        for rookie in self.rookie:
            check = 0
            for pic in self.picture:
                if rookie["name"] == pic["name"]:
                    rookie["pic_url"] = pic["pic_url"]
                    print(rookie["name"] + "有照片！！！")
                    check = 1
                    break
            if check == 0:
                rookie["pic_url"] = "https://stats.nba.com/media/img/league/nba-headshot-fallback.png"
                print(rookie["name"] + "沒照片QQ")
        self.save_to_json("rookie_final", self.rookie)

if __name__ == '__main__':
    merge = MergeRookiePic()
    merge.process()
