import firebase_admin

databaseURL = 'https://fit-diplomka-default-rtdb.europe-west1.firebasedatabase.app/'
cred_obj = firebase_admin.credentials.Certificate('diplomka-firebase.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})


ref = firebase_admin.db.reference("/")