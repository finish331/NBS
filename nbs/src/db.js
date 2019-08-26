import firebase from 'firebase/app'
import 'firebase/firestore'

// Initialize your firebase app
firebase.initializeApp({
  projectId: 'nbs-eff63',
  databaseURL: 'https://nbs-eff63.firebaseio.com'
})
firebase.firestore().settings({ timestampsInSnapshots: true })

export const db = firebase.firestore()