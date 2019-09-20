from bs4 import BeautifulSoup as BS
import pandas
import requests
import json
from lxml import html

class NewTeamCrawler:
    def __init__(self):
        self.result = []
        self.data = {}

    # 取得球隊名單及當年數據
    def GetData(self, url):
        dict = {
            "rosters": {},
            "stats": {}
        }
        # 取得球員名單
        dict["rosters"] = pandas.read_html(url)[0].to_dict()
        # 取得球隊數據
        html = requests.get(url).text
        soup = BS(html, 'html.parser')
        placeholders = soup.find_all('div', {'class': 'placeholder'})
        table = None
        for title in placeholders:
            # get elements after placeholder and join in one string
            comment = ''.join(title.next_siblings)
            # parse comment
            soup_comment = BS(comment, 'html.parser')
            if soup_comment.find(id='team_and_opponent') != None:
                table = soup_comment.find(id='team_and_opponent')
                data = pandas.read_html(str(table))[0]
                dict["stats"] = data.to_dict()
                break
        if table == None:
            dict["stats"] = None
        return dict

    # 進入各球隊、各年，並加入List
    def process(self, index_start, index_final):
        i = 0
        for key, value in self.data.items():
            if i >= int(index_start):
                print("取得" + key + "資料中...")
                dict = {}
                dict["name"] = key
                for inner_key, inner_value in value.items():
                    dict[inner_key] = self.GetData(inner_value)
                self.result.append(dict)
                print(key + " Done！")
            elif i > int(index_final):
                break
            i += 1      
    # 取得各球隊各球季連結
    def GetEachYears(self, domain, url):
        temp = {}
        res = requests.get(url).text
        res = BS(res, 'lxml')
        links = res.select("tbody tr th a") #取得各球季連結
        i = 0
        for link in links:
            temp[link.text] = domain + link.get('href')
            i += 1
            if i == 11: # 共取11季
                break
        return temp

    # 取得各球隊連結
    def GetTeamList(self):
        domain = "https://www.basketball-reference.com"
        res = requests.get("https://www.basketball-reference.com/teams/").text
        res = BS(res, 'lxml')
        table = res.select('table')[0]
        links = table.select('a')
        for link in links:
            self.data[link.text] = self.GetEachYears(domain, domain + link.get('href'))
            print(link.text + "取得各年連結！")

    def openFile(self):
        fileName = './JSON/team_link.json'
        with open(fileName, 'r') as loadFile:
            self.data = json.load(loadFile)

    # 最後寫入檔案
    def save_to_json(self, name, data):
        file_name = "./JSON/" + name + ".json"
        with open(file_name, 'w') as file_object:
            json.dump(data, file_object)
            print(file_name + "完成！！！")

if __name__ == '__main__':
    crawler = NewTeamCrawler()
    index_start = input("請輸入想從第幾支球隊開始爬取，0~29：")
    index_final = input("請輸入想爬取到第幾支球隊，0~29：")
    file_name = input("請輸入輸出檔案名稱：")
    #crawler.GetTeamList()
    #crawler.save_to_json("team_link", crawler.data)
    crawler.openFile()
    crawler.process(index_start, index_final)
    crawler.save_to_json(file_name, crawler.result)
