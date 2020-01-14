import json

def writeFile(fileName, type, result):
    path = "./JSON/" + fileName
    with open(path, type) as file_object:
        json.dump(result, file_object)
        print(path + "寫檔成功！")

# 開檔並讀取資料
def openFile(fileName, type):
    path = './JSON/' + fileName
    with open(path, type) as loadFile:
        print(path + "開檔成功！")
        return json.load(loadFile)

def mergeAllFile():
    domain = "player_pic"
    final_list = []
    for i in range(65, 91):
        letter = chr(i)
        fileName = domain + letter + ".json"
        try:
            final_list += openFile(fileName, "r")
        except:
            print(fileName + "檔案不存在！")
            pass
    return final_list

if __name__ == '__main__':
    final_list = mergeAllFile()
    writeFile("player_pic_final.json", "w", final_list)
