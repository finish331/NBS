from bs4 import BeautifulSoup as BS
import requests
import json

class TeamStandingCrawler:
    def __init__(self):
        self.result = {}
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    def GetTeamRank(self, url):
        res = requests.get(url, headers = self.headers)
        res = BS(res.text, 'lxml')
        list = res.select('table .hide-mobile a')
        temp = []
        for team in list:
            temp.append(team.text)
        return temp

    def GoEachYear(self):
        url = 'https://www.espn.com/nba/standings/_/season/{0}/group/league'
        for year in range(2010, 2020):
            self.result[str(year)] = self.GetTeamRank(url.format(str(year)))
            
    # 最後寫入檔案
    def save_to_json(self, name, data):
        file_name = "../JSON/" + name + ".json"
        with open(file_name, 'w') as file_object:
            json.dump(data, file_object)
            print(name + " 完成！！！")

if __name__ == '__main__':
    crawler = TeamStandingCrawler()
    crawler.GoEachYear()
    crawler.save_to_json('TeamStanding', crawler.result)
