import json
import pandas

class Test:
    def __init__(self):
        self.result = pandas.DataFrame()

    # 開檔並讀取資料
    def openFile(self, name):
        fileName = '../JSON/' + name + '.json'
        with open(fileName, 'r') as loadFile:
            print('開啟' + fileName + '...')
            return pandas.DataFrame(json.load(loadFile))

    # 最後寫入檔案
    def save_to_json(self, name, data):
        file_name = "../JSON/" + name + ".json"
        with open(file_name, 'w') as file_object:
            data = data.to_dict()
            json.dump(data, file_object)
            print(file_name + "完成！！！")

    def Process(self):
        for year in range(2010, 2020):
            file_name = 'MVP/final/MVP_' + str(year)
            temp = self.openFile(file_name)
            self.result = pandas.concat([self.result, temp])
        # print(self.result)
        self.save_to_json('MVP/final_mvp', self.result)

if __name__ == '__main__':
    test = Test()
    test.Process()
