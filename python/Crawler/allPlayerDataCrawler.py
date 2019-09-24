from bs4 import BeautifulSoup as BS
import pandas
import requests
import json
import re
from os import listdir
from os.path import isfile, isdir, join
import time


class PlayerDataCrawler:
    def __init__(self):
        self.data = {}
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    def GetAllYearList(self):
        domain = 'https://www.basketball-reference.com'
        res = requests.get('https://www.basketball-reference.com/leagues/', headers=self.headers).text
        res = BS(res, 'lxml')
        list = res.select('#stats th.left a')
        for year in list:
            if self.SplitYear(year.get('href')) == '2020':
                pass
            else:
                url = year.get('href').replace('.html', '_advanced.html')
                self.GetPlayerData(domain + url)
                file_name = 'all_player' + self.SplitYear(year.get('href'))
                self.save_to_json(file_name, self.result)

    def GetPlayerData(self, url):
        while(True):
            try:
                table = pandas.read_html(url)[0]
                break
            except:
                print(url + ' ERROR')
                time.sleep(2)
        self.result = table.to_dict()

    # 擷取出字串中的年度
    def SplitYear(self, url):
        year = ''
        for i in re.findall('[0-9]', url):
            year += i
        return year

    def ProcessData(self, data):
        data.drop_duplicates('Rk', inplace=True)
        data.dropna(how='all', axis='columns', inplace=True)
        self.data = data[data.Rk != 'Rk']
        self.data = self.data.to_dict()

    # 最後寫入檔案
    def save_to_json(self, name, data):
        file_name = "../JSON/AllPlayer/" + name + ".json"
        with open(file_name, 'w') as file_object:
            json.dump(data, file_object)
            print(name + " 完成！！！")

    # 開啟檔案
    def openFile(self, name):
        fileName = name
        with open(fileName, 'r') as loadFile:
            self.data = json.load(loadFile)
            self.data = pandas.DataFrame.from_dict(self.data)
            self.ProcessData(self.data)

    def openFolder(self):
        path = '../JSON/AllPlayer'
        files = listdir(path)
        for file in files:
            fullPath = join(path, file)
            self.openFile(fullPath)
            file_name = file.replace('.json', '')
            self.save_to_json(file_name, self.data)


if __name__ == '__main__':
    crawler = PlayerDataCrawler()
    crawler.GetAllYearList()
    crawler.openFolder()
