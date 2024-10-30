# face-detection-attendance

Attendance system using Face Recognition with direct mail with csv of attending student

Set Up a Virtual Environment
Ensure you have virtualenv installed. You can install it using pip:
### python version: Python 3.12.3


pip install virtualenv


# Clone the project
git clone https://github.com/shivam201483101/face-detection-attendance
cd project

# Create a virtual environment
python -m virtualenv venv

# Activate the virtual environment
# Windows
.\venv\Scripts\activate


# Install dependencies
pip install -r requirements.txt

# Run the project
python main.py

Deactivating the Virtual Environment: After you're done, deactivate the virtual environment with:

deactivate
## Create necessary Folders
1.Attendance
2.ImagesBasic
3.StudentDetails
4.TrainingImage
5.TrainingImageLabel


# Output
***** Face Recognition Attendance System *****

********** WELCOME MENU **********
[1] Check Camera
[2] Capture Faces
[4] Recognize & Attendance
[5] Auto Mail
[6] Quit
Enter Choice : 
## press Q/q for close the camera/exit
## for capturing a student data it requires 101 frames per person so have patience
## after adding required no of student we can choose option 3 to train model
## after new addition re-train the model before choosing option 4 for recognixe and attendance
## after clicking 4 we can scan each person one by one and it will be added in a csv file
# Note:
The file name in automail.py is kept static change ,change the file name before sending/clicking option 5 Auto mail,or make it dynamic.
## Attendance_2024-10-30_13-18-46 to Attendance_current date/time string.csv 
Also create a account on twilio/sendGrid ,generate api key,generatea verified sender address to work ,and select web api and choose python during creation of api,donot select smtp for api key generation. 
