import json
import pandas


class TeamProcessor:
    def __init__(self):
        self.player = {}
        self.mvp = {}
        self.result = pandas.DataFrame()
        self.columns = ['G' ,'GS' ,'MP' ,'FG' ,'FGA' ,'FG%' ,'3P' ,'3PA' ,'3P%' ,'2P' ,'2PA' ,'2P%' ,'eFG%' ,'FT' ,'FTA' ,'FT%' ,'ORB' ,'DRB' ,'TRB' ,'AST' ,'STL' ,'BLK' ,'TOV' ,'PF' ,'PTS' ,'Share']

    def openFile(self, name):
        fileName = '../JSON/' + name + '.json'
        with open(fileName, 'r') as loadFile:
            print('開啟' + fileName + '...')
            return json.load(loadFile)

    def ProcessFile(self):
        for year in range(2010, 2020):
            # 使用前一年的球員資料，以及下一年的MVP
            file_name = 'NewPlayer/player_' + str(year - 1)
            # 讀取所有球員資料並轉成Dataframe
            self.player = self.openFile('AllPlayer/all_player' + str(year - 1))
            self.player = pandas.DataFrame(self.player)
            # 讀取MVP資料並轉成Dataframe
            self.mvp = self.openFile('MVP/MVP_' + str(year))
            self.mvp = pandas.DataFrame(self.mvp)
            self.process()
            self.save_to_json(file_name, self.player.to_dict())

    # 最後寫入檔案
    def save_to_json(self, name, data):
        file_name = "../JSON/" + name + ".json"
        with open(file_name, 'w') as file_object:
            json.dump(data, file_object)
            print(file_name + "完成！！！")

    def process(self):
        for player_index, player_row in self.player.iterrows():
            for mvp_index, mvp_row in self.mvp.iterrows():
                if player_row['Player'] == mvp_row['Player']:
                    self.player.at[player_index, 'Share'] = mvp_row['Share']
                    break
                else:
                    self.player.at[player_index, 'Share'] = 0
        # 如有缺則補0
        self.player.loc[:, 'G': 'Share'].fillna(value=0, inplace=True)
        # 更改型態
        for column in self.columns:
            self.player[column] = self.player[column].astype('float64')
        for column in ['Rk', 'Age']:
            self.player[column] = self.player[column].astype('int64')
        # print(self.player.info())


if __name__ == '__main__':
    processor = TeamProcessor()
    processor.ProcessFile()
    # temp = pandas.DataFrame(processor.openFile('NewPlayer/player_2018'))
    # print(temp.tail(50))
