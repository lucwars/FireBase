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
#cria uma referencia para o compente de storage no firebase
storage = firebase.storage();
#eniar para o storage da imagem escolhida
results = storage.child("Foto2.jpg").put("C:/Users/lucwa/Desktop/LAPIN(FIREBASE WEBCAM)/FotosCam/2018/10/16/15_45_2.jpg", users['idToken'])
