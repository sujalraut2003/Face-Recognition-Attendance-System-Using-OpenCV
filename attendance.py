import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Path to the folder containing images
path = 'images'
images = []
classNames = []
myList = os.listdir(path)
print(f"Loaded image files: {myList}")

# Load images and corresponding class names
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(f"Class Names: {classNames}")

# Function to find face encodings for all images
def findEncodings(images):
    encodeList = []
    for img in images:
        try:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        except IndexError:
            print(f"Face not found in image, skipping: {img}")
    return encodeList

# Function to record attendance in CSV
def attendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]

        if name not in nameList:
            time_now = datetime.now()
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%y')
            f.writelines(f'\n{name},{tStr},{dStr}')

# Get encodings of all images
encodeListKnown = findEncodings(images)
print('Encodings Complete')

# Start webcam feed
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture video")
        break

    # Resize frame for faster processing
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Find face locations and encodings in the current frame
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    # Compare each face with known encodings
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

            # Scale face locations back to the original frame size
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            # Draw rectangle around the face and display the name
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            # Mark attendance
            attendance(name)

    # Display the video feed with recognition boxes
    cv2.imshow('Webcam', img)

    # Exit on pressing the 'Enter' key
    if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
        break

cap.release()
cv2.destroyAllWindows()