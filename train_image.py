import os
import time
import cv2
import numpy as np
from PIL import Image
from threading import Thread

def getImagesAndLabels(path):
    # Path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []
    
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')  # Convert to grayscale
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])  # Extract ID from filename
        faces.append(imageNp)
        Ids.append(Id)
    
    return faces, Ids

def TrainImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Create recognizer
    harcascadePath = "haarcascade_default.xml"  # Path to the Haar Cascade
    detector = cv2.CascadeClassifier(harcascadePath)

    faces, Ids = getImagesAndLabels("TrainingImage")  # Get faces and IDs
    recognizer.train(faces, np.array(Ids))  # Train recognizer
    os.makedirs("TrainingImageLabel", exist_ok=True)  # Create directory if not exists
    recognizer.save("TrainingImageLabel/Trainner.yml")  # Save trained model
    print("All Images Trained")

def counter_img(path):
    imgcounter = 1
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    
    for imagePath in imagePaths:
        print(f"{imgcounter} Images Trained", end="\r")
        time.sleep(0.008)
        imgcounter += 1

