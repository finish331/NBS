import json

class MergeTeamSummary:
    def __init__(self):
        self.summary = self.openFile('team_summary')
        self.team = self.openFile('team_final')
        self.none_summary = {
            "Record": None,
            "Rank": None,
            "Coach": None,
            "Executive": None
        }

    def openFile(self, name):
        fileName = '../JSON/' + name + '.json'
        with open(fileName, 'r') as loadFile:
            print('開啟' + fileName + '...')
            return json.load(loadFile)

    def process(self):
        for team in self.team:
            for key, value in self.summary.items():
                if team['name'] == key:
                    for inner_key, inner_value in value.items():
                        try:
                            team[inner_key]['summary'] = inner_value
                        except:
                            print(team['name'] + ' ' + inner_key + ' error')
                            pass
                    team['2019-20']['summary'] = self.none_summary
        self.save_to_json('new_team_final', self.team)

    # 最後寫入檔案
    def save_to_json(self, name, data):
        file_name = "../JSON/" + name + ".json"
        with open(file_name, 'w') as file_object:
            json.dump(data, file_object)
            print(file_name + "完成！！！")

if __name__ == '__main__':
    merger = MergeTeamSummary()
    merger.process()
