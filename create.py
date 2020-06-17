from firebase import firebase

firebase = firebase.FirebaseApplication("https://flaskfirebase-9bb90.firebaseio.com/",None)
data={
	'Name': 'Harvey Specter',
	'Email': 'harveyspecter@gmail.com',
	'Mobile': '7262099457'
}
result = firebase.post('/Customer',data)
print(result)