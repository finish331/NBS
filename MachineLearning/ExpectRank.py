import json

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
loadPlayerData = []
loadTeamData = []

def MatchData():
    for team in loadTeamData:
        teamName = team['Tm']
        for teamPlayerName in team

if __name__ == '__main__':
    with open('playerData.json', 'r') as load_a:
        loadPlayerData = json.load(load_a)
    with open('../python/JSON/team_final.json') as load_b
        loadTeamData = json.load(load_b)
    MatchData()
    
        


