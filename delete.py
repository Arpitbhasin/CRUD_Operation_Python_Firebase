from firebase import firebase

firebase = firebase.FirebaseApplication("https://flaskfirebase-9bb90.firebaseio.com/",None)

firebase.delete('/Customer/','-M6Ou3BEAkI9K2k6N-PB')
print('record deleted')