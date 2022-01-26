# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 21:56:32 2022

@author: User
"""

import firebase_admin
from firebase_admin import db

cred_object = firebase_admin.credentials.Certificate('serve.json')
default_app = firebase_admin.initialize_app(cred_object, {'databaseURL':'https://class-25d2c-default-rtdb.firebaseio.com/'})

ref = db.reference("/")

data = {
	rollno:
	{
        'roll' : rollno,
		"Sunday": [0,0,0,0,0,0,0,0,0,0],
		"Monday": [0,0,0,0,0,0,0,0,0,0],
		"Tuesday": [0,0,0,0,0,0,0,0,0,0],
		"Wednesday": [0,0,0,0,0,0,0,0,0,0],
        "Thursday":[0,0,0,0,0,0,0,0,0,0],
        "Friday":[0,0,0,0,0,0,0,0,0,0],
        "Saturday":[0,0,0,0,0,0,0,0,0,0],
	} for rollno in credentials
}
    
ref = db.reference("/")
ref.set({
	"Class":
	{
		"Students": -1
	}
})

ref = db.reference("/Class/Students")

#pUSING THE DATA TO THE DATABASE
for key, value in data.items():
	ref.push().set(value)
    
#For accesing the data
best=ref.get()

