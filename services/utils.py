import numpy as np
import face_recognition
from pymongo import MongoClient

from configs import Config
from exceptions import FacesException

client = MongoClient(Config.MONGODB_HOST, Config.MONGO_PORT)
db = client[Config.MONGO_DBNAME]
faces_collection = db[Config.MONGO_COLLECTION]

def add_single_person(
        image: str, 
        name: str, 
        age: int, 
        gender: str, 
        info: str = None) -> bool:
    try:
        face = face_recognition.load_image_file(image)
        face_encodings = face_recognition.face_encodings(face)[0]
        data = {
                "name": name,
                "face_encoding": face_encodings.tolist(),
                "age": age,
                "gender": gender,
                "info": info
        }
        faces_collection.insert_one(data)
        return True
    except FacesException:
        return False

def find_person(face: str) -> list:
    result = None
    person = face_recognition.load_image_file(face)
    person_encoding = face_recognition.face_encodings(person)[0]
    for person in faces_collection.find():
        answer = face_recognition.compare_faces(
            [np.asarray(person["face_encoding"])],
            person_encoding,
            tolerance=0.44
        )
        if answer[0]:
            result = {
                "name": person['name'],
                "age": person['age'],
                "gender": person['gender'],
                "info": person['info']
            }
    
    return result
