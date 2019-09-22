from bs4 import BeautifulSoup as BS
import pandas
import requests
import json
import re
from lxml import html

class DraftCralwer:
    def __init__(self):
        self.result = []
        self.teamLinks = []
        self.rookies = []
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    # 取得各球隊連結
    def GetTeamList(self):
        domain = "https://www.basketball-reference.com"
        res = requests.get("https://www.basketball-reference.com/teams/").text
        res = BS(res, 'lxml')
        table = res.select('table')[0]
        links = table.select('a')
        for link in links:
            temp = domain + link.get('href')
            self.GetEachYears(domain, temp)
        print("有" + str(len(self.teamLinks)) + "支球隊")

    # 取得各球隊各球季連結
    def GetEachYears(self, domain, url):
        temp = {}
        res = requests.get(url, headers = self.headers).text
        res = BS(res, 'lxml')
        links = res.select("tbody tr th a") #取得各球季連結
        for link in links:
            temp = domain + link.get('href')
            break
        self.teamLinks.append(temp)
        print(temp)

    def GetRookies(self, url):
        domain = "https://www.basketball-reference.com"
        res = requests.get(url, headers = self.headers).text
        res = BS(res, 'lxml')
        tr = res.select('tbody tr')
        for item in tr:
            # print(item.select('a')[0].get('href') + " " + item.select('td')[6].text)
            temp = {}
            if item.select('td')[6].text == "R":
                temp["name"] = item.select('a')[0].text
                temp["link"] = domain + item.select('a')[0].get('href')
                self.rookies.append(temp)

    # 取得球員資料
    def GetData(self, url):
        res = requests.get(url, headers = self.headers).text
        res = BS(res, 'html.parser')
        team = None
        name = res.select('h1')[0].text  # 球員名字
        meta = res.select('#meta')[0]  # 球員基本資料區
        meta = meta.select('p')  # 球員基本資料
        # 球員歷年數據表格
        placeholders = res.find_all('div', {'class': 'placeholder'})
        table = None
        for title in placeholders:
            # get elements after placeholder and join in one string
            comment = ''.join(title.next_siblings)
            # parse comment
            soup_comment = BS(comment, 'html.parser')
            if soup_comment.find(id='all_college_stats') != None:
                table = soup_comment.find(id='all_college_stats')
                table = pandas.read_html(str(table))[0]
                # 重設columns
                table.columns = ['Season', 'Age', 'College', 'G', 'MP', 'FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'TRB', 'AST', 'STL',	'BLK', 'TOV', 'PF',	'PTS', 'FG%', '3P%', 'FT%',	'MP', 'PTS', 'TRB',	'AST']
                table = table.loc[:, 'Season':'FT%']    # 刪掉不要的資料欄
                table = table.to_dict()
                break

        for strongStr in meta:
            if len(strongStr.select('strong')) != 0:
                if re.findall("Position", strongStr.select('strong')[0].text):
                    position = strongStr.text   #抓球員位置
                if re.findall("Team", strongStr.select('strong')[0].text):
                    team = strongStr.select('a')[0].text    #抓球員所屬球隊

        #取得球員位置
        str_temp = re.split('\n', position)
        for i in range(len(str_temp)):
            if str_temp[i] == '  Position:':
                break
        position = str_temp[i+2][2:]

        player = {}
        player["name"] = name
        player["number"] = None
        player["team"] = team
        player["position"] = position
        player["college_data"] = table
        self.result.append(player)

    def process(self):
        self.GetTeamList()
        print("取得所有球隊列表！")
        for link in self.teamLinks:
            self.GetRookies(link)
        print("取得所有菜鳥連結！")
        for rookie in self.rookies:
            self.GetData(rookie["link"])
            print(rookie["name"] + " Get！")
        # self.GetData("https://www.basketball-reference.com/players/w/willizi01.html")
        self.save_to_json("rookie", self.result)
        print("總共" + str(len(self.result)) + "個新秀")

    # 最後寫入檔案
    def save_to_json(self, name, data):
        file_name = "./JSON/" + name + ".json"
        with open(file_name, 'w') as file_object:
            json.dump(data, file_object)
            print(file_name + "完成！！！")

if __name__ == '__main__':
    crawler = DraftCralwer()
    crawler.process()
