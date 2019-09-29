from bs4 import BeautifulSoup as BS
import requests
import json
import re

class TeamSummaryCrawler:
    def __init__(self):
        self.link = self.openFile('Backup/team/team_link')
        self.result = {}
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    def openFile(self, name):
        fileName = '../JSON/' + name + '.json'
        with open(fileName, 'r') as loadFile:
            print('開啟' + fileName + '...')
            return json.load(loadFile)

    def GoToEachTeam(self):
        for key, value in self.link.items():
            print(key + '...')
            team = {}
            for inner_key, inner_value in value.items():
                if inner_key == '2019-20':
                    pass
                else:
                    team[inner_key] = self.GetData(inner_value)
                print(inner_key + 'Done！')
            self.result[key] = team
        self.save_to_json('team_summary', self.result)

    def GetData(self, url):
        temp = {}
        res = requests.get(url, headers = self.headers).text
        res = BS(res, 'lxml')
        meta = res.select('#meta')[0]  # 球隊基本資料區
        meta = meta.select('p')  # 球隊基本資料
        temp['Record'], temp['Rank'] = self.GetInformation(meta, 'Record:')
        temp['Coach'] = self.GetInformation(meta, 'Coach:')
        temp['Executive'] = self.GetInformation(meta, 'Executive:')
        return temp

    def GetInformation(self, meta, key):
        for strongStr in meta:
            if len(strongStr.select('strong')) != 0:
                if key == 'Coach:' or key == 'Executive:':
                    if re.findall(key, strongStr.select('strong')[0].text):
                        return strongStr.select('a')[0].text
                else:
                    if re.findall(key, strongStr.select('strong')[0].text):
                        temp_str = re.split('\n', strongStr.text)
                        for i in range(len(temp_str)):
                            if temp_str[i] == 'Record:':
                                break
                        temp = temp_str[i+2]
                        temp = re.split(',', temp)
                        Record = temp[0].strip()
                        Rank = temp[1].strip() + ' ' + temp_str[i+3].strip()
                        return Record, Rank
        return None

    # 最後寫入檔案
    def save_to_json(self, name, data):
        file_name = "../JSON/" + name + ".json"
        with open(file_name, 'w') as file_object:
            json.dump(data, file_object)
            print(file_name + "完成！！！")

if __name__ == '__main__':
    crawler = TeamSummaryCrawler()
    crawler.GoToEachTeam()
