from bs4 import BeautifulSoup as BS
import pandas
import requests
import json
from lxml import html

def GoToEachYear(domain, url, list):
    res = requests.get(url).text
    res = BS(res, 'lxml')
    table = res.select('table')[0]
    table = table.select('tbody')[0]
    ths = table.select('th')
    year = 0
    years = []
    for th in ths:
        year += 1
        list.append(domain + th.select('a')[0].get('href'))
        if year == 10:
            break
    return list

def GetTeamList():
    domain = "https://www.basketball-reference.com"
    res = requests.get("https://www.basketball-reference.com/teams/").text
    res = BS(res, 'lxml')
    table = res.select('table')[0]
    links = table.select('a')
    result = []
    team_names = []
    for link in links:
        # result.append(domain + link.get('href'))
        result = GoToEachYear(domain, domain + link.get('href'), result)
        team_names.append(link.text)
    return result, team_names

def main(url):
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

if __name__ == '__main__':
    result = {}
    links, team_names = GetTeamList()
    count = 0
    year = 2020
    for link in links:
        if count %10 == 0:
            team = team_names.pop(0)
            result[team] = {}
            # print(team)
        if count %10 == 1 and count > 10:
            year = 2020
        # print(year)
        # print(link)
        result[team][str(year)] = main(link)
        year -= 1
        count += 1
    with open("test.json", 'w') as file_object:
        json.dump(result, file_object)
