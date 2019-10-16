import json
import pandas as pd

#計算球員屬性，回傳為一個List，順序會依照featureList
def ComputePlayerFeature(playerData,seasonIndex):
    playerFeature = []
    for feature in featureList:
        #當float轉型失敗時，會透過except接住，並將其值設為0，以利計算屬性時不將其納入計算
        try:
            #判斷NaN
            if playerData[feature][seasonIndex] != playerData[feature][seasonIndex]:
                playerFeature.append(0.0)
            else:
                #平均出場時間需大於12分鐘且該賽季需出場40場以上者才納入計算
                if float(playerData['MP'][seasonIndex]) > 12.0 and \
                float(playerData['G'][seasonIndex] > 40.0):
                    playerFeature.append(float(playerData[feature][seasonIndex]))
                else:
                    playerFeature.append(0.0)
        except:
            playerFeature.append(0.0)
    return playerFeature
        

#比對球員與球隊的名單是否都有對上
def MatchPlayerData(teamPlayer, season, teamName):
    playerExist = False
    sumResult = 0.0
    errorResult = 0
    tempFeature = []
    playerFeature = []  #所有球員的
    teamSeasonList = [] #球隊的，將球員資料計算過後的

    for teamPlayerName in teamPlayer:
        for player in loadPlayerData:
            notFoundName = teamPlayer[teamPlayerName] + '/' + season + '/' + teamName[0]
            if 'data' in player:
                for playerSeasonIndex in player['data']['Season']:
                    if (season == player['data']['Season'][playerSeasonIndex]) and \
                    (player['name'] == teamPlayer[teamPlayerName]):
                        #這邊寫的比較奇怪是因為重複球員還需要比Tm這個欄位且都有Tm欄位
                        #一般球員其實比到名子就可以了，因此沒有Tm欄位的也算對
                        if 'Tm' in player['data']:
                            if player['data']['Tm'][playerSeasonIndex] in teamName:
                                playerExist = True
                                tempFeature = ComputePlayerFeature(player['data'],playerSeasonIndex)
                                break
                        else:
                            playerExist = True
                            tempFeature = ComputePlayerFeature(player['data'],playerSeasonIndex)
                            break
        if playerExist:
            playerFeature.append(tempFeature.copy())
        else:
            notFoundPlayer.append(notFoundName)
        notFoundName = ''
        playerExist = False
        tempFeature.clear()
    
    #index控制目前計算哪個feature
    for index in range(len(playerFeature[0])):
        for feature in playerFeature:
            if(feature[index] == 0):
                errorResult += 1
            sumResult += feature[index]
        teamSeasonList.append(sumResult / (len(playerFeature) - errorResult))   #將該feature總和除以(球隊球員 - 資料不符合者)
        sumResult = 0.0
        errorResult = 0
    return teamSeasonList
        
    

#確認資料是否OK
def ConfirmData():
    trainingData = []
    i=0
    for team in loadTeamData:
        teamName = team['Tm']
        for season in team:
            if(season in SeasonRange):
                temp = MatchPlayerData(team[season]['rosters']['Player'], season, teamName)
                temp.append(int(team[season]['rosters']['Rank']))
                #以下新增賽季及球隊名稱，無實質作用，方便觀看數據，之後訓練時要拿掉
                temp.append(season)
                temp.append(team['name'])
                i += 1
                print(i)
                trainingData.append(temp)
    return trainingData 

#確認重複的球員是誰
def ConfirmRepeatData():
    for index,value in enumerate(loadPlayerData):
        for index2,value2 in enumerate(loadPlayerData):
            if(value['name'] == value2['name'] and index != index2):
                RepeatPlayer.append(value['name'])

def ExportCSV():
    trainingData = ConfirmData()
    print(len(trainingData))
    featureList.append('Rank')
    #以下新增賽季及球隊名稱，無實質作用，方便觀看數據，之後訓練時要拿掉
    featureList.append('Season')
    featureList.append('Name')
    df = pd.DataFrame(trainingData, columns = featureList)
    print (df)
    df.to_csv('training_data.csv')


def main():
    #匯出CSV用
    ExportCSV()

if __name__ == '__main__':
    notFoundPlayer = []
    RepeatPlayer = []
    featureList = [
        'Age',
        'PTS',
        'FG%',
        '3P%',
        '3PA',
        'FT%',
        'ORB',
        'DRB',
        'AST',
        'STL',
        'BLK',
        'TOV',
        'PF',
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
    with open('playerData.json','r') as load_a:
        loadPlayerData = json.load(load_a)
    with open('../python/JSON/team_final.json','r') as load_b:
        loadTeamData = json.load(load_b)
    main()

    
        


