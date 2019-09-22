import json

def openFile(fileName):
    fileName = './JSON/' + fileName + '.json'
    with open(fileName, 'r') as loadFile:
        return json.load(loadFile)

# 最後寫入檔案
def save_to_json(name, data):
    file_name = "./JSON/" + name + ".json"
    with open(file_name, 'w') as file_object:
        json.dump(data, file_object)
        print(file_name + "完成！！！")

if __name__ == '__main__':
    old_player = openFile("player_final")
    rookie = openFile("rookie_final")
    new_list = old_player + rookie
    save_to_json("all_players", new_list)
    print("總共有" + str(len(new_list)) + "個球員")
