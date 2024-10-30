import csv
import cv2
import os


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def takeImages():
    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")

    if is_number(Id) and name.isalpha():
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath) 

        sampleNum = 0
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(
                gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE
            )

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                sampleNum += 1
                # Saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage" + os.sep + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum > 100:
                break

        cam.release()
        cv2.destroyAllWindows()

        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        # Save to StudentDetails.csv
        os.makedirs("StudentDetails", exist_ok=True)  # Create directory if it doesn't exist
        with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)

        print(res)

    else:
        if not is_number(Id):
            print("Enter Numeric ID")
        if not name.isalpha():
            print("Enter Alphabetical Name")

