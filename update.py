from firebase import firebase

firebase = firebase.FirebaseApplication("https://flaskfirebase-9bb90.firebaseio.com/",None)

firebase.put('/Customer/-M6OyH4yeI1YR57IRwM5','Email','MikeRoss@email.com')
print('record updated')