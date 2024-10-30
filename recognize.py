import datetime
import os
import time
import cv2
import pandas as pd

def recognize_attendance(): 
    recognizer = cv2.face.LBPHFaceRecognizer_create()  
    recognizer.read("TrainingImageLabel/Trainner.yml")  # Load the trained model
    harcascadePath = "haarcascade_default.xml"  # Path to the Haar Cascade
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    
    # Load student details with Id and Name
    df = pd.read_csv("StudentDetails/StudentDetails.csv", header=None, names=['Id', 'Name'])
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # DataFrame for attendance
    attendance = pd.DataFrame(columns=['Id', 'Name'])

    # Start real-time video capture
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640) 
    cam.set(4, 480) 
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5, minSize=(int(minW), int(minH)), flags=cv2.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (10, 159, 255), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            
            if conf < 100:
                aa = df.loc[df['Id'] == Id]['Name'].values
                confstr = "  {0}%".format(round(100 - conf))
                name = str(aa[0]) if len(aa) > 0 else "Unknown"
                attendance.loc[len(attendance)] = [Id, name]
            else:
                Id = '  Unknown  '
                name = 'Unknown'

            if (100 - conf) > 67:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                
                # Only add to attendance if recognized
                if name != 'Unknown':
                    attendance.loc[len(attendance)] = [Id, name]

            # Display recognized Id and confidence
            cv2.putText(im, f'{Id} - {name}', (x + 5, y - 5), font, 1, (255, 255, 255), 2)

        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('Attendance', im)
        if (cv2.waitKey(1) == ord('q')):
            break

    # Save attendance log to CSV
    fileName = "Attendance/Attendance_" + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".csv"
    attendance.to_csv(fileName, index=False)
    print("Attendance Successful")
    cam.release()
    cv2.destroyAllWindows()


