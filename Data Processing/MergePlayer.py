import json
import pandas as pd

class MergePlayer:
    def __init__(self):
        self.player1 = pd.DataFrame()
        self.player2 = pd.DataFrame()
        self.mvp = pd.DataFrame()
        self.result = pd.DataFrame()
        self.MVPresult = []
        self.columns = ['G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PER', 'TS%', '3PAr', 'FTr', 'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP']

    # 最後寫入檔案
    def save_to_json(self, name, data):
        file_name = "../JSON/" + name + ".json"
        with open(file_name, 'w') as file_object:
            data = data.to_dict()
            json.dump(data, file_object)
            print(file_name + "完成！！！")

    # 開檔並讀取資料
    def openFile(self, name):
        fileName = '../JSON/' + name + '.json'
        with open(fileName, 'r') as loadFile:
            print('開啟' + fileName + '...')
            return pd.DataFrame(json.load(loadFile))

    def MergeData(self):
        self.player2 = self.player2.loc[:, 'PER':]
        self.result = pd.concat([self.player1, self.player2], axis=1, join='inner').set_index('Rk')
        self.result.fillna(value=0, inplace=True)
        for col in self.columns:
            self.result[col] = self.result[col].astype('float64')
        self.result['Age'] = self.result['Age'].astype('int64')

    def MergeMVP(self, year):
        mvp_columns = self.player1.columns
        mvp_columns = list(mvp_columns)
        mvp_columns.append('Share')
        mvp_columns.append('Season')
        # print(mvp_columns)
        for mvp_index, mvp_row in self.mvp.iterrows():
            for player_index, player_row in self.player1.iterrows():
                new_row = player_row
                if mvp_row['Player'] == player_row['Player']:
                    new_row['Share'] = mvp_row['Share']
                    new_row['Season'] = year
                    self.MVPresult.append(new_row.values)
                    break
        self.result = self.result.append(pd.DataFrame(self.MVPresult, columns=mvp_columns))
        # print(self.result)

    def process(self, type):
        if type == 'player':
            for year in range(1947, 2020):
                # 合併球員資料
                self.player1 = self.openFile('AllPlayer/per_game/all_player' + str(year))
                self.player2 = self.openFile('AllPlayer/old/all_player' + str(year))
                self.MergeData()
                self.save_to_json('AllPlayer/final/all_player' + str(year), self.result)
        else:
            for year in range(1956, 2020):
                # 合併MVP資料
                self.player1 = self.openFile('AllPlayer/final/all_player' + str(year - 1))
                self.mvp = self.openFile('MVP/MVP_' + str(year))
                self.MergeMVP(year)
                self.save_to_json('MVP/final/MVP_' + str(year), self.result)

if __name__ == '__main__':
    mergePlayer = MergePlayer()
    mergePlayer.process('mvp')
