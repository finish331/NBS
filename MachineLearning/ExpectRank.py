import json

feature = [
    'Age',
    'PTS',
    'FG%',
    '3P',
    '3PA',
    'FT%',
    'ORB',
    'DRB',
    'AST',
    'STL',
    'BLK',
    'TOV',
    'PF'
]

SeasonRange = [
    '2009-10',
    '2010-11',
    '2011-12',
    '2012-13',
    '2013-14',
    '2014-15',
    '2015-16',
    '2016-17',
    '2017-18',
    '2018-19'
]

#比對球員與球隊的名單是否都有對上
def MatchPlayerData(teamPlayer, season, teamName):
    playerExist = False
    for teamPlayerName in teamPlayer:      
        for player in loadPlayerData:
            temp = teamPlayer[teamPlayerName] + '/' + season + '/' + teamName[0]
            if 'data' in player:
                for playerSeasonIndex in player['data']['Season']:
                    if (season == player['data']['Season'][playerSeasonIndex]) and \
                    (player['name'] == teamPlayer[teamPlayerName]):
                        if 'Tm' in player['data']:
                            if player['data']['Tm'][playerSeasonIndex] in teamName:
                                playerExist = True
                                continue
                        else:
                            playerExist = True
        if not playerExist:
            notFoundPlayer.append(temp)
        temp = ''
        playerExist = False

#確認資料是否OK
def ConfirmData():
    for team in loadTeamData:
        teamName = team['Tm']
        for season in team:
            if(season in SeasonRange):
                MatchPlayerData(team[season]['rosters']['Player'], season, teamName)

#確認重複的球員是誰
def ConfirmRepeatData():
    for index,value in enumerate(loadPlayerData):
        for index2,value2 in enumerate(loadPlayerData):
            if(value['name'] == value2['name'] and index != index2):
                RepeatPlayer.append(value['name'])

if __name__ == '__main__':
    notFoundPlayer = []
    RepeatPlayer = []
    test = []
    with open('playerData.json','r') as load_a:
        loadPlayerData = json.load(load_a)
    with open('../python/JSON/team_final.json','r') as load_b:
        loadTeamData = json.load(load_b)
    ConfirmData()
    print(notFoundPlayer)
    print(len(notFoundPlayer))
    print(test)
    
        


