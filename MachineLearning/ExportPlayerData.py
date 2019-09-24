import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('../project_key/PythonKey.json')
default_app = firebase_admin.initialize_app(cred)

if __name__ == '__main__':
    data = []
    db = firestore.client()
    teamData = db.collection('Player').get()
    for team in teamData:
        data.append(team.to_dict())
    with open('playerData.json','w') as file_object:
        json.dump(data,file_object)