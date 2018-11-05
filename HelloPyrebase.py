import pyrebase

config = {
    "apiKey": "AIzaSyAgWzJypcKysr7Negw6mhNbcv3pZOKmfSA",
    "authDomain": "imageai-2018.firebaseapp.com",
    "databaseURL": "https://imageai-2018.firebaseio.com",
    "projectId": "imageai-2018",
    "storageBucket": "imageai-2018.appspot.com",
    "messagingSenderId": "862027968333"
}

firebase = pyrebase.initialize_app(config);


auth = firebase.auth();

users = auth.sign_in_with_email_and_password('lucas_unifor@hotmail.com', 'Naruto123')



 db = firebase.database()

data = {
    "Nome": "Daniel Valente"

 }

results = db.child("users").push(data, users['idToken'])
 print results
'''

data = {"NOME ": "Lucas Alves"}


db.child("users").push(data, users['idToken'])


db.child("users").set(data, users['idToken'])
'''
