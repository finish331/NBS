import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('../project_key/PythonKey.json')
default_app = firebase_admin.initialize_app(cred)

if __name__ == '__main__':
    data = []
    db = firestore.client()
    teamData = db.collection('Team').get()
    for team in teamData:
        data.append(team.to_dict())
    with open('team.json','w') as file_object:
        json.dump(data,file_object)
    with open('team.json','r') as file_read:
        load_data = json.load(file_read)
    print(load_data)