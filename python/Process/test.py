import json
import pandas

class Test:
  def __init__(self):
    
  def openFile(self, name):
        fileName = '../JSON/' + name
        with open(fileName, 'r') as loadFile:
            return json.load(loadFile)