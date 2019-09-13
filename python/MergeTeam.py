import json

class ProcessTeamFile:
    def __init__(self):
        self.statsFile = None
        self.picFile = None

    def openFile(self, fileName, type):
        path = './JSON/' + fileName
        with open(path, type) as loadFile:
            return loadFile

if __name == '__main__':
    process = ProcessTeamFile()
    process.statsFile = process.openFile('team.json', 'r')
    process.picFile = process.openFile('team_pic.json', 'r')
    print(process.picFile)
