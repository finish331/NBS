import json
import pandas as pd

def openFile(name):
    file_name = '../JSON/' + name + '.json'
    with open(file_name, 'r') as loadFile:
        print(file_name + '開檔成功...')
        return pd.DataFrame(json.load(loadFile))

def process(player, mvp):
    player['Share'] = 0
    for mvp_index, mvp_row in mvp.iterrows():
        for player_index, player_row in player.iterrows():
            if mvp_row['Player'] == player_row['Player']:
                player.loc[player_index, 'Share'] = mvp_row['Share']
                # print(mvp_row['Player'], player_row['Share'])
    return player

def save_to_json(name, data):
    file_name = "../JSON/" + name + ".json"
    with open(file_name, 'w') as file_object:
        data = data.to_dict()
        json.dump(data, file_object)
        print(file_name + "完成！！！")

if __name__ == '__main__':
    result = pd.DataFrame()
    for year in range(2010, 2020):
        player = openFile('AllPlayer/final/all_player' + str(year - 1))
        mvp = openFile('MVP/MVP_' + str(year))
        player['MVP_Season'] = year
        if year == 2010:
            result = process(player, mvp)
        else:
            result = result.append(process(player, mvp), ignore_index=True, sort=False)
    save_to_json('mvp_final', result)
    for index, row in result.iterrows():
        if row['Share'] != 0:
            print(row['Player'], row['MVP_Season'], row['Share'])
