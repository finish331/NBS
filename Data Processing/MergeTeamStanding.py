import json

with open('../python/JSON/team_standing.json','r') as load_a:
    loadStanding = json.load(load_a)
with open('../python/JSON/team_final.json','r') as load_b:
    loadTeam = json.load(load_b)

def MatchTeam(seasonRank, season, teamName):
    for team in loadTeam:
        if(team['name'] == teamName):
            team[season]['rosters']['Rank'] = seasonRank

for season in loadStanding:
    for index,value in enumerate(loadStanding[season]):
        MatchTeam(index+1, season, value)

with open('../python/JSON/team_final.json','w') as file_object:
    json.dump(loadTeam,file_object)
    
    