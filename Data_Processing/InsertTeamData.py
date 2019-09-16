import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('../project_key/PythonKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

with open("team_final.json", 'r') as load_f:
  load_dict = json.load(load_f)

for data in load_dict :
  db.collection('Team').document(data['name']).set(data)