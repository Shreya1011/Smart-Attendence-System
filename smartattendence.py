import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path='../image'
images=[]
classnames=[]
mylist=os.listdir(path)
print(mylist)

def load_images_from_folder(folder):
    for filename in os.listdir(folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(folder, filename)
            img = cv2.imread(img_path)
            if img is not None:
                images.append(img)
                classnames.append(os.path.splitext(filename)[0])
    return images, classnames

# print(classnames)
def findencodings(images):
    encodinglist=[]
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodinglist.append(encode)
    return encodinglist


def markattendence(name):
    with open('attendence.csv', 'r+') as f:
        mydatalist = f.readlines()
        namelist = []
        for line in mydatalist:
            entry = line.split(',')
            if len(entry) >= 2:  # Check if entry has at least two elements
                namelist.append((entry[0], entry[1].strip()))  # Tuple of (name, date)
            else:
                print("Malformed entry:", entry)  # Debug output

        now = datetime.now()
        datestring = now.strftime('%Y-%m-%d')
        timestring = now.strftime('%H:%M:%S')

        if (name, datestring) not in namelist:
            f.writelines(f'\n{name},{datestring},{timestring}')

        # print(mydatalist)

dataset_folder = '../image'
images, classnames = load_images_from_folder(dataset_folder)


encodelistknown=findencodings(images)
print('encoding complete')

cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()
    imgsmall=cv2.resize(img,(0,0),None,0.25,0.25)
    imgsmall = cv2.cvtColor(imgsmall, cv2.COLOR_BGR2RGB)
    facesincurrentframeloc = face_recognition.face_locations(imgsmall)
    encodecurrentframe = face_recognition.face_encodings(imgsmall,facesincurrentframeloc)

    for encodeface,faceloc in zip(encodecurrentframe,facesincurrentframeloc):
        matchedface=face_recognition.compare_faces(encodelistknown,encodeface)
        facedis=face_recognition.face_distance(encodelistknown,encodeface)
        # print(facedis)
        matchindex=np.argmin(facedis)

        if faceDis[matchIndex] < 0.50:
            name = classNames[matchIndex].upper()
            markAttendance(name)
        else:
            name = 'Unknown'
        # print(name)
        y1,x2,y2,x1=faceloc
        y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        font_scale = 0.7
        font_thickness = 2
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size = cv2.getTextSize(name, font, font_scale, font_thickness)[0]
        text_x = x1 + (x2 - x1) // 2 - text_size[0] // 2
        text_y = y2 + text_size[1] + 10
        cv2.putText(img, name, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness)
        # cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        markattendence(name)

    cv2.imshow('webcam',img)
    cv2.waitKey(1)



