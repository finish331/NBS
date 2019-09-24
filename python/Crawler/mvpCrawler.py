from bs4 import BeautifulSoup as BS
import pandas
import requests
import json
import re

class MVPCrawler:
    def __init__(self):
        self.data = {}
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        self.columns = ['Rank',	'Player', 'Age', 'Tm', 'First', 'Pts Won', 'Pts Max', 'Share', 'G', 'MP',	'PTS', 'TRB', 'AST', 'STL', 'BLK', 'FG%', '3P%', 'FT%', 'WS', 'WS/48']

    def GetAllMVPYears(self):
        domain = 'https://www.basketball-reference.com/awards/awards_'
        res = requests.get('https://www.basketball-reference.com/awards/mvp.html').text
        res = BS(res, 'lxml')
        list = res.select('#mvp_NBA th.left a')
        for link in list:
            year = self.SplitYear(link.get('href'))
            self.GetMVPList(domain + year + '.html')
            file_name = 'MVP_' + year
            self.save_to_json(file_name, self.data)

    # 擷取出字串中的年度
    def SplitYear(self, url):
        year = ''
        for i in re.findall('[0-9]', url):
            year += i
        return year

    # 取得當年度MVP候選列表
    def GetMVPList(self, url):
        list = pandas.read_html(url)[0]
        list.columns = self.columns
        self.data = list.to_dict()

    # 最後寫入檔案
    def save_to_json(self, name, data):
        file_name = "../JSON/MVP/" + name + ".json"
        with open(file_name, 'w') as file_object:
            json.dump(data, file_object)
            print(name + " 完成！！！")

    # 開啟檔案
    def openFile(self):
        fileName = '../JSON/MVP/test.json'
        with open(fileName, 'r') as loadFile:
            self.data = json.load(loadFile)
            print(pandas.DataFrame.from_dict(self.data))

if __name__ == '__main__':
    crawler = MVPCrawler()
    crawler.GetAllMVPYears()
    # crawler.GetMVPList('https://www.basketball-reference.com/awards/awards_2019.html')
    # crawler.save_to_json('test', crawler.data)
    # crawler.openFile()
