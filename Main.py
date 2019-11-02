import random
import time

import pyrebase

def get_results():
    return random.randint(0, 11)

# Configuration key for realtime database with all permission (read + write) to true
config = {
    "apiKey": "AIzaSyA6wZISMpsD6dkmiX1R-kdYLeDlaJcz1Ps",
    "authDomain": "electriccityhacks4.firebaseapp.com",
    "databaseURL": "https://electriccityhacks4.firebaseio.com",
    "storageBucket": "electriccityhacks4.appspot.com"
}

# Initialize the "pyrebase" and retrieve the realtime database
firebase = pyrebase.initialize_app(config)
firestore_db = firebase.database()

# This will be set to some random user account
username = ""

while True:

    # Replace get_results with prediction data from model
    ran_energy = get_results()
    data = {"energy": ran_energy}

    # Send the post request in realtime database
    firestore_db.child("users").child(username).push(data)

    print(data)

    # Stop the entire thread; used to create delays
    time.sleep(5)