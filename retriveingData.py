from firebase import firebase

firebase = firebase.FirebaseApplication("https://flaskfirebase-9bb90.firebaseio.com/",None)

result = firebase.get('/Customer','')
print(result)